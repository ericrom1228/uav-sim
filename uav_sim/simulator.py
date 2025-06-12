# uav_simulator.py

import numpy as np
from pid_controller import PIDController
from sensor import add_sensor_noise


class UAVSimulator:
    def __init__(self, config):
        self.dt = config["dt"]
        self.max_time = config["sim_time"]
        self.max_velocity = config["max_velocity"]
        self.tolerance = config["tolerance"]
        self.position = np.array(config["initial_position"], dtype=float)
        self.velocity = np.zeros(3)
        self.waypoints = [np.array(wp, dtype=float) for wp in config["waypoints"]]
        self.current_wp_idx = 0
        self.noise = config["sensor_noise"]

        self.pid_controllers = {
            "x": PIDController(**config["pid"]["x"], dt=self.dt),
            "y": PIDController(**config["pid"]["y"], dt=self.dt),
            "z": PIDController(**config["pid"]["z"], dt=self.dt),
        }

        self.trajectory = []

    def run(self):
        t = 0.0
        while t < self.max_time and self.current_wp_idx < len(self.waypoints):
            target = self.waypoints[self.current_wp_idx]
            error = target - self.position

            if np.linalg.norm(error) < self.tolerance:
                self.current_wp_idx += 1
                if self.current_wp_idx >= len(self.waypoints):
                    print(f"All waypoints reached in {t} seconds.")
                    break
                # Reset PID controllers for next waypoint
                for pid in self.pid_controllers.values():
                    pid.reset()
                continue

            accel = np.array([
                self.pid_controllers["x"].update(target[0], self.position[0]),
                self.pid_controllers["y"].update(target[1], self.position[1]),
                self.pid_controllers["z"].update(target[2], self.position[2]),
            ])

            self.velocity += accel * self.dt
            speed = np.linalg.norm(self.velocity)
            if speed > self.max_velocity:
                self.velocity = (self.velocity / speed) * self.max_velocity

            self.position += add_sensor_noise(self.velocity * self.dt)
            self.position += self.velocity * self.dt
            self.trajectory.append((t, *self.position, *self.velocity, *error))
            t += self.dt

        print("Simulation complete.")

    def save_to_csv(self, filename="simulation_output.csv"):
        import csv
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["time", "x", "y", "z", "vx", "vy", "vz", "ex", "ey", "ez"])
            writer.writerows(self.trajectory)

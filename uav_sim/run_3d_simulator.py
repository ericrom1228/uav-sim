# run_3d_simulation.py

import csv
from uav_sim.controller.pid import PIDController
from uav_sim.controller.simulator import UAVSimulator
from uav_sim.plot_3d_animated import animate_3d_flight


def run_simulation():
    target = [20.0, 50.0, 10.0]  # x,y,z

    pid_x = PIDController(1.0, 0.0, 0.3)
    pid_y = PIDController(1.0, 0.0, 0.3)
    pid_z = PIDController(1.0, 0.0, 0.3)

    drone = UAVSimulator()
    dt = 0.1  # seconds
    sim_time = 10  # seconds
    positions = []

    with open("data/flight_log_3d.csv", "x+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "position", "velocity", "error"])

        for step in range(1, int(sim_time / dt) + 1):
            time = step * dt
            pos = drone.get_position()
            error = [target[i] - pos[i] for i in range(3)]

            vx = pid_x.update(error[0], dt)
            vy = pid_y.update(error[1], dt)
            vz = pid_z.update(error[2], dt)

            writer.writerow([time, drone.position, drone.velocity, error])
            positions.append(pos.copy())
            drone.update([vx, vy, vz], dt)

    # animate_3d_flight(positions, target, dt, save_path="uav_simulation.gif")
    animate_3d_flight(positions, target, dt)


if __name__ == "__main__":
    run_simulation()

# simulator.py

import numpy as np
import pandas as pd
from pid_controller import PIDController
from sensor import add_sensor_noise


class UAVSimulator:
    def __init__(self, config):
        self.dt = config["dt"]
        self.sim_time = config["sim_time"]
        self.start_position = np.array(config["start_position"], dtype=float)
        self.target_position = np.array(config["target_position"], dtype=float)
        self.max_velocity = config["max_velocity"]

        self.position = self.start_position.copy()
        self.velocity = np.zeros(3)

        self.pid_x = PIDController(**config["pid"]["x"])
        self.pid_y = PIDController(**config["pid"]["y"])
        self.pid_z = PIDController(**config["pid"]["z"])

        self.history = []

    def clip_velocity(self, velocity):
        speed = np.linalg.norm(velocity)
        if speed > self.max_velocity:
            return velocity * (self.max_velocity / speed)
        return velocity

    def run(self):
        steps = int(self.sim_time / self.dt)
        for step in range(steps):
            error = self.target_position - self.position

            vx = self.pid_x.compute(error[0], self.dt)
            vy = self.pid_y.compute(error[1], self.dt)
            vz = self.pid_z.compute(error[2], self.dt)

            self.velocity = np.array([vx, vy, vz])
            self.velocity = self.clip_velocity(self.velocity)

            self.position += add_sensor_noise(self.velocity * self.dt)

            self.history.append({
                "time": step * self.dt,
                "x": self.position[0],
                "y": self.position[1],
                "z": self.position[2],
                "vx": self.velocity[0],
                "vy": self.velocity[1],
                "vz": self.velocity[2],
            })

        return pd.DataFrame(self.history)

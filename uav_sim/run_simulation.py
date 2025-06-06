import csv
from uav_sim.controller.pid import PIDController
from uav_sim.controller.simulator import UAVSimulator
from uav_sim.controller.sensor import add_sensor_noise


def run():
    setpoint = 10.0
    dt = 0.1
    sim_time = 10

    pid = PIDController(kp=1.0, ki=0.1, kd=0.05)
    sim = UAVSimulator()

    with open("data/flight_log.csv", "x+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "position", "velocity", "error", "command"])

        for step in range(int(sim_time / dt)):
            time = step * dt
            noisy_position = add_sensor_noise(sim.position)
            error = setpoint - noisy_position
            command = pid.update(error, dt)
            sim.step(command, dt)
            writer.writerow([time, sim.position, sim.velocity, error, command])


if __name__ == "__main__":
    run()

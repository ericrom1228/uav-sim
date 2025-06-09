# pid_controller.py

class PIDController:
    def __init__(self, kp, ki, kd, dt):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint, measured):
        error = setpoint - measured
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt

        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )
        self.prev_error = error
        return output

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

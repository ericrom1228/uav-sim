class UAVSimulator:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]  # x, y, z
        self.velocity = [0.0, 0.0, 0.0]  # vx, vy, vz
        self.max_velocity = 10.0  # set physical limitations

    def update(self, velocity_vector: list[float], dt: float) -> None:
        for i in range(3):
            self.velocity[i] = min(velocity_vector[i], self.max_velocity)
            self.position[i] += self.velocity[i] * dt

    def get_position(self) -> list[float]:
        return self.position

class UAVSimulator:
    def __init__(self, initial_position=0.0, initial_velocity=0.0):
        self.position = initial_position
        self.velocity = initial_velocity
        self.history = []

    def step(self, acceleration, dt):
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.history.append((self.position, self.velocity))

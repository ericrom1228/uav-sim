import random


def add_sensor_noise(value, noise_std=0):
    return value + random.gauss(0, noise_std)
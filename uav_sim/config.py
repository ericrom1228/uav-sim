# config.py

SIM_CONFIG = {
    "initial_position": [0.0, 0.0, 0.0],
    "waypoints": [
        [5.0, 0.0, 2.0],
        [5.0, 5.0, 2.0],
        [0.0, 5.0, 2.0],
        [0.0, 0.0, 2.0]
    ],
    "max_velocity": 10.0,
    "dt": 0.01,
    "sim_time": 40.0,
    "tolerance": 0.2,
    "pid": {
        "x": {"kp": 1.2, "ki": 0.0, "kd": 0.5},
        "y": {"kp": 1.2, "ki": 0.0, "kd": 0.5},
        "z": {"kp": 1.5, "ki": 0.0, "kd": 0.6},
    }
}

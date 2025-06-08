# config.py

SIM_CONFIG = {
    "dt": 0.001,
    "sim_time": 10.0,
    "start_position": [0.0, 0.0, 0.0],
    "target_position": [10.0, 5.0, 3.0],
    "max_velocity": 10.0,
    "pid": {
        "x": {"kp": 1.2, "ki": 0.0, "kd": 0.3},
        "y": {"kp": 1.2, "ki": 0.0, "kd": 0.3},
        "z": {"kp": 1.0, "ki": 0.0, "kd": 0.2},
    }
}

# uav-sim
Unmanned Aerial Vehicle Simulator

# Project Structure
```
uav_sim_project/
+-- controller/
|   +-- pid.py                # PID control class
|   +-- simulator.py          # Simulates UAV movement
|   +-- sensor.py             # Simulated noisy sensor
|-- tests/
|   +-- test_pid.py           # Unit tests for PID
|   +-- test_simulator.py     # Tests for simulation logic
|-- data/
|   +-- flight_log.csv        # Output log
|-- scripts/
|   +-- run_simulation.py     # Main entrypoint
|-- notebooks/
|   +-- analyze_flight.ipynb  # Plot and analyze log data
|-- requirements.txt
```

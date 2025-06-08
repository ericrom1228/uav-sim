# uav-sim
Basic Unmanned Aerial Vehicle Simulator.

# Project Structure
```
uav-sim/
|  +-- uav_sim/
|  |   +-- config.py           # Configuration
|  |   +-- pid_controller.py   # PID control class
|  |   +-- simulator.py        # Simulates UAV movement
|  |   +-- run_simulation.py   # Main entrypoint
|  |   +-- plot_3d.py          # Plot and analyze log data
|-- requirements.txt
```

# Run the simulation
```
cd uav_sim
python run_simulation.py
```

# Plot the results
```
cd uav_sim
python plot_3d.py
```
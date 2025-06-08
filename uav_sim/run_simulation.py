# run_simulator.py

from config import SIM_CONFIG
from simulator import UAVSimulator

if __name__ == "__main__":
    sim = UAVSimulator(SIM_CONFIG)
    df = sim.run()
    df.to_csv("simulation_output.csv", index=False)
    print("Simulation complete. Output saved to simulation_output.csv")

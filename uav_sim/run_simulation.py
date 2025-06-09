# run_simulator.py

from config import SIM_CONFIG
from simulator import UAVSimulator


def main():
    sim = UAVSimulator(SIM_CONFIG)
    sim.run()
    sim.save_to_csv()


if __name__ == "__main__":
    main()

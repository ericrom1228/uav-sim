import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename="simulation_output.csv"):
    return pd.read_csv(filename)


def plot_position(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["time"], df["x"], label="x")
    plt.plot(df["time"], df["y"], label="y")
    plt.plot(df["time"], df["z"], label="z")
    plt.title("Position vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/position_vs_time.png")
    # plt.show()


def plot_velocity(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["time"], df["vx"], label="vx")
    plt.plot(df["time"], df["vy"], label="vy")
    plt.plot(df["time"], df["vz"], label="vz")
    plt.title("Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/velocity_vs_time.png")
    # plt.show()


def plot_error(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["time"], df["ex"], label="Error x")
    plt.plot(df["time"], df["ey"], label="Error y")
    plt.plot(df["time"], df["ez"], label="Error z")
    plt.title("Error vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Error (m)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/error_vs_time.png")
    # plt.show()


def plot_trajectory(df):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(df["x"], df["y"], df["z"], label="UAV Trajectory", color="blue")
    ax.scatter(df["x"].iloc[0], df["y"].iloc[0], df["z"].iloc[0], color="green", label="Start", s=50)
    ax.scatter(df["x"].iloc[-1], df["y"].iloc[-1], df["z"].iloc[-1], color="red", label="End", s=50)
    ax.set_title("3D UAV Trajectory")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.legend()
    plt.tight_layout()
    plt.savefig("plots/trajectory_3d.png")
    # plt.show()


if __name__ == "__main__":
    df = load_data()
    plot_position(df)
    plot_velocity(df)
    plot_error(df)
    plot_trajectory(df)

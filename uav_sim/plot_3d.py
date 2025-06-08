# plot_3d.py

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from matplotlib.animation import FuncAnimation
from config import SIM_CONFIG

# Load simulation results
df = pd.read_csv("simulation_output.csv")

# Extract simulation metadata
target = SIM_CONFIG["target_position"]
dt = SIM_CONFIG["dt"]
stride = 10  # adjust for performance vs. smoothness

# Prepare 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Initialize plot elements
line, = ax.plot([], [], [], "b-", label="Drone Path")
point, = ax.plot([], [], [], "ro", label="Drone")
target_point, = ax.plot([target[0]], [target[1]], [target[2]], "gx", markersize=10, label="Target")

time_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)


def init():
    ax.set_xlim(df["x"].min() - 1, df["x"].max() + 1)
    ax.set_ylim(df["y"].min() - 1, df["y"].max() + 1)
    ax.set_zlim(df["z"].min() - 1, df["z"].max() + 1)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.legend()
    return line, point, time_text


def update(frame):
    i = frame * stride
    if i >= len(df):
        return line, point, time_text

    # Update the drone's path
    x = df["x"][:i]
    y = df["y"][:i]
    z = df["z"][:i]
    line.set_data(x, y)
    line.set_3d_properties(z)

    # Update the drone's current position (as a single point)
    point.set_data([df["x"][i]], [df["y"][i]])
    point.set_3d_properties([df["z"][i]])

    # Update time text
    time_text.set_text(f"Time: {df['time'][i]:.2f}s")
    return line, point, time_text


# Animate
ani = FuncAnimation(
    fig, update,
    frames=range(0, len(df) // stride),
    init_func=init,
    interval=SIM_CONFIG["dt"] * stride * 1000,
    blit=False,
    repeat=False
)

plt.tight_layout()
plt.show()

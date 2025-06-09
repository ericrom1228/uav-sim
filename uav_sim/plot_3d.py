# plot_3d.py

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D projection
from config import SIM_CONFIG
import numpy as np

# Load data
df = pd.read_csv("simulation_output.csv")

# Extract time and position arrays
times = df["time"].values
x = df["x"].values
y = df["y"].values
z = df["z"].values

# Set up figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D UAV Flight Path Simulation")

# Plot waypoints
wps = np.array(SIM_CONFIG["waypoints"])
ax.scatter(wps[:, 0], wps[:, 1], wps[:, 2], color="red", label="Waypoints", s=50)

waypoints = SIM_CONFIG["waypoints"]
tolerance = SIM_CONFIG["tolerance"]
current_wp_index = [0]  # Wrap in list so it's mutable inside update()

# Plot elements
line, = ax.plot([], [], [], lw=2, color="blue", label="UAV Trajectory")
point, = ax.plot([], [], [], "bo", label="Current Position")
target_dot, = ax.plot([], [], [], "rx", label="Target Waypoint", markersize=10)
time_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)

ax.legend()

# Init function
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    target_dot.set_data([], [])
    target_dot.set_3d_properties([])
    time_text.set_text("")
    return line, point, target_dot, time_text


# Animation update function
def update(i):
    if i >= len(times):
        return line, point, target_dot, time_text

    # Update trajectory
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])

    # Current position
    point.set_data([x[i]], [y[i]])
    point.set_3d_properties([z[i]])

    # Get current waypoint
    if current_wp_index[0] < len(waypoints):
        wp = np.array(waypoints[current_wp_index[0]])
        current_pos = np.array([x[i], y[i], z[i]])
        dist_to_wp = np.linalg.norm(current_pos - wp)

        # Move to next waypoint if close enough
        if dist_to_wp <= tolerance:
            current_wp_index[0] += 1

    # Plot target waypoint if any left
    if current_wp_index[0] < len(waypoints):
        wp = waypoints[current_wp_index[0]]
        target_dot.set_data([wp[0]], [wp[1]])
        target_dot.set_3d_properties([wp[2]])
    else:
        target_dot.set_data([], [])
        target_dot.set_3d_properties([])

    # Update time label
    time_text.set_text(f"Time: {times[i]:.2f}s")
    return line, point, target_dot, time_text


# Real-time interval matching dt
dt_seconds = SIM_CONFIG["dt"]
interval_ms = int(dt_seconds * 1000)

ani = animation.FuncAnimation(
    fig, update,
    frames=len(times),
    init_func=init,
    blit=False,
    interval=interval_ms,
    repeat=False
)

# plt.show()

# # Save as GIF
# ani.save("uav_simulation.gif", writer="pillow", fps=int(1 / dt_seconds))
# print("Saved animation to uav_simulation.gif")

# Save as MP4 using ffmpeg
ani.save("uav_simulation.mp4", writer="ffmpeg", fps=int(1 / dt_seconds))
print("Saved animation to uav_simulation.mp4")

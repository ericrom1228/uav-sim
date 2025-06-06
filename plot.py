import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

df = pd.read_csv("data/flight_log.csv")

fig, ax = plt.subplots()
ax.set_xlim(0, 12)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], 'ro', markersize=10)
target = ax.axvline(x=10, color='green', linestyle='--', label='Target')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def update(frame):
    x = df.iloc[frame]["position"]
    time = df.iloc[frame]["time"]
    line.set_data(x, 0)
    time_text.set_text(f'Time: {time:.2f}s')
    return line, time_text


ani = animation.FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=100)

plt.title("UAV Flight Simulation")
plt.legend()
plt.xlabel("Position")
plt.show()

# Optionally save:
# ani.save("uav_sim.gif", writer="imagemagick", fps=10)

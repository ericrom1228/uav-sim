import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv("data/flight_log.csv")

fig, ax = plt.subplots()
ax.set_xlim(0, df["position"].max() + 1)
ax.set_ylim(-1, 1)

line, = ax.plot([], [], "bo", markersize=10)  # Blue circle for drone
time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text("")
    return line, time_text


def update(frame):
    x = df.iloc[frame]["position"]
    time = df.iloc[frame]["time"]
    line.set_data([x], [0])  # ✅ FIXED HERE
    time_text.set_text(f"Time: {time:.2f}s")
    return line, time_text


ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(df),
    init_func=init,
    blit=True,
    interval=10,
    repeat=False
)

plt.title("Drone Position Over Time")
plt.xlabel("Position (meters)")
plt.yticks([])
plt.grid(True)
plt.tight_layout()
plt.show()

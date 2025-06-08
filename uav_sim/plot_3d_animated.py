# plot_3d_animated.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


def animate_3d_flight(position_history, target_position, dt, save_path=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    max_range = max(
        max(p[i] for p in position_history) for i in range(3)
    ) + 2

    ax.set_xlim(0, max_range)
    ax.set_ylim(0, max_range)
    ax.set_zlim(0, max_range)

    line, = ax.plot([], [], [], lw=2, label="UAV Path", color="blue")
    dot, = ax.plot([], [], [], 'bo', label="UAV Position")  # Current UAV position
    target = ax.scatter(*target_position, color="red", label="Target", s=50)

    # Labels
    position_text = ax.text2D(0.05, 0.92, "", transform=ax.transAxes)
    time_text = ax.text2D(0.05, 0.86, "", transform=ax.transAxes)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Animated 3D UAV Flight")
    ax.legend()

    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        dot.set_data([], [])
        dot.set_3d_properties([])
        position_text.set_text("")
        time_text.set_text("")
        return line, dot, position_text, time_text

    def update(frame):
        xs = [p[0] for p in position_history[:frame + 1]]
        ys = [p[1] for p in position_history[:frame + 1]]
        zs = [p[2] for p in position_history[:frame + 1]]

        line.set_data(xs, ys)
        line.set_3d_properties(zs)

        dot.set_data(xs[-1:], ys[-1:])
        dot.set_3d_properties(zs[-1:])

        time_text.set_text(f"Time: {frame * dt:.1f} s")
        position_text.set_text(f"UAV Position: ({xs[-1]:.2f}, {ys[-1]:.2f}, {zs[-1]:.2f})")

        return line, dot, position_text, time_text

    ani = FuncAnimation(
        fig, update, frames=100,
        init_func=init, blit=False, interval=100, repeat=False
    )

    if save_path:
        print(f"Saving animation to {save_path}...")
        ani.save(save_path, writer='pillow', fps=20)
        print("Saved successfully.")
    else:
        plt.tight_layout()
        plt.show()

    plt.tight_layout()
    plt.show()

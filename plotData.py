import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
import argparse

def scale_axes(ax):
    # Scale axes properly
    # https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.axes.zaxis.set_ticklabels([])
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    ax.axes.zaxis.set_ticks([])


def plot_data(data, ax, rotate=True):
    if rotate:
        ax.scatter(data[0, :], data[2, :], -data[1, :])

        ax.view_init(elev=10, azim=-60)

    else:
        ax.scatter(data[0, :], data[1, :], data[2, :])

        ax.view_init(elev=-90, azim=-90)


def rotate_and_save(figure, axis, filename, save=False):
    def init():
        return figure,

    def animate(i):
        axis.view_init(elev=10., azim=i)
        return figure,

    # Animate
    anim = animation.FuncAnimation(figure, animate, init_func=init,
                                   frames=360, interval=20, blit=True)
    plt.close()

    # Save
    if save:
        anim.save(filename, fps=30, extra_args=['-vcodec', 'libx264'], dpi=300)



# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True,
	help="path to data file")
args = vars(ap.parse_args())

# Plot the data
fig = plt.figure()
fig.set_size_inches(5, 5, True)
ax = fig.add_subplot(projection='3d')
parsedData = np.genfromtxt(args["data"], delimiter=',')
plot_data(parsedData, ax)
scale_axes(ax)

# Save a rotation animation of the data
filename = 'pose_rotation.mp4'
rotate_and_save(fig, ax, filename, save=True)
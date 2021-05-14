
import time
import numpy as np
import matplotlib.pyplot as plt

# Settings
WINDOW = 2
T = 10
t = 0
dt = 0.1
tsamp = 0

data = {
    "t": [],
    "x1": [],
    "x2": [],
    "y1": [],
    "y2": []
}

def get_data(t):

    x1 = np.sin(t)
    x2 = 0.5*np.sin(2*t)
    y1 = np.cos(t)
    y2 = 0.5*np.cos(2*t)

    return (t, x1, x2, y1, y2)

def store_data(telem):

    data["t"].append(telem[0])
    data["x1"].append(telem[1])
    data["x2"].append(telem[2])
    data["y1"].append(telem[3])
    data["y2"].append(telem[4])

    if data["t"][-1] - data["t"][0] > WINDOW:
        for k, v in data.items():
            data[k] = v[1:]

# Initialise plots

plt.ion()
fig, axs = plt.subplots(1, 2, figsize=(10, 6))
lnx1, = axs[0].plot(0, 0)
lnx2, = axs[0].plot(0, 0)
lny1, = axs[1].plot(0, 0)
lny2, = axs[1].plot(0, 0)
lines = [lnx1, lnx2, lny1, lny2]
for ax in axs:
    ax.set_xlabel("Time [s]")
    ax.set_xlim([0, WINDOW])
    ax.set_ylim([-1.2, 1.2])
    ax.grid()
axs[0].set_ylabel("x")
axs[1].set_ylabel("y")

fig.canvas.draw()

# Update plots
def plot_data(data):

    for ln in lines:
        ln.set_xdata(data["t"])

    lnx1.set_ydata(data["x1"])
    lnx2.set_ydata(data["x2"])
    lny1.set_ydata(data["y1"])
    lny2.set_ydata(data["y2"])

    if data["t"][-1] > WINDOW:
        axs[0].set_xlim([data["t"][0], data["t"][-1]])
        axs[1].set_xlim([data["t"][0], data["t"][-1]])

    fig.canvas.draw()
    fig.canvas.flush_events()

# Initialise time
t0 = time.time()
t = time.time() - t0

while t < T:

    if t > tsamp:
        tsamp += dt

        telem = get_data(t)

        store_data(telem)

        # print(data["t"])

        plot_data(data)
    
    t = time.time() - t0

print("DONE")

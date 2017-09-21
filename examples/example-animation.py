
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()

data = np.random.randint(0, 2, size=(100, 100))
pts = plt.imshow(data, animated=True)

def generate(i):
    pts.set_array(np.random.randint(0, 2, size=(100, 100)))
    return pts


ani = animation.FuncAnimation(fig, generate, frames=100,
                              interval=20, repeat=False)
plt.show()
ani.save('animamtion.mp4')

import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create line plots
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Sine Wave')
line2, = ax.plot(x, y2, label='Cosine Wave')
ax.legend()

# Enable hover functionality
mplcursors.cursor([line1, line2], hover=True)

plt.show()
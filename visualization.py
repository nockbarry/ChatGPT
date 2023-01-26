import matplotlib.pyplot as plt
import numpy as np

# Generate some fake data to visualize
x = np.linspace(0, 10, 100)
y = x * x + 2 * x + 1

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data on the axis
ax.plot(x, y)

# Add a title and labels to the plot
ax.set_title("Quadratic Function")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Show the plot
plt.show()
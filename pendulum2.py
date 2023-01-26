import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set the length of each pendulum link
l1 = 1
l2 = 1
l3 = 1

# Set the gravitational acceleration
g = -9.81

# Set the initial angle of the pendulum links (in radians)
theta1_0 = np.pi/2
theta2_0 = np.pi/2
theta3_0 = np.pi/2

# Set the initial angular velocity of the pendulum links (in radians/second)
omega1_0 = 0.001
omega2_0 = 0.002
omega3_0 = 0.003

# Set the time step for the simulation
dt = 0.05

# Set the number of time steps to simulate
num_steps = 10000

# Initialize lists to store the angle and angular velocity of each pendulum link at each time step
theta1_list = [theta1_0]
theta2_list = [theta2_0]
theta3_list = [theta3_0]
omega1_list = [omega1_0]
omega2_list = [omega2_0]
omega3_list = [omega3_0]

# Set up the figure and subplot
fig, ax = plt.subplots(figsize=(10,10))

# Set the axis limits
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))

# Initialize the line objects for each pendulum link
line1, = ax.plot([], [], 'o-', lw=2)
line2, = ax.plot([], [], 'o-', lw=2)
line3, = ax.plot([], [], 'o-', lw=2)

# Initialize the point object for the tip of the pendulum
point, = ax.plot([], [], 'k.', markersize=1)
x_positions = []
y_positions = []
# Initialize the line object for the path of the tip
path_line, = ax.plot([], [], 'k-', lw=1)
# Function to update the animation at each time step


def animate(i):
    # Calculate the acceleration of each pendulum link using the equations of motion
    alpha1 = -g*(2*l2*np.sin(theta1_list[-1]-theta2_list[-1]) + l3*np.sin(theta1_list[-1]-theta3_list[-1]))/(l1*3)
    alpha2 = -g*(l2*np.sin(theta2_list[-1]-theta1_list[-1]) + l3*np.sin(theta2_list[-1]-theta3_list[-1]))/(l2*3)
    alpha3 = -g*l3*np.sin(theta3_list[-1]-theta2_list[-1])/(l3*3)

    # Update the angular velocity of each pendulum link using the equations of motion
    omega1_list.append(omega1_list[-1] + alpha1*dt)
    omega2_list.append(omega2_list[-1] + alpha2*dt)
    omega3_list.append(omega3_list[-1] + alpha3*dt)

    # Update the angle of each pendulum link using the equations of motion
    theta1_list.append(theta1_list[-1] + omega1_list[-1]*dt)
    theta2_list.append(theta2_list[-1] + omega2_list[-1]*dt)
    theta3_list.append(theta3_list[-1] + omega3_list[-1]*dt)

    # Calculate the x and y position of each pendulum link
    x1 = l1*np.sin(theta1_list[-1])
    y1 = -l1*np.cos(theta1_list[-1])
    x2 = x1 + l2*np.sin(theta2_list[-1])
    y2 = y1 - l2*np.cos(theta2_list[-1])
    x3 = x2 + l3*np.sin(theta3_list[-1])
    y3 = y2 - l3*np.cos(theta3_list[-1])

    x_positions.append(x3)
    y_positions.append(y3)

    # Update the line and point objects with the new positions
    line1.set_data([0, x1], [0, y1])
    line2.set_data([x1, x2], [y1, y2])
    line3.set_data([x2, x3], [y2, y3])
    point.set_data(x3, y3)
    
    path_line.set_data(x_positions, y_positions)

    return line1, line2, line3, point
# Create the animation object


anim = animation.FuncAnimation(fig, animate, frames=range(num_steps), interval=1)

# Show the animation
plt.show()

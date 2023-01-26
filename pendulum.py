import numpy as np

# Constants
m = 1.0  # mass of pendulum (kg)
l = 1.0  # length of pendulum (m)
g = 9.81  # acceleration due to gravity (m/s^2)

# Initial conditions
theta_0 = np.pi / 2  # initial angle (radians)
omega_0 = 0.0  # initial angular velocity (rad/s)

# Simulation parameters
t_0 = 0.0  # start time (s)
t_f = 10.0  # end time (s)
dt = 0.01  # time step (s)

# Set up time array for simulation
t = np.arange(t_0, t_f, dt)

# Initialize arrays to store results
theta = np.zeros_like(t)
omega = np.zeros_like(t)

# Set initial conditions
theta[0] = theta_0
omega[0] = omega_0

# Control gain
kp = 10.0  # proportional gain
kd = 5.0   # derivative gain

# Main loop
for i in range(len(t) - 1):
    # Calculate control input
    u = -kp * theta[i] - kd * omega[i]

    # Update angular velocity
    omega[i+1] = omega[i] + dt * (g/l) * np.sin(theta[i]) + dt * u/m

    # Update angle
    theta[i+1] = theta[i] + dt * omega[i+1]

# Plot results
import matplotlib.pyplot as plt

plt.plot(t, theta)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.show()
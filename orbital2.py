import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67408e-11  # gravitational constant
M_earth = 5.972e24  # mass of Earth
M_moon = 7.347e22  # mass of Moon
R_earth = 6371e3  # radius of Earth
R_moon = 1737e3  # radius of Moon

# Initial positions and velocities
r_earth = np.array([0.0, 0.0])  # initial position of Earth
r_moon = np.array([384400e3, 0.0])  # initial position of Moon
v_earth = np.array([0.0, 0.0])  # initial velocity of Earth
v_moon = np.array([0.0, 1022e3])  # initial velocity of Moon

# Time step and duration of simulation
dt = 3600  # time step (s)
t_max = 30*24*3600  # duration of simulation (s)

# Initialize lists to store position and velocity data for each body
r_earth_list = [r_earth]
r_moon_list = [r_moon]
v_earth_list = [v_earth]
v_moon_list = [v_moon]

# Loop through time steps
for t in range(int(t_max/dt)):
  # Calculate force acting on each body
  r = r_moon - r_earth
  r_mag = np.linalg.norm(r)
  F = G*M_earth*M_moon*r/r_mag**2
  
  # Calculate intermediate velocities and positions using Runge-Kutta method
  v_earth_half = v_earth + F*dt/(2*M_earth)
  r_earth_half = r_earth + v_earth*dt/2
  v_moon_half = v_moon - F*dt/(2*M_moon)
  r_moon_half = r_moon + v_moon*dt/2
  
  r_half = r_moon_half - r_earth_half
  r_mag_half = np.linalg.norm(r_half)
  F_half = G*M_earth*M_moon*r_half/r_mag_half**2
  
  # Update velocities and positions
  v_earth += F_half*dt/M_earth
  r_earth += v_earth_half*dt
  v_moon -= F_half*dt/M_moon
  r_moon += v_moon_half*dt
  
  # Append data to lists
  v_earth_list.append(v_earth)
  v_moon_list.append
  v_moon_list.append(v_moon)
  r_earth_list.append(r_earth)
  r_moon_list.append(r_moon)

# Convert position lists to arrays for easier plotting
r_earth_array = np.array(r_earth_list)
r_moon_array = np.array(r_moon_list)

# Create figure and axes for the plot
fig, ax = plt.subplots()

# Plot the orbits of the Earth and Moon
ax.plot(r_earth_array[:,0], r_earth_array[:,1], label='Earth')
ax.plot(r_moon_array[:,0], r_moon_array[:,1], label='Moon')

# Add a legend
ax.legend()

# Set the x and y limits of the plot
ax.set_xlim(-4e8, 4e8)
ax.set_ylim(-4e8, 4e8)

# Show the plot
plt.show()

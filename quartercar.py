import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the state space model of the quarter car
def quarter_car_model(t, z, F, F_d):
    # Unpack the states
    y, y_dot = z

    # Define the state equations
    y_ddot = (F - F_d*y_dot)/m - g
    dy_dt = y_dot

    # Return the state derivatives
    return [dy_dt, y_ddot]

# Define the model parameters
m = 1000  # Body mass [kg]
k = 15000  # Suspension spring stiffness [N/m]
c = 1500   # Suspension damper coefficient [N/(m/s)]
g = 9.81   # Gravitational acceleration [m/s^2]

# Define the simulation parameters
t_init = 0          # Initial time [s]
t_final = 10        # Final time [s]
t_step = 0.01       # Time step [s]
t_eval = np.arange(t_init, t_final, t_step)  # Time points for evaluation
y_init = [0, 0]     # Initial state [y, y_dot] (vertical displacement and velocity of body)
F_init = 0          # Initial suspension force [N]
F_d = 10             # Damping force [N]
F = 500
# Define the control system for a step input
def control_system(t):
    if t < 1:
        return F_init
    else:
        return F

# Solve the initial value problem using the `scipy.integrate.solve_ivp` function
sol = solve_ivp(fun=lambda t, z: quarter_car_model(t, z, control_system(t), F_d), t_span=[t_init, t_final], 
                y0=y_init, t_eval=t_eval)

# Extract the simulated states and input
t = sol.t
y = sol.y
F = [control_system(t_i) for t_i in t]

# Plot the response of the vertical displacement and velocity of the body
plt.figure()
plt.plot(t, y[0, :], 'b', label='Vertical displacement')
plt.plot(t, y[1, :], 'r', label='Vertical velocity')
plt.plot(t, F, 'g', label='Suspension force')
plt.xlabel('Time [s]')
plt.ylabel('Displacement [m] or Velocity [m/s] or Force [N]')
plt.legend()

# Plot the state-space trajectory of the body
plt.figure()
plt.plot(y[0, :], y[1, :])
plt.xlabel('Vertical displacement [m]')
plt.ylabel('Vertical velocity [m/s]')

# Plot the phase portrait of the body
plt.figure()
plt.show()
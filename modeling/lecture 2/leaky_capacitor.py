import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

# Constants for the membrane
eps_0 = 8.854 * 10**-12  # Permittivity of free space (F/m)
eps_r = 2.0  # Relative permittivity of the membrane (estimated, typical range 2-3)
membrane_area = 12.6 * 10**-6  # in m² 
membrane_thickness = 8 * 10**-9  # in m
R = 1e9  # Membrane resistance in ohms 

# Resting membrane potential (in volts)
V_initial = -65e-3  # Resting potential in volts

# Simulated input currents (time, current in amperes)
current = [(0, 10 * 10**-9), (1, 15 * 10**-9), (2, 5 * 10**-9), (3, 0)]  # (time, current)

# Compute voltage using the equation: dV/dt = -(1/tau)(V - V_inf)
def compute_voltage(V_initial: float, R: float, I: List[Tuple[float, float]], tau: float, time_points: np.ndarray) -> np.ndarray:
    I_values = [t[1] for t in I]
    time_intervals = [t[0] for t in I]

    voltage = [V_initial]
    current_index = 0

    for t in time_points[1:]:
        # Move the current index to the nearest available current time
        while current_index < len(time_intervals) - 1 and t > time_intervals[current_index + 1]:
            current_index += 1
        
        V_inf = I_values[current_index] * R  # V_inf determined by current at the current time
        V_new = voltage[-1] + (-1 / tau) * (voltage[-1] - V_inf) * (t - time_points[current_index])
        voltage.append(V_new)

    return np.array(voltage)

# Calculate capacitance and time constant tau
C = eps_0 * eps_r * membrane_area / membrane_thickness  
tau = R * C  

# Generate a finer time grid (interpolating between existing time points)
time_points_fine = np.linspace(0, 3, 500)  

voltage_smooth = compute_voltage(V_initial, R, current, tau, time_points_fine)

time_values = [t[0] for t in current]
current_values = [t[1] for t in current]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(time_points_fine, voltage_smooth, label='Membrane Voltage (V)', color='b')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Membrane Voltage (V)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(time_values, current_values, label='Injected Current (I)', color='r', marker='x')
ax2.set_ylabel('Current (A)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Leaky Capacitor Model: Voltage and Injected Current Over Time')
ax1.grid(True)

plt.tight_layout()
plt.savefig("leaky_capacitor.png")  
plt.close() 

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

eps_0 = 8.854 * 10**-12  # Permittivity of free space (F/m)
eps_r = 2.0  # Relative permittivity of the membrane (estimated, typical range 2-3)
membrane_area = 12.6 * 10**-6  # in m² 
membrane_thickness = 8 * 10**-9  # in m 

# Resting membrane potential in volts 
initial_voltage = -65 * 10**-3

# Simulated input currents (time, current in amperes)
current = [(0, 10 * 10**-9), (1, 15 * 10**-9), (2, 5 * 10**-9), (3, 0)]  # (time, current)

# Compute voltage given capacitor properties, initial voltage, and currents at given times
def compute_voltage(A: float, L: float, V_initial: float, I: List[Tuple[float, float]]) -> List[float]:
    
    # Membrane capacitance
    C = eps_0 * eps_r * A / L

    # Initialize the voltage list
    voltage = [V_initial]

    # Time intervals (assume uniform time steps for simplicity)
    time_intervals = [t[0] for t in I]
    current_values = [t[1] for t in I]

    for i in range(1, len(I)):
        dQ = current_values[i] * (time_intervals[i] - time_intervals[i-1])
        # Update voltage (V = V_previous + ΔV, where ΔV = Q / C)
        V_new = voltage[-1] + dQ / C
        voltage.append(V_new)

    return voltage

voltage = compute_voltage(membrane_area, membrane_thickness, initial_voltage, current)

time = [t[0] for t in current]
current_values = [t[1] for t in current]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(time, voltage, label='Membrane Voltage (V)', color='b', marker='o')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(time, current_values, label='Injected Current (I)', color='r', marker='x')
ax2.set_ylabel('Current (A)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Perfect Capacitor Model: Voltage and Injected Current Over Time')
ax1.grid(True)

plt.tight_layout()
plt.savefig("perfect_capacitor.png")  
plt.close() 

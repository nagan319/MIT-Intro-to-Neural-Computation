## Lecture 2 Quiz

### Simple Capacitor Model

1. Why is a neuron a capacitor?
   
2. What is capacitive current and how does it create potential difference?

3. How can the definition of capacitance be used to establish a relationship between an input current and the resulting voltage change? 

4. How does increasing membrane surface area affect the change in voltage as described by this model?

### Leaky Capacitor Model

1. What causes neurons to be 'leaky'? How can this be modeled using an electric circuit?

2. Starting from $I_L+I_C=I_e$, with $I_L$ and $I_C$ representing leaked and capacitor current respectively, how can it be shown that, given no current flow across the membrane, the voltage is directly proportional to the input current, $I_e$?

3. After obtaining the above expression, how can one re-express it in terms of change in voltage, $\frac{dV_m}{dt}$, given that $R_LC_m=\tau$, a time constant, and that the equilibrium voltage that occurs at no membrane current is defined as $V_\infin$?

4. Why are neurons generally low-pass filters? What does this mean?

### Leaky Capacitor with Battery

1. Why is the above model unable to accurately simulate a living neuron?

2. Why does combining Ohm's Law (electric current) and Fick's Law (flux) create an accurate representation of net current flow?

3. How can the Boltzmann equation, $\frac{P_{in}}{P_{out}}=e^{-\frac{U_{in}-U_{out}}{kT}}$, be used to derive the Nerst potential equation?

## Answers

### Simple Capacitor Model

1. A neuronal membrane consists of a phospholipid bilayer that separates two saline solutions, which is similar to two conductive plates separated by an insulator. It allows for charge to accumulate on both sides of the membrane.
   
2. Capacitative current is the flow of current through a capacitor due to repulsive forces across the insulator. The charge imbalance creates an electric field and potential difference.

3. $\Delta Q = C\Delta V$
   
   $\Delta V = \frac{\Delta Q}{C}$

   $\Delta V = \frac{1}{C}\int_0^t I_e(\tau)d\tau$

4. Increasing membrane surface area decreases the change in voltage due to increased capacitance.

### Leaky Capacitor Model

1. Neurons are 'leaky' due to ion channels in the membrane. This can be modeled by adding a resistor in parallel with the capacitor.

2. $I_L+I_C=I_e$
   
   $\frac{V_m}{R_L}+C_m\frac{dV_m}{dt}=I_e$

   $V_m+R_LC_m\frac{dV_m}{dt}=I_eR_L$

   $V_m=I_eR_L$

3. $V_m+\tau\frac{dV_m}{dt}=I_eR_L=V_\infin$
   
   $\frac{dV_m}{dt}=-\frac{1}{\tau}(V_m-V_\infin)$

4. The fact that a neuron is a low-pass filter means that it is more responsive to longer inputs. This is caused by the fact that an RC circuit integrates input while approaching a limit.

### Leaky Capacitor with Battery

1. Equilibrium potential difference is always zero volts due to the lack of a battery - all current is supplied by the researcher.

2. Since net current is affected both by diffusion due to concentration gradients and voltage due to 

3. $\frac{P_{in}}{P_{out}}=e^{-\frac{U_{in}-U_{out}}{kT}}$
   
   $\frac{P_{in}}{P_{out}}=e^{-\frac{q(V_{in}-V_{out})}{kT}}$

   $\Delta V = V_{in}-V_{out}=-\frac{kT}{q}ln(\frac{P_{in}}{P_{out}})$

   $\Delta V = 25mV\:ln(\frac{[K]_{out}}{[K]_{in}})$

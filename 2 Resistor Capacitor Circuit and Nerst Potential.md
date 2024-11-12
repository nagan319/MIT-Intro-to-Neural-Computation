## Learning Objectives

- Understand how neurons respond to injected currents
- Understand how membrane capacitance and resistance allows neurons to integrate or smooth their outputs over time (RC)
- How to derive the differential equations for the RC model
- Sketch the response of an RC neuron to different current inputs
- Understand where a neuron's 'batteries' come from

## Simple Capacitor Model

<b>Ion Channels</b>
- Functionality of ion channels is largely dependent on voltage
- Current is injected into the neuron and transformed into voltage change

<b>Response to injected current</b>
- Neurons perform analog numerical integratoin over time
$$V(t)=\int_0^t I(t)dt$$

<b>Why is a neuron a capacitor</b>?
- Saline solutions separated by phospholipid bilayer
- Similar to conductive plates separated by dielectric

<b>Capacitive Current</b>
- If positive charge is added to one plate of a capacitor, negative charge pushes positive charge out from its other plate
- An electric field is created due to charge imbalance, which creates a voltage difference

```charge --> imbalance --> field --> voltage```
 
Capacitance formula:
$$\Delta Q=C\Delta V$$
$$C=\frac{A}{L}$$

A lot of capacitance can be achieved due to thin, wide membrane

Capacitive current:
$$I_c(t)=\frac{dQ}{dt}=C\frac{dV_m}{dt}$$

Due to Kirchoff's current law, injected current must equal capacitive current: 
$$I_e(t)=C\frac{dV_m}{dt}$$

Integration:

$$V_m(t)=V_0+\frac{1}{C}\int_0^t I_e(\tau)d\tau$$

Note: $\tau$ is used for the time delta since $t$ is the final point

$$\Delta V=\frac{1}{C}\Delta Q$$

## Leaky Capacitor Model

Neurons are 'leaky' due to ion channels - this can be represented using a resistor

$$I_L+I_C=I_e$$

Total current goes into capacitor or leaks out

$$I_L+C\frac{dV}{dt}=I_e$$

- Membrane ionic current 
- Membrane capacitive current
- Electrode current

Convention: outward current is positive

Using Ohm's Law:
$$\frac{V_m}{R_L}+C\frac{dV_m}{dt}=I_e$$
$$V_m+R_LC\frac{dV_m}{dt}=R_LI_e$$

Under constant current (steady state):
$$V_m=R_LI_e$$

The voltage is called $V_\infin$, since it's the voltage that the system reaches  after an indefinite amount of time

$$V_m+\tau\frac{dV_m}{dt}=V_\infin$$ 
$$\tau=R_LC$$

Rewriting in the form of dV\dt:

$$\frac{dV}{dt}=-\frac{1}{\tau}(V-V_\infin)$$

<b>The voltage always approaches the equilibrium point</b>

The rate is proportional to how away the voltage is from equilibrium initially (exponential function)

General solution for differential equation:

$$V(t)-V_\infin=(V_0-V_\infin)e^\frac{-t}{\tau}$$

This applies only in the case of a constant $V_\infin$

$V_\infin\:\alpha\:I_e$, so it increases linearly with current input and drops back to zero in the case of no input current

$V_m$ approaches $V_\infin$ as specified in the differential equation

RC systems integrate up to a point but slow down as they approach equilibrium. They respond poorly to short inputs - <b>low-pass filter</b>

<b>Neuron Constants</b>

$R=10^8\Omega=100M\:\Omega$

$C=10^-10\:F$

$\tau = RC=10\:ms$

Neurons take 10-100ms to respond to input

Rewriting Ohm's Law using conductance:

$I_L=R_L^{-1}V=G_LV$

<b>Conductances in parallel and series</b>

$I_{net}=I_1+I_2$

$I_{net}=G_1V+G_2V$

Rewriting current using specific leak conductance $g$:

$I_L=Ag_LV_m$

<b>Capacitance in parallel</b>

$I_{net}=I_1+I_2$

$I_{net}=C_1\frac{dV}{dt}+C_2\frac{dV}{dt}$

Rewriting capacitance using specific capacitance $c_m$:

$C=c_mA$

$A=4\pi r^2$

<b>Rerwiting the time constant</b>

$\tau_m=R_L C=\frac{C}{G_L}=\frac{c_m A}{g_L A} = \frac{c_m}{g_L}$

Capacitance of unit area over conductance per unit area

<b>RC constant has nothing to do with the cell, only the membrane</b>

Different parts of the cell can have different time constants

## Adding a battery

The above model only works for dead neurons (no voltage at rest)

Ion channels can be represented by positive and negative battetries added in parallel to the circuit

Selective permeability allows for diffusion (flux) of one ion but not another

Only a little bit of ions flow, since the current flow due to difference in voltage ends up balancing the flux created due to the diffusion gradient

$$I_{net}=I_{drift}+I_{diffusion}$$

Ohm's Law and Fick's Law:

$$\frac{Aq^2\phi(x)D}{kT}\frac{\Delta V}{L}=AqD\frac{\delta\phi}{\delta x}$$

Nerst Equation:

$$\Delta V=\frac{kT}{q}ln(\frac{\phi_{out}}{\phi_{in}})$$

Deriving Nerst potential using the Boltzmann equation:

Boltzmann Probability Equation:

$$\frac{P_{state\:1}}{P_{state\:2}}=e^{-\frac{U_1-U_2}{kT}}$$

Probabilities of being in a certain state are exponentially related to the energy difference between those states

- If kT is zero, particles don't move
- As kT increases, and the difference decreases, e increases

$$\frac{P_{in}}{P_{out}}=e^{-\frac{U_{in}-U_{out}}{kT}}=e^{-\frac{q(V_{in}-V_{out})}{kT}}$$

$$V_{in}-V_{out}=-\frac{kT}{q}ln(\frac{P_{in}}{P_{out}})$$

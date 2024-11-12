## Continuing on the Hodgkin-Huxley Model

<b>Review:</b>

Perfect capacitor model:

$$V=\int_0^tI(\tau)d\tau$$

Leaky capacitor model:

$$I_{L}+I_{C}=I_e$$

$$\frac{V_m}{R_L}+C\frac{dV}{dt}=I_e$$

$$V_m+R_LC\frac{dV}{dt}=R_LI_e$$

$$V+\tau\frac{dV}{dt}=V_\infin$$

<b>Where do the batteries of a neuron come from?</b>

- Ion concentration gradients
- Ion-selective channels

Battery voltage is achieved by equilibrium through Nerst equation

## Nerst Potential for different ions

|Ion|Cytoplasm (mM)|Extracellular (mM)| Nerst (mV)|
|-|-|-|-|
|$K^+$|400|20|-75|
|$Na^+$|50|440|+55|
|$Cl^-$|52|560|-60|
|$Ca^{++}$|$10^{-4}$|2|+124

$$E_k=25mV[ln(\frac{20}{400})]=25mV(-3.00)=-75mV$$
$$E_{Na}=25mV[ln(\frac{440}{50})]=25mV(2.17)=55mV$$
$$E_{Cl}=-25mV[ln(\frac{560}{52})]=25mV(2.38)=-60mV$$
$$E_{Ca}=12.5mV[ln(\frac{2}{.0001})]=124mV$$

Note: Calcium is 12.5mV due to the +2 charge (two times less electric force required)

## I-V relation

The effect of input current on voltage is useful for studying ion channel functionality

Increasing current causes a linear increase in voltage; current reverses at Nerst potential (reversal potential)

$$I_K=G_K(V-E_K)$$

Can be described by a battery in series with a resistor:

$$V_m=E_k+\frac{I_K}{G_K}$$

<b>New Equation</b>:

$$V+\tau\frac{dV}{dt}=E_K+R_KI_e$$

Basically $V_\infin$ now includes current leaking through the membrane:

$$V+\tau\frac{dV}{dt}=V_\infin$$
$$V_\infin=E_K+R_KI_e$$

## Integrate and Fire Model

Action potentials make up a very small percent of the total time a neuron functions

<b>Model properties</b>: 
- A neuron spends most of its time integrating and only a bit firing
- All spikes are the same
- Spikes tend to occur when the voltage in a neuron reaches the <b>spike threshold</b>

Simplified model: Voltage is reset once the spike voltage is reached

<b>Simple example: No resistance</b>
- A neuron integrates linearly until it reaches the spike potential (sawtooth wave)

<img src='resources/lecture 3/integrate and fire no resistance.PNG' width=400>

$$f.r.=\frac{1}{\Delta t}$$

$$\Delta V = V_{threshold}-V_{rest}$$

$$C\frac{dV}{dt}=I_e$$

$$f.r=\frac{1}{\frac{C\Delta V}{I_e}}=(\frac{1}{C\Delta V})I_e$$

- If current increases, it creates the required potential difference faster
- If the capacitor is bigger, it takes longer to accumulate the required voltage
- If the required potential difference is bigger, it will take longer to happen

<b>With leak conductance</b>

<img src='resources/lecture 3/firing rate with resistance.PNG' width=400>

The voltage approaches $V_\infin$ according to the exponential function but drops to zero after reaching $V_{threshold}$

Many cells have a threshold current (rheobase) below which the cell does not spike. It can be calculated by setting $V_\infin=V_{threshold}$:

$$V_\infin=V_{threshold}$$

$$E_L+R_LI_e=V_{threshold}$$

$$I_{threshold}=I_e=G_L(V_{threshold}-E_L)$$

<b>Calculating firing rate</b>

$$V(t)-V_\infin=(V_0-V_\infin)e^\frac{-t}{\tau}$$

$$V_{threshold}-V_\infin=(V_{reset}-V_\infin)e^\frac{-\Delta t}{\tau}$$

Do some derivation here...

$$\Delta t = -\tau ln(\frac{V_\infin-V_{threshold}}{V_\infin-V_{reset}})$$

$$f = [\tau ln(\frac{V_\infin-V_{threshold}}{V_\infin-V_{reset}})]^{-1}$$

If input current and consequently $V_\infin$ is very large, the expression approaches 0

Basically, if the assumption is made that $ln(1+\alpha)=\alpha$, the following expression can be derived:

$$f=\frac{1}{C\Delta V}(I_e-I_{threshold})$$

## Replacing spike generator with ion channels

<img src='resources/lecture 3/HH model currents.PNG' width=400>

$$I_m=I_{Na}+I_{K}+I_{L}$$

$$I_m(t)=C\frac{dV(t)}{dt}=I_e(t)$$

Individual channel flows (no idea how this relates to the previous equations):

$$I_{Na}=G_{Na}(V, t)(V-E_{Na})$$

$$I_{K}=G_{K}(V, t)(V-E_{k})$$

$$I_{l}=G_{L}(V-E_L)$$

Where does time dependence and voltage dependence come from?



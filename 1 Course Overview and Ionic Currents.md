## Intro

<b>What is neural computation?</b>
- Brain/cogsci started as an extremely descriptive field
- Modern neural computation attempts to create engineering-level descriptions of neural systems
- New technologies have a allowed for monitoring thousands of neurons at a time
- <b>Neuropixels</b>: probes that can record thousands of neurons from different parts of the brain
- Comp neuro: taking data from neurons and making sense of it
- Same techniques can also be used in cogsci, medicine etc.

<img src='resources/lecture 1/what is neural computation.PNG'>

josh tennenbomb josh mcternit??

<b>Songbird example</b>
- Action potentials are recorded to see how bird learns from its parents
   
<b>Course goals</b>
- Understand basic biophysics of neurons and networks, brain and cognitive functions
- Use math to analyze neurons and networks + data sets
- Use MATLAB to implement these techniques

<img src='resources/lecture 1/lecture topics.PNG' width=400>

<i>Note: look at problem sets</i>

## A Mathematical Model of a Neuron

- A neuron can be modeled using an electrical circuit with defined mathematical properties
- Neurons have hundreds of different ion channels and are very complex
- Important to create models that allow for predicting changes due to varying ion channels and cell structures
- Neurons contain capacitors, power supplies, resistors etc.
- Intracellular/extracellular solution acts as a wire
 
## Solutions as wires

<img src='resources/lecture 1/basic electrochemistry.PNG' width=400>

- Salt solution with Na+ and Cl- ions
- 2 key mechanisms for inducing flow: diffusion and drift due to electric field

## Diffusion

<b>Thermal Energy</b>
- Every degree of freedom (particle motion) comes with a thermal energy proportional to a temperature

$$kT=E$$
- $k$ = Boltzmann constant
- $T$ = Temperature K
- $E$ = Kinetic energy

$$KE=\langle\frac{1}{2}mv^2_x\rangle=\frac{1}{2}kT$$

Due to equipartition of total thermal energy, $\frac{3}{2}kT$, along 3 axes

- Ions would have a very fast speed, but they collide with each other very frequently
- <b>Brownian motion</b> is the random motion of particles in a medium

<b>Spatial and temporal scales</b>
- An ion can diffuse across the soma of a neuron (10 um) in 50 ms
- Diffusing down a dendrite (1 mm) takes about 1 m
- Diffusing down a motor neuron axon (1m) takes 10 years

<img src='resources/lecture 1/diffusion various distances.PNG' width=300>

<b>Diffusion in 1D</b>
- Distribution follows Gaussian model
- There's a lot more ways for a particle to come back to where it started than to reach an end point
  
$$P(k;n,p)=\binom{n}{k}p^k(1-p)^{n-k}$$

$$\lim\limits_{np\to\infty}P(k;n,p)=\frac{1}{\sqrt{4\pi Dt}}e^{\frac{-x^2}{4Dt}}$$

<b>Random walk in one direction</b>
- N particles with position x=0 at time t=0
- $x_i(n)$ is the position of the ith particle at time n
- Assume each particle is independent
- $x_i(n)=x_i(n-1)\pm\delta$

Average position of all particles doesn't change:
$$\langle x_i(n)\rangle_i =\frac{1}{N}\sum_i x_i(n)$$

$$=\frac{1}{N}\sum_i [x_i(n-1)\pm\delta]$$

$$=\frac{1}{N}\sum_i [x_i(n-1)] + \frac{1}{N}\sum_i (\pm\delta)$$

$$=\frac{1}{N}\sum_i [x_i(n-1)]$$

$$\langle x_i(n)\rangle_i = \langle x_i(n-1)\rangle_i$$

The center of distribution remains the same
___
<b>Note: Definition and Computation of Variance</b>

$$s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}$$

Variance is the average distance of data points from the mean. It is the square of standard deviation.

___

The interesting part is calculating the total distance traveled (abs val) of the particles:

$$\langle |x(n)|\rangle$$

Abs val distance is a pain to deal with so use RMS instead:

$$\sqrt{\langle x^2(n)\rangle}$$

Compute variance:

$$\langle x^2(n) \rangle=\frac{1}{N}\sum_i x^2_i(n)$$

Use delta value:

$$x_i(n)=x_i(n-1)\pm \delta$$
$$x_i^2(n) = (x_i(n-1)\pm \delta)^2$$
$$x_i^2(n-1) \pm 2\delta x_i(n-1) + \delta^2$$

Plug in the crap:

$$\langle x^2(n)\rangle=\langle x^2(n-1)\rangle + \langle\pm2\delta x_i(n-1)\rangle + \langle\delta^2\rangle$$

$$\langle x^2(n)\rangle=\langle x^2(n-1)\rangle + \delta^2$$

<b>At each step, variance grows by a linear quantity</b>

$$\langle x^2(n)\rangle=n\delta^2$$

Some derivation...

$$D=\frac{\delta^2}{2\tau}$$

D is the diffusion coefficient (change in variance over time)

<b>Since standard deviation is the root of variance, the average distance a particle travels over time follows a sqrt function</b>

<b>Spatial and Temporal Scales</b>

Diffusion is fast at short length scales and slow at long length scales

Typical diffusion constant for small molecule: $~10^{-5}\:cm^2/s$

## Fick's First Law

- Diffusion produces a net flow of particles from regions of high concentration to regions of low concentration
- The flux of particles is proportional to the concentration gradient

Let $N(x)$ be the number of particles in a box a position $x$ and $N(x+\delta)$ the number of particles at position $x+\delta$

Due to random motion, half of the particles from the left will flow right, amounting to $\frac{1}{2}N(x)$, and half of the particles on the right will flow left, amounting to $\frac{1}{2}N(x+\delta)$

The net number of particles moving to the right at time $\tau$ is $\frac{1}{2}[N(x)-N(x+\delta)]$

Calculating flux (the rate at which particles move through a unit area):

$$J_x=-D\frac{1}{\delta}[\phi(x+\delta)-\phi(x)]$$

- $\phi$ represents the concentration at a given point
- $J_x$, flux, is proportional to the diffusion gradient times the difference in particle concentration at a point

$$J_x=-D\frac{\delta\phi}{\delta x}$$

Essentially, flux is proportional to the diffusion gradient and the change in concentration over distance

<b>Diffusion produces a net flux of particles down a gradient</b>

<img src='resources/lecture 1/net flux concentration gradient.PNG' width=400>

All concentration gradients go away

## Diffusion and Ohm's Law

$$I=\frac{\Delta V}{R}$$

<b>Origin of Ohm's Law</b>

Given 2 plates suspended in water with a potential difference V and a separation L,

$$E=\frac{\Delta V}{L}$$
$$F=qE$$

Particles still follow a random diffusion pattern but have a bit of acceleration in the direction of the electric field

The mean of the distribution shifts linearly in time - force produces constant velocity (not acceleration)

$$F=fv_d$$

This is just a result of viscous drag (friction)

Einstein-Smoluchovski relation:

$$f=\frac{kT}{D}$$

Deriving Ohm's Law:

$$I\:\alpha\:v_dA$$
$A$ = Area
$$I\:\alpha\:EA\:\alpha\:\frac{\Delta V}{L}A$$

Requires a constant: resistivity

$$I=(\frac{1}{\rho})\frac{\Delta V}{L}A$$

$$I=(\frac{A}{\rho L})\Delta V$$

$$R=\frac{\rho L}{A}$$

Resistance is proportional to resistivity and distance, decreases with increasing area

The resistivity of the brain is around a million times higher than copper

## Lecture 1 Quiz

### Thermal Energy, Variance, Diffusion Constant
1. In what cases can the Boltzmann constant, $k_B$, be applied?
   
2. How are thermal energy and temperature related?
   
3. What is the difference between the relationship across a single axis and when applied to 3D space?
   
4. How does average kinetic energy across a single axis relate to temperature?
   
5. What is the recursive definition of the location of a randomly-walking particle in a single dimension at a discrete time $n$, $\langle x(n)\rangle$?
   
6. How can the constancy of the average position of a 1D system of $N$ randomly walking particles be shown using this recursive definition?
   
7. What is the mathematical definition of variance? How does it relate to standard deviation, $s$?
   
8. What is the relationship between time and variance for a 1D system of randomly walking particles?
   
9.  How can this relationship be derived using the average of RMS distance traveled for particles, $\langle x^2(n)\rangle$?
    
10. What is the definiton of a diffusion constant?

11. How can a diffusion constant be derived from the above relationship, given that $\langle x^2(t)\rangle=2Dt$ (with t being equal to $n$ steps each of duration $\tau$)?

12. In the above formula, why is there a constant 2 in front of $D$?

### Fick's Law

1. Given a region $x$ with $N(x)$ particles and an adjacent region $x+\delta$ with $N(x+\delta)$ particles, what will be the particle flow from $x$ to $x+\delta$, given that $x+\delta$ is to the right of $x$?

2. What is the definition of flux in simple terms?

3. How can the answer from Question 1, with $\phi(x)$ used instead of $N(x)$ to represent particle density instead of amount, along with the diffusion gradient $D$ be used to define flux, $J_x$?

### Ohm's Law

1. Why does electron drift velocity increase linearly with force, as opposed to quadratically?

## Answers

### Thermal Energy, Variance, Diffusion Constant
1. The Boltzmann constant can be applied for particles in ideal conditions (high temperature, low pressure, small particle size).
   
2. Thermal energy is directly proportional to temperature.
   
3. Single axis: $E=\frac{1}{2}kT$, 3D space: $E=\frac{3}{2}kT$ due to equipartition theorem.

4. $\langle\frac{1}{2}mv_x^2\rangle=\frac{1}{2}kT$

5. $x(n)=x(n-1)\pm\delta$
  
6. $\langle x(n)\rangle=\langle x(n-1)\pm\delta \rangle$
   
   $\langle x(n)\rangle=\frac{1}{N}\sum_i[x_i(n-1)\pm \delta]$

   $\langle x(n)\rangle=\frac{1}{N}\sum_i[x_i(n-1)]+\frac{1}{N}\sum_i[\pm\delta]$

   $\langle x(n)\rangle=\frac{1}{N}\sum_i[x_i(n-1)]$

   $\langle x(n)\rangle=\langle x(n-1)\rangle$

7. $s^2=\frac{\sum_i(x_i-\bar{x})^2}{n-1}$
   
   Variance is equal to standard deviation squared.

8. Variance increases linearly with time.

9. $\langle x^2(n) \rangle = \frac{1}{N}\sum_ix_i^2(n)$
    
    $\langle x^2(n) \rangle = \frac{1}{N}\sum_i[x_i(n-1)\pm\delta]^2$

    $\langle x^2(n) \rangle = \frac{1}{N}\sum_i[x_i(n-1)^2\pm 2\delta x_i(n-1) + \delta^2]$

    $\langle x^2(n) \rangle = \frac{1}{N}\sum_i[x_i(n-1)^2] + \delta^2$

    $\langle x^2(n) \rangle = n\delta^2$

10. The change in variance over time for a system.

11. $\langle x^2(n)\rangle=n\delta^2$
    
    $\langle x^2(t)\rangle=\frac{t}{\tau}\delta^2$

    $2Dt=\frac{t}{\tau}\delta^2$

    $D=\frac{\delta^2}{2\tau}$

12. There are 2 possible directions of motion. In 3 dimensions, the constant would be 6. 

### Fick's Law

1. Flow from $x$ to $x+\delta$ = $\frac{1}{2}N(x)$
   
   Flow from $x+\delta$ to $x$ = $\frac{1}{2}N(x+\delta)$

   Net flow = $\frac{1}{2}[N(x) - N(x+\delta)]$

2. The rate at which particles move from one region to another.

3. The change in density between $x$ and $x+\delta$ can be defined as $\frac{\phi(x)-\phi(x+\delta)}{\delta}$
   
   Flux is proportional to both the difference in concentration and the diffusion gradient, so it is defined as $J_x=-\frac{D}{\delta}(\phi(x)-\phi(x+\delta))$. The negative sign simply reflects that flux always moves down the gradient. 

   In simpler terms, flux can be defined as $Jx=-D\frac{d\phi(x)}{dx}$

### Ohm's Law

1. Electron drift velocity increases linearly with applied force since their velocity is not constant and they experience frequent collisions.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from typing import List

def flow(amounts: List[int]):
    for i, amount in enumerate(amounts):
        if i != len(amounts) - 1:
            amounts[i+1] += amount / 2
            amounts[i] -= amount / 2
        if i != 0:
            amounts[i-1] += amount / 2
            amounts[i] -= amount / 2
    return amounts

n = 100
amounts = [500] + [0] * n + [500]

amount_histograms = []
flux_histograms = []

num_steps = 40
colormap = cm.plasma

for step in range(num_steps):
    amounts = flow(amounts)
    amount_histograms.append(list(amounts))
    flux = [amounts[i+1] - amounts[i] for i in range(len(amounts) - 1)]
    flux_histograms.append(flux)

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

for i, hist in enumerate(amount_histograms):
    color = colormap(i / num_steps)
    axs[0].bar(range(len(hist)), hist, width=1, alpha=0.7, color=color, label=f"Step {i+1}" if i % 10 == 0 else "")
axs[0].set_title("Particle Amounts Over Time")
axs[0].set_xlabel("State Position")
axs[0].set_ylabel("Number of Particles")
axs[0].grid(True)

for i, flux in enumerate(flux_histograms):
    color = colormap(i / num_steps)
    axs[1].bar(range(len(flux)), flux, width=1, alpha=0.7, color=color, label=f"Step {i+1}" if i % 10 == 0 else "")
axs[1].set_title("Particle Flux Over Time")
axs[1].set_xlabel("State Position")
axs[1].set_ylabel("Particle Flux")
axs[1].grid(True)

plt.tight_layout()
plt.savefig("flux_and_amount.png")
plt.close()

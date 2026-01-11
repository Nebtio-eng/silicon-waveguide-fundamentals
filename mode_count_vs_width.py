import matplotlib
matplotlib.use("Agg")

import meep as mp
import meep.mpb as mpb
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)

# Parameters
resolution = 32
waveguide_height = 0.22
widths = np.linspace(0.3, 0.9, 13)

si = mp.Medium(index=3.48)
sio2 = mp.Medium(index=1.44)

num_modes = []

for w in widths:
    geometry = [
        mp.Block(
            size=mp.Vector3(w, waveguide_height, mp.inf),
            center=mp.Vector3(),
            material=si
        )
    ]

    ms = mpb.ModeSolver(
        geometry_lattice=mp.Lattice(size=mp.Vector3(4, 4)),
        geometry=geometry,
        default_material=sio2,
        resolution=resolution,
        num_bands=4,   # ask for multiple modes
        k_points=[mp.Vector3(0, 0, 1)]
    )

    ms.run_te()
    freqs = ms.all_freqs[0]

    # Count guided modes (n_eff > n_clad)
    guided = 0
    for f in freqs:
        if f > 0:
            neff = 1 / f
            if neff > 1.44:  # oxide index
                guided += 1

    num_modes.append(guided)
    print(f"Width {w:.2f} µm → {guided} guided modes")

# Plot
plt.figure()
plt.plot(widths, num_modes, "o-")
plt.xlabel("Waveguide width (µm)")
plt.ylabel("Number of guided modes")
plt.title("Single-mode cutoff in SOI waveguide")
plt.grid(True)
plt.savefig("results/mode_count_vs_width.png", dpi=300)
plt.close()

print("\nSaved: results/mode_count_vs_width.png")

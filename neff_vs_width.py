# ============================================================
# Effective index vs waveguide width sweep (SOI)
# ============================================================

import matplotlib
matplotlib.use("Agg")  # WSL-safe

import meep as mp
import meep.mpb as mpb
import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# Create results folder
# -----------------------------
os.makedirs("results", exist_ok=True)

# -----------------------------
# Parameters
# -----------------------------
resolution = 32
waveguide_height = 0.22  # microns
widths = np.linspace(0.3, 0.8, 8)

# -----------------------------
# Materials
# -----------------------------
si = mp.Medium(index=3.48)
sio2 = mp.Medium(index=1.44)

# -----------------------------
# Storage
# -----------------------------
te_neff_list = []
tm_neff_list = []

# -----------------------------
# Sweep loop
# -----------------------------
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
        num_bands=1,
        k_points=[mp.Vector3(0, 0, 1)]
    )

    # TE mode
    ms.run_te()
    te_neff = 1 / ms.all_freqs[0][0]
    te_neff_list.append(te_neff)

    # TM mode
    ms.run_tm()
    tm_neff = 1 / ms.all_freqs[0][0]
    tm_neff_list.append(tm_neff)

    print(f"Width = {w:.2f} µm | TE n_eff = {te_neff:.3f} | TM n_eff = {tm_neff:.3f}")

# -----------------------------
# Plot
# -----------------------------
plt.figure()
plt.plot(widths, te_neff_list, "o-", label="TE")
plt.plot(widths, tm_neff_list, "s-", label="TM")
plt.xlabel("Waveguide width (µm)")
plt.ylabel("Effective index n_eff")
plt.title("Effective index vs waveguide width (SOI)")
plt.legend()
plt.grid(True)
plt.savefig("results/neff_vs_width.png", dpi=300)
plt.close()

print("\nPlot saved as results/neff_vs_width.png")

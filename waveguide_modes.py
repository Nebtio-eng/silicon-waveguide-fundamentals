# ============================================================
# Silicon SOI Waveguide — TE/TM Mode Solver (ROBUST VERSION)
# ============================================================

# --- Force non-GUI backend (fixes Qt / Wayland issues in WSL)
import matplotlib
matplotlib.use("Agg")

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
# Simulation parameters
# -----------------------------
resolution = 32
waveguide_width = 0.5    # microns
waveguide_height = 0.22  # microns

# -----------------------------
# Materials (SOI platform)
# -----------------------------
si = mp.Medium(index=3.48)
sio2 = mp.Medium(index=1.44)

# -----------------------------
# Geometry: Silicon waveguide
# -----------------------------
geometry = [
    mp.Block(
        size=mp.Vector3(waveguide_width, waveguide_height, mp.inf),
        center=mp.Vector3(),
        material=si
    )
]

# -----------------------------
# Lattice (2D cross-section)
# -----------------------------
geometry_lattice = mp.Lattice(size=mp.Vector3(4, 4))

# -----------------------------
# Mode Solver
# -----------------------------
ms = mpb.ModeSolver(
    geometry_lattice=geometry_lattice,
    geometry=geometry,
    default_material=sio2,
    resolution=resolution,
    num_bands=1,
    k_points=[mp.Vector3(0, 0, 1)]
)

# ============================================================
# TE MODE
# ============================================================
ms.run_te()

te_freq = ms.all_freqs[0][0]
te_neff = 1 / te_freq

# Get electric field
E_te = ms.get_efield(1)

# Robust field magnitude (always works)
E_te_mag = np.sqrt(np.sum(np.abs(E_te)**2, axis=0))
E_te_mag = np.squeeze(E_te_mag)

plt.figure()
plt.imshow(E_te_mag.T, origin="lower", cmap="inferno")
plt.colorbar(label="|E| (TE)")
plt.title(f"TE Mode | n_eff = {te_neff:.3f}")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("results/TE_mode.png", dpi=300)
plt.close()

# ============================================================
# TM MODE
# ============================================================
ms.run_tm()

tm_freq = ms.all_freqs[0][0]
tm_neff = 1 / tm_freq

# Get electric field
E_tm = ms.get_efield(1)

# Robust field magnitude
E_tm_mag = np.sqrt(np.sum(np.abs(E_tm)**2, axis=0))
E_tm_mag = np.squeeze(E_tm_mag)

plt.figure()
plt.imshow(E_tm_mag.T, origin="lower", cmap="inferno")
plt.colorbar(label="|E| (TM)")
plt.title(f"TM Mode | n_eff = {tm_neff:.3f}")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("results/TM_mode.png", dpi=300)
plt.close()

# ============================================================
# Print results
# ============================================================
print("====================================")
print("Silicon SOI Waveguide Results")
print("====================================")
print(f"Waveguide width  : {waveguide_width} µm")
print(f"Waveguide height : {waveguide_height} µm")
print("------------------------------------")
print(f"TE mode n_eff = {te_neff:.4f}")
print(f"TM mode n_eff = {tm_neff:.4f}")
print("====================================")
print("Field plots saved in ./results/")

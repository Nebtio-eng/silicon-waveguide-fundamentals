# ============================================================
# Waveguide Parameter Sweep (Data-Oriented, NO pandas)
# ============================================================

import matplotlib
matplotlib.use("Agg")

import meep as mp
import meep.mpb as mpb
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# -----------------------------
# Output directories
# -----------------------------
os.makedirs("results", exist_ok=True)

# -----------------------------
# Parameters
# -----------------------------
resolution = 32
waveguide_height = 0.22        # microns
widths = np.linspace(0.3, 0.9, 13)
wavelength = 1.55              # microns (telecom)

k_norm = 1.0
clad_index = 1.44

# -----------------------------
# Materials
# -----------------------------
si = mp.Medium(index=3.48)
sio2 = mp.Medium(index=clad_index)

# -----------------------------
# CSV file setup
# -----------------------------
csv_path = "results/neff_vs_width.csv"

with open(csv_path, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "width_um",
        "wavelength_um",
        "mode_id",
        "neff",
        "guided"
    ])

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
            num_bands=4,
            k_points=[mp.Vector3(0, 0, k_norm)]
        )

        ms.run_te()
        freqs = ms.all_freqs[0]

        for mode_id, fval in enumerate(freqs):
            if fval <= 0:
                continue

            neff = k_norm / fval
            guided = int(neff > clad_index)

            writer.writerow([
                round(w, 4),
                wavelength,
                mode_id,
                round(neff, 6),
                guided
            ])

        print(f"Processed width = {w:.2f} µm")

print("\nSaved:", csv_path)

# -----------------------------
# Quick plot (fundamental mode)
# -----------------------------
width_plot = []
neff_plot = []

with open(csv_path, mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["mode_id"]) == 0:
            width_plot.append(float(row["width_um"]))
            neff_plot.append(float(row["neff"]))

plt.figure()
plt.plot(width_plot, neff_plot, "o-")
plt.xlabel("Waveguide width (µm)")
plt.ylabel("Effective index n_eff")
plt.title("Effective index vs width (fundamental mode)")
plt.grid(True)
plt.savefig("results/neff_vs_width.png", dpi=300)
plt.close()

print("Saved: results/neff_vs_width.png")

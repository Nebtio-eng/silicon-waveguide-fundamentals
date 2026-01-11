# Silicon Waveguide Fundamentals (SOI)

This repository presents a systematic study of guided modes in a
Silicon-On-Insulator (SOI) waveguide using full-vector Maxwell eigenmode solvers
(MIT Meep and MPB).

The project focuses on understanding modal confinement, effective index,
single-mode conditions, and geometry-dependent dispersion, which form the
foundation of integrated silicon photonics design.

---

## Objectives

- Model an SOI strip waveguide using Maxwell’s equations
- Compute guided modes and effective index (n_eff)
- Visualize electromagnetic field confinement
- Study the dependence of n_eff on waveguide geometry
- Determine the single-mode cutoff condition

---

## Platform & Tools

- Ubuntu (WSL2)
- Python 3.10
- MIT Meep (pymeep)
- MIT MPB (eigenmode solver)
- NumPy, Matplotlib
- Git & GitHub for version control

---

## Project Structure



---

## Results

### 1. Guided Mode Profiles

The fundamental guided mode is strongly confined within the silicon core due to
the high refractive index contrast between silicon (n ≈ 3.48) and oxide cladding
(n ≈ 1.44).  
Field magnitude plots are used to robustly visualize confinement.

---

### 2. Effective Index vs Waveguide Width

The effective index increases monotonically with waveguide width, indicating
stronger modal confinement for wider waveguides.

This geometry-dependent behavior directly impacts phase accumulation, dispersion,
and device performance in integrated photonic circuits.

> Note: In the 2D approximation used here, TE and TM polarizations exhibit
> identical effective indices due to structural symmetry and scalar polarization
> treatment.

---

### 3. Single-Mode Cutoff Analysis

By computing multiple eigenmodes and sweeping waveguide width, the number of
guided modes was determined as a function of geometry.

- Narrow waveguides support only the fundamental mode
- Higher-order modes appear beyond a critical width
- This transition defines the **single-mode cutoff condition**

The results explain why silicon photonic platforms commonly use waveguide widths
around 450–500 nm for single-mode operation at telecom wavelengths.

---

## Key Takeaways

- Modal behavior in SOI waveguides is governed by geometry and index contrast
- Single-mode operation is essential for stable and predictable photonic devices
- Eigenmode solvers provide quantitative design insight beyond ray optics
- Geometry sweeps are a core tool in photonic integrated circuit design

---

## Applications

- Silicon photonic integrated circuits (PICs)
- Ring resonators
- Mach–Zehnder interferometers
- Optical modulators and filters

---

## Author

**Nebtio**  
Integrated Photonics & Optical Technologies  

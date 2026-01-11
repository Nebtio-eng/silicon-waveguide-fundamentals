# Silicon Waveguide Fundamentals (SOI)

This project studies guided modes in a Silicon-On-Insulator (SOI) waveguide using
MIT Meep and MPB eigenmode solvers.

## Objectives
- Understand guided modes in high-index-contrast waveguides
- Compute effective index (n_eff)
- Study dependence of n_eff on waveguide geometry
- Visualize electromagnetic mode profiles

## Platform
- Ubuntu (WSL2)
- Python 3.10
- Meep + MPB

## Results

### Guided Mode Profiles
The fundamental guided mode is well confined inside the silicon core,
demonstrating strong index contrast between silicon and oxide cladding.

### Effective Index vs Width
The effective index increases with waveguide width, indicating stronger
modal confinement.  
In the 2D approximation used here, TE and TM polarizations show identical
effective indices due to structural symmetry.

## Applications
- Silicon photonic integrated circuits
- Ring resonators
- Mach–Zehnder interferometers
- Optical modulators

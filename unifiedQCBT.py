import numpy as np
import matplotlib.pyplot as plt

# --- Fundamental Constants (SI Units) ---
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
G = 6.67430e-11       # Gravitational constant (N·m²/kg²)
c = 2.99792458e8      # Speed of light (m/s)
m0 = 1.67e-27         # Characteristic mass (Nucleon mass, kg)

# --- Define Objects and Masses (Total Mass in kg) ---
objects = {
    "Electron": 9.11e-31,
    "Proton": 1.67e-27,
    "Neutron": 1.67e-27,
    "Pluto": 1.46e22,
    "Earth": 5.97e24,
    "Jupiter": 1.90e27,
    "Sun": 1.99e30,
    "Black Hole": 1.0e31 # Approx. 5 Solar Masses
}

names = list(objects.keys())
masses = np.array(list(objects.values()))

# --- QCBT™ / Objective Collapse Formulas ---

# 1. Collapse Rate (lambda): Scales with the square of the mass ratio (N^2)
# λ(M) ~ λ₀ * (M / m0)²
lambda_base = (G**2 * m0**5 * c) / (hbar**3) # Fundamental collapse rate (~1e-16 s^-1)
lambda_M = lambda_base * (masses / m0)**2

# 2. Compton Wavelength (λ_C): Scales inversely with mass (1/M)
# This represents the characteristic quantum length and is inversely proportional to energy (E=Mc²)
lambda_C = hbar / (masses * c)

# --- Plotting the QCBT™ Transition ---

fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.set_xscale('log')

# --- Axis 1: Collapse Rate (RED, Right Axis) ---
ax1.plot(masses, lambda_M, 'r-', linewidth=2, label=r'QCBT Collapse Rate, $\lambda \propto M^2$')
ax1.set_yscale('log')
ax1.set_xlabel('Object Mass, $M$ (kg)', fontsize=14)
ax1.set_ylabel(r'QCBT Collapse Rate, $\lambda$ ($\text{s}^{-1}$)', color='red', fontsize=14)
ax1.tick_params(axis='y', labelcolor='red')

# --- Axis 2: Compton Wavelength/Energy (BLUE, Left Axis) ---
ax2 = ax1.twinx()
ax2.plot(masses, lambda_C, 'b--', linewidth=2, label=r'Compton Wavelength, $\lambda_C \propto 1/M$')
ax2.set_yscale('log')
ax2.set_ylabel(r'Quantum Length Scale, $\lambda_C$ (m)', color='blue', fontsize=14)
ax2.tick_params(axis='y', labelcolor='blue')

# --- Annotate the data points (on the lambda curve) ---
# Define annotation positions and offsets
annotation_positions = {
    "Electron": (-50, -50),
    "Proton": (50, 50),
    "Neutron": (-50, 50),
    "Pluto": (30, 30),
    "Earth": (-30, -30),
    "Jupiter": (30, -30),
    "Sun": (-30, 30),
    "Black Hole": (30, 30)
}

for i, name in enumerate(names):
    ax1.plot(masses[i], lambda_M[i], 'ro', markersize=7)
    
    # Add labels with arrows (annotate)
    ax1.annotate(
        name,
        xy=(masses[i], lambda_M[i]),  # Point to annotate
        xytext=annotation_positions[name],  # Offset from point
        textcoords='offset points',  # Offset units
        fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.7),  # Add white background to text
        arrowprops=dict(
            arrowstyle='->',
            connectionstyle='arc3,rad=0.2',
            alpha=0.7
        )
    )

# --- Final Adjustments ---
ax1.grid(True, which="both", ls="--", alpha=0.6)
plt.title(r'QCBT™ Unified Bridge: Collapse Rate ($\lambda$) and Energy Scale ($\lambda_C$) vs. Mass', fontsize=16, pad=20)

# Adjust the layout to make room for the legend
plt.subplots_adjust(right=0.85)  # Make room on the right for the legend

# Place legend outside the plot on the right
fig.legend(loc='center right', bbox_to_anchor=(0.98, 0.5), bbox_transform=ax1.transAxes)
plt.show()

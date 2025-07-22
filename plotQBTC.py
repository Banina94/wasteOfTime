import numpy as np
import matplotlib.pyplot as plt

# --- Constants ---
# Planck mass (kg)
m_P = 2.18e-8  # kg (approx. 2.176 x 10^-8 kg)

# Speed of light (m/s)
c = 2.998e8  # m/s

# Characteristic quantum energy scale (Joule)
# 1 eV = 1.602e-19 J
E_QM = 1.0 * 1.602e-19  # J (1 eV)

# Exponent for lambda(M)
alpha = 1

# --- Mass Range ---
# Minimum mass (approx. electron mass scale)
# m_electron = 9.109e-31 kg
min_mass = 1e-30 # kg

# Maximum mass (approx. supermassive black hole mass scale, 10^5 Solar Masses)
# M_sun = 1.989e30 kg
max_mass = 1e31 # kg (roughly 5000 solar masses, well into black hole regime)

# Generate a logarithmically spaced array of masses
# We'll use 1000 points for a smooth curve
masses = np.logspace(np.log10(min_mass), np.log10(max_mass), 1000)

# --- Calculations ---

# 1. Compute lambda(M)
lambda_M = (m_P / masses)**alpha

# 2. Compute fractional energy correction (E/Mc^2 - 1)
# E_correction = lambda_M * (E_QM / (masses * c**2))

# Full expression for E/Mc^2
# E = M c^2 * [1 + lambda(M) * (E_QM / (M c^2))]
# So, E / (M c^2) = 1 + lambda(M) * (E_QM / (M c^2))
fractional_energy_deviation = lambda_M * (E_QM / (masses * c**2))
total_relative_energy = 1 + fractional_energy_deviation

# --- Plotting ---

plt.figure(figsize=(10, 7))

# Plot E/Mc^2 vs. Mass
plt.loglog(masses, total_relative_energy, label=r'$\frac{E}{Mc^2} = 1 + \left(\frac{m_P}{M}\right)^\alpha \frac{E_{QM}}{Mc^2}$')

# Add a horizontal line at y=1 for the classical limit
plt.axhline(y=1, color='gray', linestyle='--', label='Classical Limit ($E/Mc^2 = 1$)')

# --- Annotations and Labels ---
plt.xlabel('Mass M (kg)', fontsize=14)
plt.ylabel(r'Fractional Energy $\frac{E}{Mc^2}$', fontsize=14)
plt.title(f'Quantum Corrections Across Mass Scales (QCBT™)\n'
          f'($m_P = {m_P:.2e}$ kg, $\\alpha = {alpha}$, $E_{{QM}} = {E_QM/1.602e-19:.0f}$ eV)', fontsize=16)
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend(fontsize=12)

# Customizing ticks for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add annotations for key mass scales
plt.text(masses[0] * 1.5, total_relative_energy[0] * 1.5, 'Quantum Dominant',
         verticalalignment='bottom', horizontalalignment='left', color='blue', fontsize=10, weight='bold')
plt.text(m_P * 10**(-0.5), 1.01, 'Crossover Region',
         verticalalignment='bottom', horizontalalignment='left', color='purple', fontsize=10, weight='bold')
plt.text(masses[-1] * 0.5, 1.000001, 'Classical Dominant',
         verticalalignment='bottom', horizontalalignment='right', color='green', fontsize=10, weight='bold')


# Optional: Add vertical line at Planck mass for visual reference
plt.axvline(x=m_P, color='red', linestyle=':', linewidth=1.5, label=f'Planck Mass ($m_P = {m_P:.2e}$ kg)')

# Add an inset for the deviation to show it more clearly at larger masses
ax_inset = plt.axes([0.6, 0.6, 0.28, 0.28]) # [left, bottom, width, height]
plt.loglog(masses, fractional_energy_deviation, color='orange')
plt.title('Fractional Deviation', fontsize=10)
plt.xlabel('Mass (kg)', fontsize=8)
plt.ylabel(r'$\frac{E}{Mc^2} - 1$', fontsize=8)
plt.grid(True, which="both", ls="-", alpha=0.2)
ax_inset.tick_params(axis='both', which='major', labelsize=7)
ax_inset.tick_params(axis='both', which='minor', labelsize=5)


plt.tight_layout(rect=[0, 0, 1, 0.95]) # Adjust layout to prevent title overlap
plt.show()

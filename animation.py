import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
hbar = 1.0545718e-34  # J·s
c = 299792458         # m/s
E = 8.1871e-14        # Joules (electron rest energy)
k = 1e10              # wave number
omega = E / hbar      # angular frequency
gamma0 = 1            # simplified gamma matrix
mass_einstein = E / c**2  # Constant

# Spacetime grid
x = np.linspace(-1e-9, 1e-9, 1000)  # Position in meters
times = np.linspace(0, 5e-18, 100)  # Time in seconds

# Create figure for animation
fig, ax = plt.subplots(figsize=(12, 6))
line1, = ax.plot([], [], label="Schrödinger", color='blue')
line2, = ax.plot([], [], label="Klein-Gordon", color='green')
line3, = ax.plot([], [], label="Dirac (formal)", color='red')
line4, = ax.plot([], [], label="Einstein (constant)", color='black')
ax.set_xlim(x[0]*1e9, x[-1]*1e9)
ax.set_ylim(8.5e-31, 9.5e-31)
ax.set_xlabel("Position (nm)")
ax.set_ylabel("Mass (kg)")
ax.set_title("Time Evolution of Mass Expressions with Spacetime Curvature")
ax.legend()
ax.grid(True)

# Simulate spacetime curvature as a sinusoidal perturbation in wave vector
def curvature_factor(x, t):
    return 1 + 0.05 * np.sin(2 * np.pi * 1e9 * x) * np.cos(2 * np.pi * 2e17 * t)

# Animation update function
def update(frame):
    t = times[frame]
    k_curved = k * curvature_factor(x, t)
    omega_curved = omega * curvature_factor(x, t)
    Psi = np.exp(1j * (k_curved * x - omega_curved * t))

    dPsi_dt = -1j * omega_curved * Psi
    laplacian_Psi = -k_curved**2 * Psi
    mass_schrodinger = - (hbar / (2j)) * (laplacian_Psi / (Psi * dPsi_dt)).real

    box_Psi = (-omega_curved**2 / c**2 + k_curved**2) * Psi
    mass_kg = (hbar / c) * np.sqrt(np.abs(-box_Psi.real / Psi.real))

    dPsi_dx = 1j * k_curved * Psi
    dirac_mass = (1j * hbar / c) * ((gamma0 * dPsi_dx) / Psi).real

    line1.set_data(x * 1e9, mass_schrodinger)
    line2.set_data(x * 1e9, mass_kg)
    line3.set_data(x * 1e9, dirac_mass)
    line4.set_data(x * 1e9, [mass_einstein] * len(x))
    return line1, line2, line3, line4

# Animate
ani = animation.FuncAnimation(fig, update, frames=len(times), blit=True, interval=100)
plt.close()
ani

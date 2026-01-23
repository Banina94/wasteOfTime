import numpy as np
import matplotlib.pyplot as plt

# --- IMPORTANT DISCLAIMERS (READ CAREFULLY) ---
print("--------------------------------------------------------------------------------------------------------------------")
print("WARNING: This script graphs an equation explicitly stated in your provided document as having NO PHYSICAL MEANING.")
print("It is NOT a physically derived law and cannot predict real-world phenomena.")
print("Arbitrary mathematical assumptions have been made for undefined variables (Wavefunction, Potential, Abstract Parameter)")
print("to make graphing possible. The resulting graph is a purely mathematical illustration.")
print("--------------------------------------------------------------------------------------------------------------------")

# --- 1. Define Physical Constants (Standard SI Units) ---
c = 2.99792458e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (Joule-seconds)
M_proton = 1.67262192e-27  # Rest mass of a proton (kg)

# --- 2. Define Abstract Parameters (Arbitrary Values for Illustration) ---
# As per your document, these have no inherent physical meaning here.
Lambda = 1.0  # Arbitrary value for the Abstract Scale Parameter

# Parameters for the arbitrary complex exponential wavefunction Psi(x, t) = A * exp(i * (k0 * x - omega0 * t))
A_psi = 1.0       # Amplitude of Psi (arbitrary)
k0 = 1.0e10       # Arbitrary 'wave number' (m^-1), chosen to show some oscillation over a small range
omega0 = 1.0e15   # Arbitrary 'angular frequency' (rad/s), chosen to show some oscillation

# --- 3. Define the Abstract Wavefunction and Potential (Arbitrary Forms) ---
def psi_function(x, t):
    """
    Arbitrary complex exponential wavefunction for demonstration.
    This does NOT represent a real proton wavefunction.
    """
    return A_psi * np.exp(1j * (k0 * x - omega0 * t))

def potential_energy(x, t):
    """
    Arbitrary potential energy function (set to zero for simplicity).
    This does NOT represent a real potential for a proton.
    """
    return 0.0 # Assuming V(x,t) = 0 for simplicity

# --- 4. Define the Energy Equation Function ---
def calculate_energy(x, t, M_input, Lambda, k0, omega0):
    """
    Calculates the value of the abstract energy equation.
    Uses simplified forms for Psi and V, and takes arbitrary Lambda.
    """
    psi = psi_function(x, t)

    # Calculate derivatives of Psi assuming psi_function is A * exp(i * (k0 * x - omega0 * t))
    # d/dt Psi = -i * omega0 * Psi
    dt_psi = -1j * omega0 * psi

    # d^2/dx^2 Psi = -(k0)^2 * Psi  (assuming d_2x d_2x means d^2/dx^2 in 1D)
    d2x_d2x_psi = -(k0**2) * psi

    V = potential_energy(x, t)

    # First term: c^2 * E_Minput * (1 + exp(Lambda))
    # E_Minput is simply the M_input (proton mass) as it's the "Generalized Mass Input"
    term1 = c**2 * M_input * (1 + np.exp(Lambda))

    # Second term: 2 * (i*hbar*dt_psi - V*Psi - hbar^2*d2x_d2x_psi)
    term2 = 2 * (1j * hbar * dt_psi - V * psi - hbar**2 * d2x_d2x_psi)

    # Total Energy
    E = term1 - term2
    return E

# --- 5. Generate Data for Plotting ---
x_values = np.linspace(-1e-10, 1e-10, 500) # A very small range for x, suitable for quantum-like scales
fixed_t = 0.0 # Fix time at t=0 for a 2D graph

# Calculate Energy values
E_values = np.array([calculate_energy(x, fixed_t, M_proton, Lambda, k0, omega0) for x in x_values])

# Extract Real, Imaginary, and Magnitude for plotting
E_real = np.real(E_values)
E_imag = np.imag(E_values)
E_magnitude = np.abs(E_values)

# --- 6. Plotting the Results ---
plt.figure(figsize=(12, 8))

plt.plot(x_values, E_real, label='Real Part of Abstract Energy $E$', color='blue')
plt.plot(x_values, E_imag, label='Imaginary Part of Abstract Energy $E$', color='red', linestyle='--')
plt.plot(x_values, E_magnitude, label='Magnitude of Abstract Energy $E$', color='green', linestyle=':', linewidth=2)

plt.xlabel('Abstract Spatial Variable x (m)', fontsize=12)
plt.ylabel('Abstract Energy E (J)', fontsize=12)
plt.title('Mathematical Illustration of Abstract Energy Equation (Proton Minput)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.axhline(0, color='gray', linestyle='-', linewidth=0.5) # Add x-axis line
plt.axvline(0, color='gray', linestyle='-', linewidth=0.5) # Add y-axis line
plt.tight_layout()
plt.show()

print("\n--- Plotting Complete ---")
print("Remember: This plot is a purely mathematical visualization of an abstract equation,")
print("not a representation of physical reality for a proton or anything else.")
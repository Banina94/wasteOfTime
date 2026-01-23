import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer # <<<-- THIS IS THE CHANGE
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# --- 1. Abstract Energy Calculation (from previous script) ---
# IMPORTANT: This part is purely classical and abstract, no physical meaning.
c = 2.99792458e8
hbar = 1.054571817e-34
M_input_val = 1.67262192e-27 # Proton mass for Minput
Lambda_val = 1.0
A_psi_val = 1.0
k0_val = 1.0e10
omega0_val = 1.0e15

def psi_function(x, t):
    return A_psi_val * np.exp(1j * (k0_val * x - omega0_val * t))

def potential_energy(x, t):
    return 0.0

def calculate_abstract_energy(x, t, M_input, Lambda, k0, omega0):
    psi = psi_function(x, t)
    dt_psi = -1j * omega0 * psi
    d2x_d2x_psi = -(k0**2) * psi
    V = potential_energy(x, t)

    term1 = c**2 * M_input * (1 + np.exp(Lambda))
    term2 = 2 * (1j * hbar * dt_psi - V * psi - hbar**2 * d2x_d2x_psi)
    E = term1 - term2
    return E

# --- 2. Choose Arbitrary Input for Abstract Energy Calculation ---
arbitrary_x = 0.0 # Just pick a point
arbitrary_t = 0.0 # And a time

# Classically calculate the abstract energy
abstract_E = calculate_abstract_energy(arbitrary_x, arbitrary_t, M_input_val, Lambda_val, k0_val, omega0_val)
abstract_E_magnitude = np.abs(abstract_E)

# Normalize/scale the magnitude to be a valid rotation angle (0 to 2*pi)
# This mapping is COMPLETELY ARBITRARY for "shits and giggles"
scaling_factor = 1e-10 # Adjust this to get a reasonable angle
rotation_angle = (abstract_E_magnitude * scaling_factor) % (2 * np.pi)

print(f"Abstract Energy Magnitude: {abstract_E_magnitude:.2e} J (Purely abstract)")
print(f"Arbitrary Rotation Angle derived from it: {rotation_angle:.4f} radians ({np.degrees(rotation_angle):.2f} degrees)")

# --- 3. Quantum Circuit Construction (Using Qiskit) ---
# This part uses quantum mechanics, but its input is from the abstract calculation.
qc = QuantumCircuit(1, 1) # 1 qubit, 1 classical bit

qc.h(0) # Apply Hadamard gate to put qubit into superposition

# Apply a Z-axis rotation (Rz gate) with the arbitrary angle derived from Abstract Energy
qc.rz(rotation_angle, 0)

qc.h(0) # Apply another Hadamard to measure in X-basis to see effect of phase

qc.measure(0, 0) # Measure the qubit

# --- 4. Simulation and Visualization ---
simulator = Aer.get_backend('qasm_simulator') # Corrected import used here
job = simulator.run(transpile(qc, simulator), shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("\n--- Quantum Circuit Results (Purely Illustrative) ---")
print(f"Measurement Counts: {counts}")
plot_histogram(counts, title="Measurement Results from 'Abstract Energy' Driven Phase").show()

print("\n--- Circuit Drawing ---")
print(qc.draw(output='text'))
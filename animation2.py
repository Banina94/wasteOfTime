import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define the abstract functions ---
# Abstract Relativistic Mass function
# Here, we've simplified the constants (A/C^2) to 1 for illustration
def abstract_relativistic_mass(x):
    """
    Represents an abstract relativistic mass function, simplified to x^2.
    """
    return x**2

# Abstract Quantum Mass function
# Here, we've simplified the constant (B) to 1 for illustration
def abstract_quantum_mass(x):
    """
    Represents an abstract quantum mass function, simplified to x.
    """
    return x

# --- 2. Define the range for the abstract variable x ---
# We choose a range that clearly shows the intersection points
x_values = np.linspace(-1.5, 2.5, 400) # From -1.5 to 2.5 with 400 points for smoothness

# --- 3. Calculate the corresponding mass values ---
m_R_values = abstract_relativistic_mass(x_values)
m_Q_values = abstract_quantum_mass(x_values)

# --- 4. Identify the intersection points mathematically ---
# We know from solving x^2 = x that intersections occur at x=0 and x=1
intersection_x = [0, 1]
intersection_y = [0, 1] # At x=0, y=0. At x=1, y=1.

# --- 5. Plotting ---
plt.figure(figsize=(10, 7)) # Set the figure size for better readability

# Plot the abstract relativistic mass function
plt.plot(x_values, m_R_values, label=r'Abstract $M_{Rel}(x) = x^2$', color='blue', linewidth=2, linestyle='-')

# Plot the abstract quantum mass function
plt.plot(x_values, m_Q_values, label=r'Abstract $M_{QM}(x) = x$', color='red', linewidth=2, linestyle='--')

# Plot the intersection points
plt.scatter(intersection_x, intersection_y, color='purple', s=100, zorder=5,
            label='Intersection Points', edgecolors='black')

# --- 6. Add labels, title, grid, and legend ---
plt.xlabel('Abstract Variable x', fontsize=14)
plt.ylabel('Abstract Mass m', fontsize=14)
plt.title('Mathematical Intersection of Abstract Mass Functions', fontsize=16)
plt.grid(True, linestyle='-', alpha=0.7)

# Adjust plot limits for better visualization
plt.xlim(-1.5, 2.5)
plt.ylim(-0.5, 3.5)

# Add vertical and horizontal lines for visual aid at intersections
plt.axvline(0, color='gray', linestyle=':', linewidth=0.7) # Vertical line at x=0 for visual aid
plt.axhline(0, color='gray', linestyle=':', linewidth=0.7) # Horizontal line at y=0 for visual aid
plt.axvline(1, color='gray', linestyle=':', linewidth=0.7) # Vertical line at x=1 for visual aid
plt.axhline(1, color='gray', linestyle=':', linewidth=0.7) # Horizontal line at y=1 for visual aid

plt.legend(fontsize=12)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show() # This displays the plot

# Print the intersection points to the console
print(f"Intersection Point 1: (x={intersection_x[0]}, m={intersection_y[0]})")
print(f"Intersection Point 2: (x={intersection_x[1]}, m={intersection_y[1]})")
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Set the default renderer to 'browser' to force opening in a new tab
pio.renderers.default = "browser"

# --- ABSOLUTELY ARBITRARY MATHEMATICAL ASSUMPTIONS (NO PHYSICAL BASIS) ---
# These values and functions are chosen purely to allow numerical computation
# and plotting of the abstract formula. They have NO connection to physics.

# 1. Fundamental Constants (Numerical values used, but roles are purely mathematical)
c = 3e8  # Speed of light (m/s)
hbar = 1.054e-34 # Reduced Planck's constant (J*s)

# 2. Lambda (Abstract Scale Parameter)
# Chosen to be very small to prevent numerical overflow for large masses in np.exp()
lam = 1e-36

# 3. Arbitrary Constants for Proxy Functions
psi_constant = 1e-10 # Arbitrary constant for the 'abstract_psi' function
v_constant = 1e-5    # Arbitrary constant for the 'abstract_v' function

# 4. Arbitrary Scaling Factors for the Quantum Influence Term (Y-axis proxy)
# Used to combine psi_val and v_val into a single number for the Y-axis.
q_factor1 = 1e10
q_factor2 = 1e-15

# 5. Abstract Proxy Functions for Psi and V (NOT real wavefunctions/potentials)
# These functions yield a single numerical value based on mass, x_val, and t_val.
def abstract_psi_proxy(mass, x_val, t_val):
    # Designed to prevent division by zero if x_val or t_val are 0.
    # We enforce x_val and t_val to be positive in the meshgrid for this plot.
    # Resulting value is just an arbitrary number, not a physical wavefunction value.
    return psi_constant / (mass * (x_val + 1) * (t_val + 1))

def abstract_v_proxy(mass, x_val, t_val):
    # Resulting value is just an arbitrary number, not a physical potential value.
    return v_constant * mass * x_val * t_val

# 6. Abstract Quantum Influence Term (This will be used internally for the energy exponent)
# This is an arbitrary linear combination of abstract_psi_proxy and abstract_v_proxy.
# It completely ignores derivatives and complex numbers, taking only the real part.
def calculate_abstract_quantum_influence(mass_input, x_proxy, t_proxy):
    psi_val = abstract_psi_proxy(mass_input, x_proxy, t_proxy)
    v_val = abstract_v_proxy(mass_input, x_proxy, t_proxy)
    return np.real(q_factor1 * psi_val - q_factor2 * v_val)

# 7. Final Abstract Energy Calculation (Z-axis for the plot)
# Implements the given abstract energy equation using all the proxy values.
def calculate_abstract_energy(mass_input, x_proxy, t_proxy, c_val, lambda_val):
    try:
        # Calculate the arbitrary quantum influence term for the exponent
        abstract_quantum_term_for_exponent = calculate_abstract_quantum_influence(mass_input, x_proxy, t_proxy)

        # First part of the energy equation: c^2 * e^(lambda * M_input)
        term_exp_mass = np.exp(lambda_val * mass_input)

        # Second part of the energy equation: (1 + e^lambda)^(-AbstractQuantumTerm)
        term_exp_lambda_base = (1 + np.exp(lambda_val))
        
        # Clip the exponent to prevent extreme values leading to inf/0 in power
        # These values are empirical to stay within float limits for typical calculations
        exponent_clip_max = 700
        exponent_clip_min = -700 
        clipped_abstract_quantum_term = np.clip(abstract_quantum_term_for_exponent, exponent_clip_min, exponent_clip_max)

        term_exp_lambda = term_exp_lambda_base**(-clipped_abstract_quantum_term)

        energy = c_val**2 * term_exp_mass * term_exp_lambda
        
        # Return NaN if the final energy value is not finite
        if not np.isfinite(energy):
            return np.nan
        
        return energy
    except OverflowError:
        return float('inf') # Still catch, though clipping should reduce
    except Exception as e:
        # print(f"Error calculating energy for mass {mass_input:.2e}, x {x_proxy:.2e}, t {t_proxy:.2e}: {e}") # Uncomment for debug
        return np.nan # Return NaN for other errors

# --- DATA FOR PLOTTING (OBJECTS AND THEIR ARBITRARY PROXY VALUES) ---
# We now only care about the mass for each object for this type of plot.
objects_data = {
    "Electron": {"mass": 9.109e-31},
    "Proton": {"mass": 1.672e-27},
    "Neutron": {"mass": 1.675e-27},
    "Pluto": {"mass": 1.309e22},
    "Earth": {"mass": 5.972e24},
    "Jupiter": {"mass": 1.898e27},
    "Sun": {"mass": 1.989e30},
    "Black Hole (5 Solar Masses)": {"mass": 1.0e31}
}

# Convert to DataFrame for easier handling of names and masses
df_objects_info = pd.DataFrame([{'Object': name, 'Mass': data['mass']} for name, data in objects_data.items()])

# --- USER INTERFACE (Selection for Mass for Surface Plot) ---
print("Select ONE object whose mass will be used for the Abstract Energy Surface Plot:")
print("Invalid input or no selection will result in no plot.")
for i, label in enumerate(df_objects_info['Object']):
    print(f"{i+1}. {label}")

selected_mass_index = -1
user_input_mass = input("Your choice (enter number): ").strip()

if user_input_mass:
    try:
        idx = int(user_input_mass) - 1
        if 0 <= idx < len(df_objects_info):
            selected_mass_index = idx
        else:
            print(f"Warning: Option {idx+1} is out of range.")
    except ValueError:
        print("Invalid input. No plot will be generated.")
else:
    print("No input provided. No plot will be generated.")

if selected_mass_index != -1:
    selected_object_name = df_objects_info.iloc[selected_mass_index]['Object']
    selected_mass_for_plot = df_objects_info.iloc[selected_mass_index]['Mass']
    print(f"\nGenerating surface plot for selected mass: {selected_object_name} (Mass: {selected_mass_for_plot:.2e} kg)")

    # --- Define ranges for Abstract X-Proxy and T-Proxy for the surface ---
    # Using log space to cover many orders of magnitude abstractly.
    # Adjust num_points to control the smoothness/resolution of the surface.
    num_points = 50 # Number of points in each dimension for the grid

    # X-proxy values (abstract space dimension)
    x_proxy_min = 1e-10 # From very small to very large (arbitrary units)
    x_proxy_max = 1e10
    x_proxy_values = np.logspace(np.log10(x_proxy_min), np.log10(x_proxy_max), num_points)

    # T-proxy values (abstract time dimension)
    t_proxy_min = 1e-10
    t_proxy_max = 1e10
    t_proxy_values = np.logspace(np.log10(t_proxy_min), np.log10(t_proxy_max), num_points)

    # Create a meshgrid for the surface plot
    X_grid, T_grid = np.meshgrid(x_proxy_values, t_proxy_values)
    
    # Initialize the Z-grid (Abstract Energy)
    Z_energy_grid = np.zeros_like(X_grid, dtype=float)

    # Calculate Energy for each point on the grid
    for i in range(num_points):
        for j in range(num_points):
            Z_energy_grid[i, j] = calculate_abstract_energy(
                selected_mass_for_plot, X_grid[i, j], T_grid[i, j], c, lam
            )

    # Check for non-positive values in Z_energy_grid for log scale
    log_z_scale = True
    if np.any(Z_energy_grid <= 0) or np.all(np.isnan(Z_energy_grid)): # Also check if all are NaN
        log_z_scale = False
        print(f"\nWarning: Abstract Energy for {selected_object_name} contains non-positive or all NaN values. Z-axis will be linear.")

    # --- GENERATE THE 3D SURFACE PLOT USING PLOTLY GO ---
    fig = go.Figure(data=[go.Surface(z=Z_energy_grid, x=X_grid, y=T_grid,
                                     colorscale='Viridis',
                                     cmin=np.nanmin(Z_energy_grid) if np.any(np.isfinite(Z_energy_grid)) else None,
                                     cmax=np.nanmax(Z_energy_grid) if np.any(np.isfinite(Z_energy_grid)) else None
                                     )])

    fig.update_layout(
        title=f"Abstract Energy Surface for {selected_object_name} Mass<br><sup>(Mathematical Exploration of Abstract Spatial (x) and Temporal (t) Coordinates)</sup>",
        scene=dict(
            xaxis_title="Abstract Spatial Coordinate (x) (Arbitrary Units)", # Renamed
            yaxis_title="Abstract Temporal Coordinate (t) (Arbitrary Units)", # Renamed
            zaxis_title="Abstract Energy (J-like Units)",
            xaxis_type="log",
            yaxis_type="log",
            zaxis_type="log" if log_z_scale else "linear",
            camera=dict(eye=dict(x=1.5, y=1.5, z=0.8))
        ),
        title_x=0.5,
        hoverlabel=dict(namelength=-1)
    )
    
    fig.show()

else:
    print("No valid object selected. No plot will be displayed.")

# --- PRINT SELECTED VALUES FOR INSPECTION (Optional, if needed) ---
if selected_mass_index != -1:
    print("\n--- Summary for Selected Object's Abstract Surface ---")
    print(f"Object Name: {selected_object_name}")
    print(f"Input Mass (M_input): {selected_mass_for_plot:.2e} kg")
    print(f"Abstract X-Proxy Range: {x_proxy_min:.1e} to {x_proxy_max:.1e} (arbitrary units)")
    print(f"Abstract T-Proxy Range: {t_proxy_min:.1e} to {t_proxy_max:.1e} (arbitrary units)")
    if log_z_scale:
        print(f"Abstract Energy Range: {np.nanmin(Z_energy_grid):.2e} to {np.nanmax(Z_energy_grid):.2e} (J-like units, log scale)")
    else:
        print(f"Abstract Energy Range: {np.nanmin(Z_energy_grid):.2e} to {np.nanmax(Z_energy_grid):.2e} (J-like units, linear scale)")
else:
    print("\nNo object selected to display summary.")

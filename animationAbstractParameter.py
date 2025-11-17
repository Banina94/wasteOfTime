import numpy as np
from scipy.optimize import fsolve
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd # Import pandas

# --- Constants (using physical values, but remember the context is abstract) ---
c = 2.99792458e8  # Speed of light (m/s)
hbar = 1.054571817e-34 # Reduced Planck constant (J*s)

# --- Function to represent the equation for numerical solving ---
# We want to find lambda such that f(lambda) = 0
def equation_for_lambda(lambda_val, E_input, M_input_val, Q_val):
    """
    The function to find the root of: c^2 * exp(lambda * M_input) * (1 + exp(lambda))^(-Q) - E = 0
    Args:
        lambda_val (float): The abstract scale parameter we are trying to find.
        E_input (float): The abstract energy input.
        M_input_val (float): The abstract generalized mass input.
        Q_val (float): The abstract quantum-like term (simplified to a real number for this example).
    Returns:
        float: The difference that should be zero when lambda_val is the solution.
    """
    try:
        # Numerical stability checks
        # Avoid issues with very large lambda_val leading to overflow in exp(lambda_val)
        if lambda_val * M_input_val > 700 or lambda_val > 700:
            return np.inf
        if lambda_val * M_input_val < -700 or lambda_val < -700:
            return -np.inf

        term1 = np.exp(lambda_val * M_input_val)
        term2 = (1 + np.exp(lambda_val))**(-Q_val)
        calculated_E = c**2 * term1 * term2
        return calculated_E - E_input
    except OverflowError:
        return np.inf
    except Exception: # Catch any other numerical issues
        return np.nan

# --- Function to find lambda for given inputs ---
def find_lambda(E_val, M_val, Q_val, initial_guess=0.1):
    """
    Numerically solves for lambda given E, M_input, and Q.
    Args:
        E_val (float): Abstract energy.
        M_val (float): Abstract mass input.
        Q_val (float): Abstract quantum term.
        initial_guess (float): An initial guess for lambda to help the solver.
    Returns:
        float: The calculated abstract lambda value, or NaN if no solution is found.
    """
    try:
        # Using a more robust method like 'hybr' which is often good for non-linear systems
        # The 'args' tuple must match the order of parameters in equation_for_lambda after lambda_val
        result = fsolve(equation_for_lambda, initial_guess, args=(E_val, M_val, Q_val), factor=0.1, xtol=1e-8)
        lambda_solution = result[0]

        # Verify if the found solution is indeed a root
        if np.isclose(equation_for_lambda(lambda_solution, E_val, M_val, Q_val), 0, atol=1e-6):
            return lambda_solution
        else:
            return np.nan # Solution found but not a valid root
    except Exception as e:
        # print(f"Solver failed for E={E_val:.2e}, M={M_val:.2e}, Q={Q_val:.1f}. Error: {e}")
        return np.nan

# --- Main part for demonstration and graphing with Plotly ---

if __name__ == "__main__":
    # Define ranges for your abstract input parameters
    # Choose ranges carefully; extremely large or small values can cause numerical instability
    E_values_abstract = np.logspace(-12, -9, 20) # Range for abstract E (J)
    M_values_abstract = np.logspace(-28, -26, 10) # Range for abstract M_input (kg)
    Q_values_abstract = np.linspace(0.1, 5.0, 10) # Range for abstract Q (dimensionless)

    # Store results for Plotly
    E_coords = []
    M_coords = []
    Q_coords = []
    lambda_results = []
    initial_guess_history = {} # To store last successful lambda for better warm-starting fsolve

    print("Calculating solutions... This might take a moment.")
    total_iterations = len(E_values_abstract) * len(M_values_abstract) * len(Q_values_abstract)
    current_iteration = 0

    # Nested loops to generate combinations of E, M, Q
    for E_val in E_values_abstract:
        for M_val in M_values_abstract:
            for Q_val in Q_values_abstract:
                current_iteration += 1
                if current_iteration % 100 == 0:
                    print(f"Progress: {current_iteration}/{total_iterations}")

                # Use a more adaptive initial guess for fsolve
                key_tuple = (M_val, Q_val)
                initial_guess_for_this_point = initial_guess_history.get(key_tuple, 0.1)

                lambda_found = find_lambda(E_val, M_val, Q_val, initial_guess=initial_guess_for_this_point)

                if not np.isnan(lambda_found):
                    E_coords.append(E_val)
                    M_coords.append(M_val)
                    Q_coords.append(Q_val)
                    lambda_results.append(lambda_found)
                    initial_guess_history[key_tuple] = lambda_found

    print("Calculations complete. Generating plot.")

    # Create a Pandas DataFrame
    data = pd.DataFrame({
        'Abstract Energy (E)': E_coords,
        'Abstract Mass Input (M_input)': M_coords,
        'Abstract Quantum Term (Q)': Q_coords,
        'Abstract Parameter (λ)': lambda_results
    })

    # Create the 3D Scatter plot
    fig = px.scatter_3d(data,
                        x='Abstract Energy (E)',
                        y='Abstract Mass Input (M_input)',
                        z='Abstract Quantum Term (Q)',
                        color='Abstract Parameter (λ)',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        opacity=0.7,
                        title='Abstract λ as a Function of Abstract E, M_input, and Q',
                        labels={'Abstract Energy (E)': 'E (Abstract Joules)',
                                'Abstract Mass Input (M_input)': 'M_input (Abstract kg)',
                                'Abstract Quantum Term (Q)': 'Q (Abstract Dimensionless)'},
                        log_x=True,
                        log_y=True) # Apply log scale to x and y axes for E and M_input

    fig.update_layout(scene = dict(
                        xaxis_title='E (Abstract Joules)',
                        yaxis_title='M_input (Abstract kg)',
                        zaxis_title='Q (Abstract Dimensionless)'),
                      margin=dict(l=0, r=0, b=0, t=40))

    # --- Save the plot as an HTML file ---
    plot_filename = "abstract_lambda_3d_plot.html"
    fig.write_html(plot_filename)
    print(f"\n3D interactive plot saved to {plot_filename}. Open this file in your web browser to view the graph.")

    # --- Verifying Calculations below the graph ---
    print("\n--- Verifying Calculations ---")
    if len(E_coords) > 0:
        # Let's pick 3 random points to verify
        num_examples = min(3, len(E_coords)) # Don't try to pick more than available points
        random_indices = np.random.choice(len(E_coords), num_examples, replace=False)

        for i, idx in enumerate(random_indices):
            E_example = E_coords[idx]
            M_example = M_coords[idx]
            Q_example = Q_coords[idx]
            lambda_example = lambda_results[idx]

            print(f"\n--- Example {i+1} ---")
            print(f"Input E (Abstract): {E_example:.2e}")
            print(f"Input M_input (Abstract): {M_example:.2e}")
            print(f"Input Q (Abstract): {Q_example:.1f}")
            print(f"Calculated Abstract Lambda (λ): {lambda_example:.4f}")

            # Recalculate E using the found lambda and other inputs
            calculated_E_check = c**2 * np.exp(lambda_example * M_example) * (1 + np.exp(lambda_example))**(-Q_example)
            print(f"Verifying: Recalculated E with found λ: {calculated_E_check:.2e}")
            print(f"Difference (Recalculated E - Input E): {calculated_E_check - E_example:.2e}")
            if np.isclose(calculated_E_check, E_example, rtol=1e-5, atol=1e-8):
                print("Verification: SUCCESS (Recalculated E is close to Input E)")
            else:
                print("Verification: FAILED (Recalculated E is NOT close to Input E)")
    else:
        print("No valid lambda values were found during calculation. Cannot provide verification examples.")

import numpy as np
import plotly.graph_objects as go
import scipy.constants as const

# Define solar mass manually (as scipy.constants doesn't include it directly)
solar_mass = 1.98847e30 # kg (approximate value for Sun's mass)

def get_object_info(object_name):
    """Returns mass, label, and type for a given object."""
    object_name_lower = object_name.lower()
    if object_name_lower == "proton":
        return const.m_p, "Proton", "elementary"
    elif object_name_lower == "neutron":
        return const.m_n, "Neutron", "elementary"
    elif object_name_lower == "electron":
        return const.m_e, "Electron", "elementary"
    elif object_name_lower == "jupiter":
        return 1.898e27, "Jupiter", "macroscopic"
    elif object_name_lower == "earth":
        return 5.972e24, "Earth", "macroscopic"
    elif object_name_lower == "black hole":
        # Let's use a stellar-mass black hole (e.g., 10 solar masses)
        return 10 * solar_mass, "Black Hole (Stellar)", "macroscopic"
    else:
        raise ValueError("Invalid object. Choose 'Proton', 'Neutron', 'Electron', 'Jupiter', 'Earth', or 'Black Hole'.")

# --- Main execution ---
if __name__ == "__main__":
    print("This script visualizes the real and imaginary parts of a relativistic quantum wave function.")
    print("For elementary particles, an interactive animation will open in your default web browser.")
    print("For macroscopic objects, a static plot will open, demonstrating the negligible quantum effects.")

    object_choice = input("Enter object (Proton, Neutron, Electron, Jupiter, Earth, Black Hole): ").strip()
    try:
        mass, object_label, object_type = get_object_info(object_choice)
    except ValueError as e:
        print(e)
        exit()

    # --- Physical Constants ---
    h_bar = const.hbar  # Reduced Planck's constant
    c = const.c         # Speed of light

    # --- Momentum Parameter ---
    # For a relativistic effect to be visible, p*c should be comparable to m*c^2
    # We choose a momentum that makes the particle somewhat relativistic if it's elementary.
    # For macroscopic objects, this momentum will still yield an immeasurably small wavelength.
    p0 = 0.5 * mass * c

    # Calculate relativistic energy for the given momentum and mass
    energy = np.sqrt((p0 * c)**2 + (mass * c**2)**2)

    # --- Spatial and Temporal Ranges ---
    if object_type == "elementary":
        # For elementary particles, plot a few wavelengths
        wavelength = (2 * np.pi * h_bar) / p0
        x_coords = np.linspace(0, 5 * wavelength, 500) # Plot a few wavelengths
        num_frames = 100 # Number of animation frames
        period = (2 * np.pi * h_bar) / energy # Period of oscillation
        time_step = period / num_frames # Time increment per frame
        print(f"\nParticle: {object_label}")
        print(f"Mass: {mass:.2e} kg")
        print(f"Momentum (p0): {p0:.2e} kg m/s")
        print(f"Calculated Wavelength: {wavelength:.2e} meters")
        print(f"Calculated Period: {period:.2e} seconds")
    else: # macroscopic
        # For macroscopic objects, the wavelength is minuscule.
        # We'll choose an arbitrary human-scale spatial range, or a very large range.
        # The wavelength will be so small it won't be visible on this scale.
        x_coords = np.linspace(0, 10, 500) # 0 to 10 meters, for instance
        num_frames = 1 # Only one static frame for macroscopic objects
        time_step = 0 # No animation for macroscopic objects
        print(f"\nObject: {object_label}")
        print(f"Mass: {mass:.2e} kg")
        print(f"Momentum (p0, theoretical): {p0:.2e} kg m/s")
        # For macroscopic objects, the de Broglie wavelength is ridiculously small
        try:
            macroscopic_wavelength = (2 * np.pi * h_bar) / p0
            print(f"Theoretical De Broglie Wavelength: {macroscopic_wavelength:.2e} meters (Extremely small!)")
        except ZeroDivisionError:
            print("Theoretical De Broglie Wavelength: Undefined for zero momentum, or practically zero.")


    # --- Create Plotly Figure ---
    frames = []
    initial_time = 0

    # Create the initial figure object
    fig = go.Figure(
        data=[
            go.Scatter(x=x_coords * (1e9 if object_type == "elementary" else 1),
                       y=np.cos((p0 * x_coords - energy * initial_time) / h_bar),
                       mode='lines', name='Real Part', line=dict(color='blue')),
            go.Scatter(x=x_coords * (1e9 if object_type == "elementary" else 1),
                       y=np.sin((p0 * x_coords - energy * initial_time) / h_bar),
                       mode='lines', name='Imaginary Part', line=dict(color='red', dash='dash')),
        ],
        layout=go.Layout(
            xaxis=dict(range=[x_coords.min() * (1e9 if object_type == "elementary" else 1),
                              x_coords.max() * (1e9 if object_type == "elementary" else 1)],
                       title=f'Position ({"nm" if object_type == "elementary" else "m"})'),
            yaxis=dict(range=[-1.1, 1.1], title='Amplitude'),
            title=f'Relativistic Quantum Wave Function for {object_label}',
            hovermode="x unified",
        )
    )

    if object_type == "elementary":
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play", method="animate", args=[None, {"frame": {"duration": time_step * 1000, "redraw": True}, "fromcurrent": True}]),
                         dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}])
                        ]
            )],
            sliders=[dict(
                steps=[
                    dict(
                        method="animate",
                        args=[[f'frame{k}'], {"mode": "immediate", "frame": {"duration": time_step * 1000, "redraw": True}, "transition": {"duration": 0}}],
                        label=f'{k*time_step*1e15:.2f} fs'
                    ) for k in range(num_frames)
                ],
                transition=dict(duration=0),
                xanchor="left",
                currentvalue=dict(font=dict(size=16), prefix="Time: ", suffix=" fs", visible=True, xanchor="right"),
                len=0.9
            )]
        )
        # Populate frames for animation for elementary particles
        for k in range(num_frames):
            current_time = k * time_step
            current_phase = (p0 * x_coords - energy * current_time) / h_bar
            current_real_psi = np.cos(current_phase)
            current_imag_psi = np.sin(current_phase)

            frames.append(go.Frame(
                data=[
                    go.Scatter(x=x_coords * 1e9, y=current_real_psi),
                    go.Scatter(x=x_coords * 1e9, y=current_imag_psi),
                ],
                name=f'frame{k}',
                layout=go.Layout(title_text=f'Relativistic Quantum Wave Function for {object_label} (t = {current_time*1e15:.2f} fs)')
            ))
        fig.frames = frames

    else: # macroscopic objects - static plot with specific title
        fig.update_layout(
            title=dict(
                text=f'Relativistic Quantum Wave Function for {object_label}<br><sup>Note: For macroscopic objects, quantum wave behavior is not practically observable.</sup>',
                x=0.5, # Center the title
                xanchor='center'
            ),
            # Remove animation controls for static plot
            updatemenus=[],
            sliders=[]
        )

    fig.show()
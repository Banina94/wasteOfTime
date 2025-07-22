import numpy as np
import matplotlib.pyplot as plt

# --- CONFIG ---
GRID_SIZE = (4, 4)  # 4x4 chip (16 Compute Units)
MEMORY_LOCATIONS = [(0, 0), (3, 3)]  # Memory Units at corners
HEAT_DECAY = 0.95  # cooling rate per cycle
WORKLOAD_DENSITY = 0.6  # percent of CUs active per step

# --- INIT ---
chip = np.zeros(GRID_SIZE)  # Heatmap of chip
workload = np.random.rand(*GRID_SIZE) < WORKLOAD_DENSITY
memory_map = np.zeros(GRID_SIZE)
for loc in MEMORY_LOCATIONS:
    memory_map[loc] = 1  # mark memory units

# --- SIMULATION FUNCTION ---
def run_simulation(steps=20):
    global chip
    history = []

    for step in range(steps):
        # Random workload update (simulate changing AI workload)
        active_units = np.random.rand(*GRID_SIZE) < WORKLOAD_DENSITY
        heat_gen = active_units.astype(float)

        # Simulate data movement cost to memory (distance-based)
        for x in range(GRID_SIZE[0]):
            for y in range(GRID_SIZE[1]):
                if active_units[x, y]:
                    min_dist = min([np.linalg.norm(np.array([x, y]) - np.array(mem)) for mem in MEMORY_LOCATIONS])
                    heat_gen[x, y] += min_dist * 0.05  # simulate data-fetch cost

        # Update heat
        chip = chip * HEAT_DECAY + heat_gen
        history.append(chip.copy())

    return history

# --- RUN ---
heatmap_history = run_simulation(steps=30)

# --- VISUALIZE ---
def show_heatmap(final_only=False):
    if final_only:
        plt.imshow(heatmap_history[-1], cmap='hot', interpolation='nearest')
        plt.title("Final Heatmap")
        plt.colorbar()
        plt.show()
    else:
        for i, frame in enumerate(heatmap_history):
            plt.clf()
            plt.imshow(frame, cmap='hot', interpolation='nearest')
            plt.title(f"Step {i+1}")
            plt.pause(0.1)
        plt.show()

show_heatmap(final_only=True)

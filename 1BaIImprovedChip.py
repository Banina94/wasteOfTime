import numpy as np
import matplotlib.pyplot as plt
import random

GRID_SIZE = (4, 4)
HEAT_DECAY = 0.95
WORKLOAD_DENSITY = 0.6
NUM_GENERATIONS = 20
POPULATION_SIZE = 10
STEPS_PER_SIM = 25
MEMORY_COUNT = 2  # number of memory units to evolve

# --- Simulation Engine ---
def run_chip_sim(memory_locs, steps=STEPS_PER_SIM):
    chip = np.zeros(GRID_SIZE)
    for _ in range(steps):
        active_units = np.random.rand(*GRID_SIZE) < WORKLOAD_DENSITY
        heat_gen = active_units.astype(float)

        for x in range(GRID_SIZE[0]):
            for y in range(GRID_SIZE[1]):
                if active_units[x, y]:
                    min_dist = min([np.linalg.norm(np.array([x, y]) - np.array(mem)) for mem in memory_locs])
                    heat_gen[x, y] += min_dist * 0.05

        chip = chip * HEAT_DECAY + heat_gen
    return chip

# --- Fitness Function ---
def score_layout(memory_locs):
    final_heatmap = run_chip_sim(memory_locs)
    return np.mean(final_heatmap)  # lower = better

# --- Evolution Engine ---
def random_layout():
    locs = set()
    while len(locs) < MEMORY_COUNT:
        locs.add((random.randint(0, GRID_SIZE[0]-1), random.randint(0, GRID_SIZE[1]-1)))
    return list(locs)

def mutate_layout(layout):
    new_layout = layout.copy()
    i = random.randint(0, len(new_layout) - 1)
    new_layout[i] = (random.randint(0, GRID_SIZE[0]-1), random.randint(0, GRID_SIZE[1]-1))
    return new_layout

def crossover(layout1, layout2):
    split = len(layout1) // 2
    return layout1[:split] + layout2[split:]

def evolve():
    population = [random_layout() for _ in range(POPULATION_SIZE)]

    for gen in range(NUM_GENERATIONS):
        scored = [(layout, score_layout(layout)) for layout in population]
        scored.sort(key=lambda x: x[1])  # sort by fitness (lower is better)
        best_layouts = [layout for layout, _ in scored[:POPULATION_SIZE // 2]]

        print(f"Gen {gen+1} | Best Score: {scored[0][1]:.4f} | Layout: {scored[0][0]}")

        # Reproduce next generation
        next_gen = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = random.sample(best_layouts, 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.3:
                child = mutate_layout(child)
            next_gen.append(child)
        population = next_gen

    return scored[0][0], run_chip_sim(scored[0][0])

# --- Run Evolution ---
best_mem_layout, best_heatmap = evolve()

# --- Visualize ---
plt.imshow(best_heatmap, cmap='hot', interpolation='nearest')
plt.title(f"Optimized Heatmap\nMemory Locations: {best_mem_layout}")
plt.colorbar()
plt.show()

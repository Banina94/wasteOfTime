from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit.utils import algorithm_globals
from qiskit_optimization.converters import QuadraticProgramToQubo

# Set reproducibility
algorithm_globals.random_seed = 42

# Define renewable deployment problem
problem = QuadraticProgram()

# Decision variables: build at 4 sites
sites = ['x0', 'x1', 'x2', 'x3']
for site in sites:
    problem.binary_var(site)

# Installation costs (in $M)
costs = {'x0': 5, 'x1': 4, 'x2': 7, 'x3': 6}
# Power potential (in MW) - we want to maximize this
power = {'x0': 12, 'x1': 10, 'x2': 15, 'x3': 9}

# Convert to minimization: cost - power (normalized)
objective = {k: costs[k] - 0.5 * power[k] for k in sites}
problem.minimize(linear=objective)

# Constraints:
# Budget constraint: sum(costs[x]*x) <= 13
problem.linear_constraint(
    linear=costs, sense='LE', rhs=13, name='budget'
)

# Must activate at least 2 sites
problem.linear_constraint(
    linear={k: 1 for k in sites}, sense='GE', rhs=2, name='min_sites'
)

# Convert to QUBO
converter = QuadraticProgramToQubo()
qubo = converter.convert(problem)

# Set up QAOA solver
sampler = Sampler()
qaoa = QAOA(sampler=sampler, reps=1)
optimizer = MinimumEigenOptimizer(qaoa)

# Solve the QUBO
result = optimizer.solve(qubo)

# Output
print("🔋 Optimal Site Selection:")
for k, v in result.variables_dict.items():
    print(f"  {k} = {v}")

print(f"\n💰 Total Cost: ${sum(costs[k] for k in costs if result.variables_dict[k] == 1)}M")
print(f"⚡ Total Power: {sum(power[k] for k in power if result.variables_dict[k] == 1)} MW")
print(f"🎯 Objective Function Value: {result.fval:.2f}")

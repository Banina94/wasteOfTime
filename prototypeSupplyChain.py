from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit.utils import algorithm_globals
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_aer import AerSimulator

# Set reproducibility
algorithm_globals.random_seed = 42

# Define QUBO: 3 warehouses (x0, x1, x2), with constraints and cost
qubo = QuadraticProgram()
qubo.binary_var('x0')
qubo.binary_var('x1')
qubo.binary_var('x2')

# Minimize cost of opening warehouses
qubo.minimize(linear={'x0': 3, 'x1': 2, 'x2': 4})

# Constraint: At least 2 warehouses open
qubo.linear_constraint(linear={'x0': 1, 'x1': 1, 'x2': 1}, sense='GE', rhs=2, name='constraint')

# Convert to QUBO
converter = QuadraticProgramToQubo()
qubo_problem = converter.convert(qubo)

# Solve using QAOA with a sampler
sampler = Sampler()
qaoa = QAOA(sampler=sampler, reps=1)
optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qubo_problem)

# Show result
print("Optimal solution:", result.variables_dict)
print("Minimum cost:", result.fval)

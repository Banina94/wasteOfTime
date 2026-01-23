import pennylane as qml
import numpy as np
import random

n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

# Define the problem Hamiltonian (e.g., Ising or QUBO)
@qml.qnode(dev)
def circuit(params):
    for i in range(n_qubits):
        qml.RY(params[i], wires=i)
    for i in range(n_qubits - 1):
        qml.CNOT(wires=[i, i+1])
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))

# Q-learning: states are parameter vectors; actions = small parameter tweaks
params = np.random.rand(n_qubits)
alpha = 0.1  # learning rate
gamma = 0.95  # discount factor
eps = 0.1     # exploration

for episode in range(100):
    action = np.random.randn(n_qubits) * 0.1 if random.random() < eps else 0
    new_params = params + action
    reward = -circuit(new_params)  # minimize expectation
    params = params + alpha * (reward) * action
    if episode % 10 == 0:
        print(f"Episode {episode}: Energy = {circuit(params):.4f}")

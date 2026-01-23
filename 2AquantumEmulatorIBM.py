import torch
import torch.nn as nn
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit import Parameter
import numpy as np
import matplotlib.pyplot as plt

# Setup quantum simulator
backend = Aer.get_backend("aer_simulator_statevector")

# Quantum circuit as a PyTorch module
class QuantumCircuitLayer(nn.Module):
    def __init__(self, n_qubits):
        super().__init__()
        self.n_qubits = n_qubits
        self.theta = nn.Parameter(torch.randn(n_qubits))  # trainable parameters

    def forward(self, x):
        # Construct parameterized quantum circuit
        qc = QuantumCircuit(self.n_qubits)
        for i in range(self.n_qubits):
            qc.rx(x[i], i)
            qc.ry(self.theta[i], i)
        qc.measure_all()

        # Simulate and return expectation value (Z measurement on first qubit)
        qc.save_statevector()
        job = execute(qc, backend)
        result = job.result()
        statevector = result.get_statevector(qc)
        probs = np.abs(statevector) ** 2

        # Simple expectation value (can be replaced with better measurement)
        expectation = 1 - 2 * probs[1]  # Z expectation on qubit 0
        return torch.tensor([expectation], dtype=torch.float32)

# Hybrid quantum-classical model
class HybridModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 2)
        self.q_layer = QuantumCircuitLayer(n_qubits=2)
        self.output = nn.Linear(1, 1)

    def forward(self, x):
        qc = QuantumCircuit(self.n_qubits, self.n_qubits)
        for i in range(self.n_qubits):
            qc.rx(x[i], i)
            qc.ry(self.theta[i], i)
        qc.measure(range(self.n_qubits), range(self.n_qubits))
    
        job = backend.run(qc, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)
    
        # Convert counts to expectation value for qubit 0
        zero_counts = sum(v for k, v in counts.items() if k[-1] == '0')
        one_counts = sum(v for k, v in counts.items() if k[-1] == '1')
        expectation = (zero_counts - one_counts) / (zero_counts + one_counts)

        return torch.tensor([expectation], dtype=torch.float32)

# Toy training loop
model = HybridModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
loss_fn = nn.BCELoss()

# Dummy data: XOR-like logic
X = torch.tensor([[0.0, 0.0],
                  [0.0, 1.0],
                  [1.0, 0.0],
                  [1.0, 1.0]])
Y = torch.tensor([[0.0], [1.0], [1.0], [0.0]])

for epoch in range(10):  # Short run for demo
    total_loss = 0
    for i in range(len(X)):
        optimizer.zero_grad()
        y_pred = model(X[i].unsqueeze(0))
        loss = loss_fn(y_pred, Y[i])
        loss.backward()

        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} Loss: {total_loss:.4f}")

plt.show()

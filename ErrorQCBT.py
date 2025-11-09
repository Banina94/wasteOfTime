# --- 3. Simulation and AI-QEC Performance Analysis ---

# Run the simulations
result_ideal = simulator.run(shor_qc, shots=shots).result()
result_env_only = simulator.run(shor_qc, noise_model=noise_env_only, shots=shots).result()
result_no_ai = simulator.run(shor_qc, noise_model=noise_qcbt_no_ai, shots=shots).result()
result_with_ai = simulator.run(shor_qc, noise_model=noise_qcbt_with_ai, shots=shots).result()

# Function to estimate error based on the most common (assumed correct) state
def get_error_rate(counts):
    max_count = max(counts.values())
    total_shots = sum(counts.values())
    return (total_shots - max_count) / total_shots

# --- Output and Interpretation ---
print("\n--- QCBT™ Simulation with AI Error Correction ---")
print(f"Qubit T1, AI-Mitigated: {T1_AI_QEC_TOTAL:.2e} seconds\n")

# Calculate Error Rates
error_ideal = get_error_rate(result_ideal.get_counts())
error_env_only = get_error_rate(result_env_only.get_counts())
error_no_ai = get_error_rate(result_no_ai.get_counts())
error_with_ai = get_error_rate(result_with_ai.get_counts())

print(f"1. Ideal Circuit Error Rate: {error_ideal:.4f}")
print(f"2. Environmental Only Error Rate: {error_env_only:.4f}")
print(f"3. QCBT + Env (NO AI) Error Rate: {error_no_ai:.4f}")
print(f"4. QCBT + Env (WITH AI) Error Rate: {error_with_ai:.4f}")

# Interpretation of the AI's role:
mitigation_benefit = error_no_ai - error_with_ai
print(f"\nAI-QEC Mitigation Benefit (Reduction in Error): {mitigation_benefit:.4f}")

if error_with_ai < error_no_ai:
    print("Conclusion: The AI-QEC successfully mitigated the combined environmental and QCBT-induced error, resulting in a lower error rate.")
elif error_with_ai == error_no_ai:
     print("Conclusion: The QCBT-induced error dominates, and the AI's limited resistance (5%) was not enough to show a significant benefit.")
else:
     print("Conclusion: ERROR IN MODEL - The AI should, at minimum, improve the environmental component.")

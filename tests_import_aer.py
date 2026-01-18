try:
    from qiskit.providers.aer import Aer
    print('qiskit.providers.aer')
except Exception as e:
    print('qiskit.providers.aer failed:', type(e).__name__, e)
try:
    from qiskit_aer import Aer
    print('qiskit_aer')
except Exception as e:
    print('qiskit_aer failed:', type(e).__name__, e)

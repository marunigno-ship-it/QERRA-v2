# qerra_hybrid_test.py - Full hybrid quantum-classical test with safety kernel (Nayan PDF)
# Fixed noise model – uses depolarizing_error for IBM sim

import time
import random
from typing import Dict
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error  # Fixed import

# Safety Kernel (modular for regions)
def safety_kernel(ai_output: Dict, thresholds: Dict, region: str = 'UAE'):
    """Deterministic override kernel with region modes"""
    
    # Common PEMEV ethical check (all regions)
    if sum(ai_output.get('pemev_vectors', [0])) <= 0:
        return {'action': 'safe_state', 'reason': 'PEMEV ethical violation'}

    start = time.time()

    if region == 'UAE':  # Light ethics focus
        if ai_output.get('confidence', 0) < 0.80:
            return {'action': 'halt', 'reason': 'UAE ethics low confidence'}
        ai_output['audit_trace'] = f'UAE mode passed at {(time.time()-start)*1000:.2f}ms'
        return ai_output

    elif region == 'USA':  # Voluntary NIST/state
        if ai_output.get('confidence', 0) < 0.75:
            return {'action': 'override', 'reason': 'USA bias disclosure required'}
        ai_output['audit_trace'] = f'USA voluntary passed at {(time.time()-start)*1000:.2f}ms'
        return ai_output

    elif region == 'EU':  # Strict EU AI Act + ISO 10218
        if ai_output.get('confidence', 0) < 0.85:
            return {'action': 'halt', 'reason': 'EU AI Act robustness'}
        noisy = ai_output.get('confidence', 0) + random.uniform(-0.05, 0.05)
        if noisy < 0.70 or (time.time()-start)*1000 > thresholds.get('latency_ms', 50):
            return {'action': 'halt', 'reason': 'EU noise/latency override (ISO 10218)'}
        ai_output['audit_trace'] = f'EU compliant passed at {(time.time()-start)*1000:.2f}ms'
        return ai_output

    return ai_output

# Simple PEMEV vector calculation (your style)
def calculate_pemev(quantum_result):
    """Dummy PEMEV from quantum result (expand as needed)"""
    return [quantum_result.get('000', 0) / 1024, quantum_result.get('001', 0) / 1024, quantum_result.get('010', 0) / 1024]

# Hybrid quantum-classical simulation (IBM W-state with noise)
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0,1)
qc.cx(1,2)
qc.measure_all()

noise_model = NoiseModel()  # Simulated IBM noise
error_rate = random.uniform(0.01, 0.05)  # Random rate
depolarize = depolarizing_error(error_rate, 1)  # Fixed: proper QuantumError
noise_model.add_all_qubit_quantum_error(depolarize, 'h')  # Add to H gate

simulator = AerSimulator(noise_model=noise_model)
result = simulator.run(qc, shots=1024).result()
quantum_counts = result.get_counts()

# Fake AI output from quantum (confidence from counts)
ai_output = {
    'action': 'move_forward',
    'confidence': max(quantum_counts.values()) / 1024,
    'pemev_vectors': calculate_pemev(quantum_counts)
}

thresholds = {'latency_ms': 50}

# Apply kernel + test
print("UAE Mode:", safety_kernel(ai_output.copy(), thresholds, 'UAE'))
print("USA Mode:", safety_kernel(ai_output.copy(), thresholds, 'USA'))
print("EU Mode:", safety_kernel(ai_output.copy(), thresholds, 'EU'))

# 100-run stress test (EU mode)
print("\n=== 100-run stress test (EU mode) ===")
start_time = time.time()
for _ in range(100):
    safety_kernel(ai_output.copy(), thresholds, 'EU')
avg_latency = ((time.time() - start_time) / 100) * 1000
print(f"Average latency: {avg_latency:.2f} ms → Under 50ms: {avg_latency < 50}")

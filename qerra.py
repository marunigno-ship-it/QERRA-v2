# qerra.py
# Copyright (c) 2025-2026 Marussa Metocharaki (@marunigno) - Greece
# All rights reserved.
#
# This file is part of QERRA-v2 and is licensed under the
# GNU Affero General Public License v3.0 (AGPL-3.0)
# Full license: https://github.com/marunigno-ship-it/QERRA-v2/blob/main/LICENSE
# SPDX-License-Identifier: AGPL-3.0-or-later





import numpy as np
from qutip import *
from scipy.optimize import minimize
import requests  # For fetching quantum randomness
import hashlib   # Extra security (optional but good)
from safety_kernel import safety_kernel


def get_quantum_seed():
    try:
        # Fetch 32 real quantum bytes from QDay (free, fast)
        response = requests.get("https://qday.dev/v1/bytes?n=32&cnt=1&fmt=hex")
        response.raise_for_status()  # Check if it worked
        quantum_hex = response.text.strip()
        
        # Turn into a big safe seed number
        seed_int = int(quantum_hex, 16)
        print(f"Used real quantum seed: {quantum_hex}")  # Shows you the quantum string!
        return seed_int
    except:
        # If internet issue, fallback to old fake seed
        print("No connection—using fake seed for now")
        return 42

thresholds = {'latency_ms': 50}
safe_output = safety_kernel(ai_decision, thresholds, region='UAE')   # change to 'EU' or 'USA' anytime
final_action = safe_output.get('action', ai_decision.get('action'))


# QERRA: Quantum Ethical Rescue Resource Allocator by Marussa Metocharaki (@marunigno), aided by Grok (xAI)
# VQC for ethical binary classification (e.g., allocate resources? 1=yes, 0=no)
quantum_seed = get_quantum_seed()
np.random.seed(quantum_seed)  # Now truly quantum!
num_samples = 500
X = np.random.rand(num_samples, 4) * 2 * np.pi  # Features: [urgency, risk, ethical_impact, resource_avail]
y = np.array([1 if np.sum(x) >= 6 else 0 for x in X])  # Ethical threshold

train_size = int(0.8 * num_samples)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Gates
def rx(theta): return Qobj([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]], dims=[[2],[2]])
def ry(theta): return Qobj([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]], dims=[[2],[2]])
cz_gate = Qobj([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]], dims=[[2,2],[2,2]])

# Feature Map: RX encoding
def apply_feature_map(psi, x):
    psi = tensor(rx(x[0]), rx(x[1])) * psi
    psi = tensor(rx(x[2]), rx(x[3])) * psi
    return psi

# Ansatz: Deeper variational (RY + CZ layers) for entanglement/ethics modeling
def apply_ansatz(psi, params):
    psi = tensor(ry(params[0]), ry(params[1])) * psi
    psi = cz_gate * psi
    psi = tensor(ry(params[2]), ry(params[3])) * psi
    psi = tensor(ry(params[4]), ry(params[5])) * psi  # Depth for expressivity
    psi = cz_gate * psi
    return psi

# Expectation <Z0> for classification
def expectation_z0(rho):
    Z0 = tensor(sigmaz(), qeye(2))
    return (rho * Z0).tr().real

# Cost: MSE with ethical bias (favor action in ambiguity)
def cost(params, X, y):
    total = 0
    for xi, yi in zip(X, y):
        psi0 = tensor(basis(2,0), basis(2,0))
        psi = apply_feature_map(psi0, xi)
        psi = apply_ansatz(psi, params)
        rho = psi * psi.dag()
        exp = expectation_z0(rho)
        pred = 1 if exp < -0.1 else 0  # Tuned threshold for ethics
        total += (pred - yi)**2
    return total / len(y)

# Train: SLSQP for better convergence
initial_params = np.pi/4 * np.ones(6)  # Informed init
result = minimize(cost, initial_params, args=(X_train, y_train), method='SLSQP', tol=1e-4)
optimized_params = result.x
print("Optimized Params:", optimized_params)
print("Training Cost:", result.fun)

# Test - Fixed loop for clarity
psi0 = tensor(basis(2,0), basis(2,0))
preds = []
for xi in X_test:
    psi = apply_feature_map(psi0, xi)
    psi = apply_ansatz(psi, optimized_params)
    rho = psi * psi.dag()
    exp = expectation_z0(rho)
    pred = 1 if exp < -0.1 else 0
    preds.append(pred)
accuracy = np.mean(np.array(preds) == y_test)
print("Test Accuracy:", accuracy)

# Ethical Audit
print("Param Magnitudes (Bias Check):", np.abs(optimized_params))  # Uniform = low bias

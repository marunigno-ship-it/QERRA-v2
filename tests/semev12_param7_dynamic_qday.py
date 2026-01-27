import numpy as np
from qutip import *
from scipy.optimize import minimize
import requests  # For fetching quantum randomness
import hashlib  # Extra security (optional but good)


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


def get_quantum_range(min_val=0, max_val=100):
    """Fetch a single random integer in [min, max] from QDay (inclusive)"""
    try:
        url = "https://qday.dev/v1/range"
        params = {"min": str(min_val), "max": str(max_val)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        random_int = int(response.text.strip())
        print(f"Quantum random in [{min_val}, {max_val}]: {random_int}")
        return random_int
    except Exception as e:
        print(f"QDay range error: {e} — fallback to local random")
        return np.random.randint(min_val, max_val + 1)  # Safe fallback


# QERRA: Quantum Ethical Rescue Resource Allocator by Marussa Metocharaki (@marunigno), aided by Grok (xAI)
# VQC for ethical binary classification (e.g., allocate resources? 1=yes, 0=no)
quantum_seed = get_quantum_seed()
np.random.seed(quantum_seed % 4294967296)  # Now truly quantum! (safe 32-bit)
num_samples = 500
X = np.random.rand(num_samples, 4) * 2 * np.pi  # Features: [urgency, risk, ethical_impact, resource_avail]

# Use QDay range for dynamic ethical threshold (example 10-14)
ethical_min = 10
ethical_max = 14
dynamic_threshold = get_quantum_range(min_val=ethical_min, max_val=ethical_max)
print(f"Dynamic ethical threshold from QDay range: {dynamic_threshold}")

y = np.array([1 if np.sum(x) >= dynamic_threshold else 0 for x in X])  # Use dynamic threshold
print("Sample Data (first 3):", X[:3])
print("Sample Labels (first 3):", y[:3])

train_size = int(0.8 * num_samples)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]


# Gates
def rx(theta): return Qobj([[np.cos(theta / 2), -1j * np.sin(theta / 2)], [-1j * np.sin(theta / 2), np.cos(theta / 2)]],
                           dims=[[2], [2]])


def ry(theta): return Qobj([[np.cos(theta / 2), -np.sin(theta / 2)], [np.sin(theta / 2), np.cos(theta / 2)]],
                           dims=[[2], [2]])


cz_gate = Qobj([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]], dims=[[2, 2], [2, 2]])


# Feature Map: RX encoding
def apply_feature_map(psi, x):
    psi = tensor(rx(x[0]), rx(x[1])) * psi
    psi = tensor(rx(x[2]), rx(x[3])) * psi
    return psi


# Ansatz: Deeper variational (extra layer for better expressivity)
def apply_ansatz(psi, params):
    # 8 parameters
    psi = tensor(ry(params[0]), ry(params[1])) * psi
    psi = cz_gate * psi
    psi = tensor(ry(params[2]), ry(params[3])) * psi
    psi = cz_gate * psi
    psi = tensor(ry(params[4]), ry(params[5])) * psi
    psi = cz_gate * psi
    psi = tensor(ry(params[6]), ry(params[7])) * psi  # extra layer
    return psi


# Expectation <Z0> for classification
def expectation_z0(rho):
    Z0 = tensor(sigmaz(), qeye(2))
    return (rho * Z0).tr().real


# Cost: MSE with ethical bias (favor action in ambiguity)
def cost(params, X, y):
    total = 0
    for xi, yi in zip(X, y):
        psi0 = tensor(basis(2, 0), basis(2, 0))
        psi = apply_feature_map(psi0, xi)
        psi = apply_ansatz(psi, params)
        rho = psi * psi.dag()
        exp = expectation_z0(rho)
        pred = 1 if exp < 0.0 else 0  # Neutral threshold
        total += (pred - yi) ** 2
    return total / len(y)


# Train: COBYLA optimizer (better for small/no-gradient problems)
initial_params = np.pi / 4 * np.ones(8)  # Informed init for deeper ansatz (8 params)
result = minimize(cost, initial_params, args=(X_train, y_train), method='COBYLA', tol=1e-4, options={'maxiter': 200})
optimized_params = result.x
print("Optimized Params:", optimized_params)
print("Training Cost:", result.fun)

# Test - Fixed loop for clarity
psi0 = tensor(basis(2, 0), basis(2, 0))
preds = []
for xi in X_test:
    psi = apply_feature_map(psi0, xi)
    psi = apply_ansatz(psi, optimized_params)
    rho = psi * psi.dag()
    exp = expectation_z0(rho)
    pred = 1 if exp < 0.0 else 0  # Neutral threshold
    preds.append(pred)
accuracy = np.mean(np.array(preds) == y_test)
print("Test Accuracy:", accuracy)

# Ethical Audit
print("Param Magnitudes (Bias Check):", np.abs(optimized_params))  # Uniform = low bias

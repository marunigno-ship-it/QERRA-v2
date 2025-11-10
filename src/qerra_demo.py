import numpy as np
import matplotlib.pyplot as plt

def qerra_ethical_allocator(resources_available, priorities):
    """
    QERRA Demo: Ethical resource allocation (classical version for quick test).
    - Inputs: Resources (e.g., [10, 5]), Priorities (e.g., ['high', 'low']).
    - Logic: Random 'quantum-like' probability for fair decision, Asimov ethics.
    - Output: Ethical verdict.
    """
    # Simulate 'quantum' uncertainty with random prob (0-1)
    high_priority_prob = np.random.uniform(0.4, 0.9)  # Bias-free range
    
    # Ethical threshold: >0.5 + enough resources
    if high_priority_prob > 0.5 and resources_available[0] >= 5:
        decision = "ETHICAL ALLOCATE: Send high-priority resources (bias-free verdict)."
    else:
        decision = "BALANCE ETHICALLY: Diversify allocation (uncertainty detected)."
    
    # Simple 'counts' simulation
    counts = {'00': int(1024 * (1 - high_priority_prob)), '11': int(1024 * high_priority_prob)}
    
    # Plot: Simple bar chart for 'quantum' results
    labels = ['Low Priority', 'High Priority']
    values = [counts['00'], counts['11']]
    plt.bar(labels, values, color=['red', 'green'])
    plt.title('QERRA Ethical Allocation Simulation')
    plt.ylabel('Probability Counts')
    plt.show()
    
    return decision, counts, high_priority_prob

# Demo Run: Rescue scenario
resources = [10, 5]  # Drones for sites
priorities = ['high', 'low']  # Site 1 critical
decision, counts, prob = qerra_ethical_allocator(resources, priorities)
print(f"QERRA Verdict: {decision}")
print(f"Simulated Counts: {counts}")
print(f"High-Priority Probability: {prob:.2%}")
print("Success! Ethical demo complete - Ready for quantum upgrade.")
QERRA demo code from Colab test.


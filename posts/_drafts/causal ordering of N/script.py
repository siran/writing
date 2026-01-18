import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for saving files
import matplotlib.pyplot as plt
import sympy  # Requires: pip install sympy

def get_causal_depth(n: int) -> int:
    """
    Returns the 'Birth Era' of n.
    This is the rank of the largest prime factor of n.
    Primes: 2->1, 3->2, 5->3, 7->4...
    """
    n = int(n)
    if n <= 1:
        return 0

    try:
        factors = sympy.primefactors(n)  # sorted list of distinct primes
        if not factors:
            return 0
        largest_prime = factors[-1]
        return int(sympy.primepi(largest_prime))  # <-- force Python int
    except (TypeError, ValueError):
        return 0

def analyze_stream(data_stream):
    """
    Takes a list/array of numbers, computes Causal Depth for each.
    Returns a numpy int array.
    """
    return np.fromiter((get_causal_depth(n) for n in data_stream), dtype=np.int64)

# --- STEP 1: GENERATE DATA ---
N_SAMPLES = 1000
MAGNITUDE = 1_000_000

# DATASET A: "INTELLIGENT / STRUCTURED" (The Signal)
structured_data = []
primes_small = [2, 3, 5, 7, 11, 13]
for _ in range(N_SAMPLES):
    num = 1
    while num < MAGNITUDE // 10:
        num *= int(np.random.choice(primes_small))
    structured_data.append(int(num))

# DATASET B: "NATURAL / RANDOM NOISE" (The Noise)
random_data = np.random.randint(MAGNITUDE // 10, MAGNITUDE, size=N_SAMPLES)

# --- STEP 2: APPLY THE CAUSAL FILTER ---
print(f"Analyzing {N_SAMPLES} samples from each source...")
depths_struct = analyze_stream(structured_data)
depths_rand = analyze_stream(random_data)

# --- STEP 3: VISUALIZE THE FEATURE SEPARATION ---
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(depths_struct, bins=50, alpha=0.7, color="cyan",
         label="Machine (Structured)", log=True)
plt.hist(depths_rand, bins=50, alpha=0.7, color="magenta",
         label="Noise (Random)", log=True)
plt.title("Feature Extraction: Causal Depth Distribution")
plt.xlabel("Causal Depth (Birth Era)")
plt.ylabel("Count (Log Scale)")
plt.legend()
plt.grid(True, alpha=0.2)

plt.subplot(1, 2, 2)
subset = 200
plt.scatter(np.array(structured_data[:subset]), depths_struct[:subset],
            color="cyan", alpha=0.8, label="Machine", s=15,
            edgecolors="black", linewidth=0.2)
plt.scatter(random_data[:subset], depths_rand[:subset],
            color="magenta", alpha=0.8, label="Noise", s=15,
            edgecolors="black", linewidth=0.2)

plt.title("The 'Alien Signal' Separation")
plt.xlabel("Number Magnitude (approx 1M)")
plt.ylabel("Causal Depth")
plt.legend()
plt.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig("alien_signal_detection.png", dpi=200, bbox_inches="tight")
print("Saved 'alien_signal_detection.png'")

# --- STEP 4: QUANTIFY THE SEPARATION ---
mean_machine = float(np.mean(depths_struct))
mean_noise = float(np.mean(depths_rand))
print(f"\n--- RESULTS ---")
print(f"Machine Data Mean Depth: {mean_machine:.1f}")
print(f"Random Data Mean Depth:  {mean_noise:.1f}")
print(f"Separation Factor:       {mean_noise / mean_machine:.1f}x")

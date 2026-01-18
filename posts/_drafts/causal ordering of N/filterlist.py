import numpy as np
import matplotlib.pyplot as plt
import sympy  # Using sympy for easy factoring of larger numbers

def get_causal_depth(n):
    """
    Returns the 'Birth Era' of n.
    This is the rank of the largest prime factor of n.
    Primes: 2->1, 3->2, 5->3, 7->4...
    """
    if n <= 1: return 0
    
    # Get prime factors. sympy.primefactors returns a sorted list of distinct prime factors.
    factors = sympy.primefactors(n)
    largest_prime = factors[-1]
    
    # We need the 'rank' of this prime (Pi function)
    # sympy.primepi(x) returns the number of primes <= x
    return sympy.primepi(largest_prime)

def analyze_stream(data_stream, label):
    """
    Takes a list of numbers, computes Causal Depth for each.
    Returns the depths.
    """
    depths = [get_causal_depth(n) for n in data_stream]
    return np.array(depths)

# --- STEP 1: GENERATE DATA ---
# Let's look at numbers around 1 Million.
N_SAMPLES = 500
MAGNITUDE = 1_000_000
VARIANCE = 50_000

# DATASET A: "INTELLIGENT / STRUCTURED"
# Numbers that humans/machines like: Round numbers, powers, highly composite.
# e.g., 1000000, 1024*1024, 360*2000, etc.
# We simulate this by multiplying small primes together.
structured_data = []
primes_small = [2, 3, 5, 7, 11, 13]
for _ in range(N_SAMPLES):
    # Construct a number from small parts
    num = 1
    while num < MAGNITUDE:
        num *= np.random.choice(primes_small)
    structured_data.append(num)

# DATASET B: "NATURAL / RANDOM NOISE"
# Just pick random integers in the same range.
random_data = np.random.randint(MAGNITUDE, MAGNITUDE * 5, size=N_SAMPLES)

# --- STEP 2: APPLY THE CAUSAL FILTER ---
print("Extracting Features...")
depths_struct = analyze_stream(structured_data, "Structured")
depths_rand = analyze_stream(random_data, "Random")

# --- STEP 3: VISUALIZE THE FEATURE SEPARATION ---
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(depths_struct, bins=30, alpha=0.7, color='cyan', label='Machine (Structured)')
plt.hist(depths_rand, bins=30, alpha=0.7, color='magenta', label='Noise (Random)')
plt.title("Feature Extraction: Causal Depth Distribution")
plt.xlabel("Causal Depth (Birth Era)")
plt.ylabel("Count")
plt.legend()
plt.grid(True, alpha=0.2)

# Scatter Plot (Magnitude vs Depth)
plt.subplot(1, 2, 2)
plt.scatter(structured_data, depths_struct, color='cyan', alpha=0.6, label='Machine', s=10)
plt.scatter(random_data, depths_rand, color='magenta', alpha=0.6, label='Noise', s=10)
plt.title("The 'Alien Signal' Separation")
plt.xlabel("Number Magnitude")
plt.ylabel("Causal Depth")
plt.legend()
plt.grid(True, alpha=0.2)

plt.tight_layout()
plt.show()

# --- STEP 4: QUANTIFY THE COMPRESSION ---
# "Compression Score" = 1 - (Causal Depth / Max Possible Depth)
# Max depth for X is roughly X/ln(X) (if X is prime)

print("\n--- RESULTS ---")
print(f"Machine Data Mean Depth: {np.mean(depths_struct):.1f}")
print(f"Random Data Mean Depth:  {np.mean(depths_rand):.1f}")
print(f"Separation Factor:       {np.mean(depths_rand) / np.mean(depths_struct):.1f}x")

sample_machine = structured_data[0]
sample_noise = random_data[0]
print(f"\nExample Machine Number: {sample_machine}")
print(f" -> Causal Depth: {get_causal_depth(sample_machine)} (Made of small primes)")
print(f"Example Noise Number:   {sample_noise}")
print(f" -> Causal Depth: {get_causal_depth(sample_noise)} (Made of large primes)")

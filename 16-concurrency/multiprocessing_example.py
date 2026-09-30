"""
Multiprocessing

Best for CPU-bound tasks (number crunching, image processing).
Each process has its own memory — bypasses Python's GIL.
"""
import multiprocessing
import time


def compute(n):
    """CPU-bound: count up to n."""
    total = sum(range(n))
    print(f"Sum to {n}: {total}")
    return total


numbers = [5_000_000, 5_000_000, 5_000_000]

# Sequential
print("--- Sequential ---")
start = time.time()
for n in numbers:
    compute(n)
print(f"Sequential time: {time.time() - start:.2f}s\n")

# Multiprocessing
print("--- Multiprocessing ---")
start = time.time()
with multiprocessing.Pool(processes=3) as pool:
    pool.map(compute, numbers)
print(f"Multiprocessing time: {time.time() - start:.2f}s")

import random
import time

import matplotlib.pyplot as plt

from dsa.sorts.bubble_sort import bubble_sort
from dsa.sorts.merge_sort import merge_sort
from dsa.sorts.insertion_sort import insertion_sort
from dsa.sorts.quick_sort import quick_sort

SORTING_ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

def benchmark_algorithm(sort_function, data):
    """Measure the time required to sort a copy of the input data."""
    start = time.perf_counter()
    sort_function(data.copy())
    end = time.perf_counter()

    return end - start

def main():
    random.seed(42)
    input_sizes = [100, 500, 1_000, 2_500, 5_000]

    results = {
        name:[]
        for name in SORTING_ALGORITHMS
    }

    for size in input_sizes:
        data = [random.randint(0, 100_000) for _ in range(size)]
        print(f"\nInput size: {size}")
        for name, sort_function in SORTING_ALGORITHMS.items():
            elapsed = benchmark_algorithm(sort_function, data)
            results[name].append(elapsed)
            print(f"{name:<15} {elapsed:.6f} seconds")
            
                

    plt.figure(figsize=(10,6))
    for name, times in results.items():
        plt.plot(input_sizes, times, marker="o", label=name)
    plt.xlabel("Input Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)

    plt.savefig("benchmarks/sorting_performance.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
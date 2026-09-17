import random
import time
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

    for size in input_sizes:
        data = [random.randint(0, 100_000) for _ in range(size)]
        print(f"\nInput size: {size}")
        for name, sort_function in SORTING_ALGORITHMS.items():
            elapsed = benchmark_algorithm(sort_function, data)
            print(f"{name:<15} {elapsed:.6f} seconds")

if __name__ == "__main__":
    main()
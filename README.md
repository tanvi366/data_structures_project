# DSA Toolkit

A Python implementation of fundamental **data structures, sorting algorithms, and searching algorithms**. The project focuses on understanding how common data structures and algorithms work internally, while maintaining clean, tested, and documented code.

## Contents

* [Sorting Algorithms](#sorting-algorithms)
* [Searching Algorithms](#searching-algorithms)
* [Data Structures](#data-structures)
* [Complexity Analysis](#complexity-analysis)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Running Tests](#running-tests)
* [Future Improvements](#future-improvements)

---

## Sorting Algorithms

The following sorting algorithms are implemented:

* **Bubble Sort**
* **Insertion Sort**
* **Merge Sort**
* **Quick Sort**

Each algorithm is implemented independently to demonstrate the different approaches to sorting and their associated time and space complexities.

## Searching Algorithms

The following searching algorithms are implemented:

* **Linear Search**
* **Binary Search**

Binary search operates on a sorted collection and demonstrates the efficiency gained from repeatedly reducing the search space.

## Data Structures

The project currently includes object-oriented implementations of:

* **Stack** — Last-In, First-Out (LIFO)
* **Queue** — First-In, First-Out (FIFO)
* **Linked List** — Node-based linear data structure

Each data structure provides methods for its core operations and includes tests covering normal usage and edge cases.

---

## Complexity Analysis

### Sorting

| Algorithm      |  Best Case | Average Case | Worst Case |     Space |
| -------------- | ---------: | -----------: | ---------: | --------: |
| Bubble Sort    |       O(n) |        O(n²) |      O(n²) |      O(1) |
| Insertion Sort |       O(n) |        O(n²) |      O(n²) |      O(1) |
| Merge Sort     | O(n log n) |   O(n log n) | O(n log n) |      O(n) |
| Quick Sort     | O(n log n) |   O(n log n) |      O(n²) | O(log n)* |

*Space complexity for Quick Sort depends on the implementation and recursion depth.

### Searching

| Algorithm     | Best Case | Average Case | Worst Case |
| ------------- | --------: | -----------: | ---------: |
| Linear Search |      O(1) |         O(n) |       O(n) |
| Binary Search |      O(1) |     O(log n) |   O(log n) |

### Data Structures

| Data Structure | Operation      | Complexity |
| -------------- | -------------- | ---------: |
| Stack          | Push           |       O(1) |
| Stack          | Pop            |       O(1) |
| Stack          | Peek           |       O(1) |
| Queue          | Enqueue        |       O(1) |
| Queue          | Dequeue        |       O(1) |
| Linked List    | Search         |       O(n) |
| Linked List    | Insert at head |       O(1) |
| Linked List    | Delete/Search  |       O(n) |

> Complexity can vary depending on the specific implementation and operation.

---

## Project Structure

```text
dsa-toolkit/
│
├── dsa/
│   ├── sorts/
│   │   ├── bubble.py
│   │   ├── insertion.py
│   │   ├── merge.py
│   │   └── quick.py
│   │
│   ├── searches/
│   │   ├── linear.py
│   │   └── binary.py
│   │
│   └── data_structures/
│       ├── stack.py
│       ├── queue.py
│       └── linked_list.py
│
├── tests/
│   ├── test_sorts.py
│   ├── test_searches.py
│   ├── test_stack.py
│   ├── test_queue.py
│   └── test_linked_list.py
│
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd dsa-toolkit
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the development dependencies:

```bash
pip install -e ".[dev]"
```

---

## Usage

### Sorting

```python
from dsa.sorts.merge import merge_sort

data = [5, 2, 8, 1, 3]

result = merge_sort(data)

print(result)
# [1, 2, 3, 5, 8]
```

### Searching

```python
from dsa.searches.binary import binary_search

data = [1, 2, 3, 4, 5]

index = binary_search(data, 4)

print(index)
# 3
```

### Stack

```python
from dsa.data_structures.stack import Stack

stack = Stack()

stack.push(10)
stack.push(20)

print(stack.pop())
# 20
```

### Queue

```python
from dsa.data_structures.queue import Queue

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)

print(queue.dequeue())
# 10
```

### Linked List

```python
from dsa.data_structures.linked_list import LinkedList

linked_list = LinkedList()

linked_list.add(10)
linked_list.add(20)
linked_list.add(30)


## Running Tests

The project uses **pytest** for automated testing.

Run the complete test suite from the project root:

```bash
pytest


## Future Improvements

Planned improvements include:

* Add automated CI testing with GitHub Actions
* Add performance benchmarks for sorting algorithms
* Compare theoretical and observed algorithmic performance
* Expand the collection of data structures and algorithms
* Improve package documentation and examples

---

## Technologies

* **Python**
* **pytest**
* Object-Oriented Programming
* Algorithms & Data Structures
* Automated Testing

## Purpose

This project was created as a practical exploration of fundamental data structures and algorithms, with an emphasis on understanding their implementations, complexity, and behaviour through testing.

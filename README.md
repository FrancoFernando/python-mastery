# Python Mastery

A structured learning resource for mastering Python, featuring explanations, examples, and exercises.

## Repository Structure

### [01-fundamentals/](01-fundamentals/)

Core Python basics including data types, operators, enums, unpacking, and the walrus operator.

### [02-data-structures/](02-data-structures/)

Built-in data structures with practical examples:

- **strings/** - slicing, joining, splitting, conversion
- **lists/** - initialization, iteration, sorting, comparison, unpacking
- **dicts/** - handling missing keys

### [03-collections-module/](03-collections-module/)

Python's `collections` standard library: `Counter`, `deque`, `namedtuple`, `OrderedDict`, and `defaultdict`.

### [04-functions/](04-functions/)

Function concepts including lambdas, built-in functions (`map`, `filter`, `reduce`), and `itertools`.

### [05-patterns/](05-patterns/)

Common patterns and techniques:

- **regex/** - string replacement, whitespace handling
- **builtin-functions/** - `zip`, `any`, `reversed`

### [exercises/](exercises/)

Programming exercises organized by source:

- **the-python-workout/** - exercises from "The Python Workout" book

## Getting Started

Each Python file contains educational comments and runnable examples. Simply run any file to see the concepts in action:

```bash
python3 01-fundamentals/data_types.py
```

## Adding New Exercises

Use the helper script to create new exercise placeholders:

```bash
cd exercises/the-python-workout
python3 create_exercise.py <number> <name>
# Example: python3 create_exercise.py 6 word-count
```

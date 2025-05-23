# CIFO-Group-G

## Wedding Seating Optimization

## 🧠 Project Context

This project tackles the **Wedding Seating Optimization Problem**, a combinatorial optimization task where guests must be assigned to tables in a way that maximizes social harmony and minimizes discomfort. The challenge lies in managing conflicting preferences, relationships, and constraints (e.g., no guest appears twice, table capacities, or enemies not sitting together).

We approach this problem using **optimization algorithms**, including:

- **Genetic Algorithm (GA)**
- **Simulated Annealing (SA)**
- **Hill Climbing (HC)**

The codebase is modular, extensible, and designed for experimentation with various operators and configurations.

---

## 📂 Folder and File Descriptions

### `optimizers/`
Contains the core optimization algorithms used to solve the problem.

- **`genetic_algorithms/`** – Modules implementing the components of the Genetic Algorithm:
  - `genetic_algorithm.py`: Main driver for the GA logic and execution.
  - `crossover.py`: Contains different crossover strategies for combining parent solutions.
  - `mutation.py`: Defines multiple mutation operations used to introduce variation.
  - `selection.py`: Implements selection strategies (e.g., battle, double roulette).
  - `helpers.py`: Utility functions for GA operations.

- **`HillClimbing.py`** – Implements the Hill Climbing optimization algorithm, which iteratively improves the current solution by exploring neighbors.
- **`SimulatedAnnealing.py`** – Contains the Simulated Annealing implementation, a probabilistic technique that explores worse solutions with a decreasing likelihood to escape local optima.

---

### `utils/`
General-purpose modules and helpers.

- `WeddingSeatingHelper.py`: Core class or functions to evaluate with several helper functions, like to generate a random initial solution, calculate fitness among others.
- `parser.py`: Contains a function that allow a easy integrate the input data into a Jupyter Notebook.

---

### Other Files

- **`Wedding Setting Optimization.zip`** – Zip version of the Jupyter Notebook (this was required to be a zip, because the initial file add more than 25MB, so it was impossible to put it on GitHub as a native Jupyter Notebook file).
- **`data/`** – Folder intended for input dataset.
- **`figures/`** – Folder that stores images that can help understand better the problem and the fitnesses.

---

## 🚀 How to Run

1. Clone the repository.
2. Ensure you have Python 3.11 and required packages installed (e.g., `numpy`, `matplotlib`).
3. Run the `Wedding Setting Optimization.ipynb` notebook, stored within the zip file for experiments and results.

---

## 📬 Contributions

This project was developed by:

- Daniel Caridade
- Gonçalo Teles
- Gonçalo Peres
- Guilherme Godinho

# CIFO-Group-G

## Wedding Seating Optimization

## 🧠 Project Context

This project tackles the **Wedding Seating Optimization Problem**, a combinatorial optimization task where guests must be assigned to tables in a way that maximizes social harmony and minimizes discomfort. The challenge lies in managing conflicting preferences, relationships, and constraints (e.g., no guest appears twice, table capacities, or enemies not sitting together).

We approach this problem using **heuristic and metaheuristic algorithms**, including:

- **Genetic Algorithm (GA)**
- **Simulated Annealing (SA)**
- **Hill Climbing (HC)**

The codebase is modular, extensible, and designed for experimentation with various operators and configurations.

---

## 📁 Repository Structure


---

## 📂 Folder and File Descriptions

### `optimizers/`
Contains the core optimization algorithms used to solve the problem.

- **`genetic_algorithms/`** – Modules implementing the components of the Genetic Algorithm:
  - `genetic_algorithm.py`: Main driver for the GA logic and execution.
  - `crossover.py`: Contains different crossover strategies for combining parent solutions.
  - `mutation.py`: Defines multiple mutation operations used to introduce variation.
  - `selection.py`: Implements selection strategies (e.g., battle, double roulette).
  - `helpers.py`: Utility functions for GA operations (e.g., population generation, fitness evaluation).

- **`HillClimbing.py`** – Implements the Hill Climbing optimization algorithm, which iteratively improves the current solution by exploring neighbors.
- **`SimulatedAnnealing.py`** – Contains the Simulated Annealing implementation, a probabilistic technique that explores worse solutions with a decreasing likelihood to escape local optima.

---

### `utils/`
General-purpose modules and helpers.

- `WeddingSeatingHelper.py`: Core class or functions to evaluate seating arrangements, handle constraints, and define problem-specific logic (e.g., guest compatibility).
- `parser.py`: Likely responsible for reading and converting input data into usable formats.

---

### Other Files

- **`Wedding Setting Optimization.ipynb`** – Main Jupyter Notebook containing experiments, visualizations, and evaluation logic.
- **`Wedding Setting Optimization.zip`** – Possibly a zipped version of the project or submission bundle.
- **`data/`** – Folder intended for input datasets (e.g., guest lists, preferences).
- **`figures/`** – Folder to store generated plots, boxplots, or performance comparisons.

---

## 🚀 How to Run

1. Clone the repository.
2. Ensure you have Python 3.x and required packages installed (e.g., `numpy`, `matplotlib`).
3. Run the `Wedding Setting Optimization.ipynb` notebook for experiments and results.

---

## 📈 Goal

The project evaluates different optimization methods for finding optimal or near-optimal wedding seating plans. It provides both quantitative (fitness values) and qualitative (visual) insights into how each algorithm performs.

---

## 📬 Contributions

Contributions and suggestions are welcome. Please submit a pull request or open an issue if you'd like to propose improvements!

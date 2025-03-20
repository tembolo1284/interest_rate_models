# 📚 Interest Rate Models Library

This project is a library for **calibrating and pricing interest rate models** using various techniques. It includes support for:

- **Ho-Lee Model**  
- **Vasicek Model**  
- **CIR Model**  
- **Black-Karasinski Model**  
- **Hull-White Model**  

The library supports multiple **pricing techniques**:  
- **Monte Carlo Simulation** (with variance reduction techniques like Antithetic Sampling)  
- **Finite Difference Methods** (Crank-Nicolson scheme)  
- **Tree-Based Methods** (Binomial Trees)  

---

## 📁 Directory Structure  

interest_rate_models/

├── cpp_data_api/ # Placeholder for the future C++ data-fetching component

├── python_lib/

│ ├── interest_rate_models/

│ │ ├── calibrators/ # Calibration methods for each model

│ │ ├── models/ # Model implementations

│ │ ├── pricing/ # Pricing methods (Monte Carlo, FDM, Trees)

│ │ ├── tests/ # Test files for each model

│ │ └── main.py # Example usage of the library

├── toolchain.sh # Script to set up environment and dependencies

├── pyproject.toml # Poetry configuration file

├── README.md # You're reading this!


---

## 🔍 Setup & Installation  
1. Make sure you have **Python 3.10+** installed.  
2. Clone the repository to your local machine.  
3. From the root directory, run:  
```bash
./toolchain.sh

This script will:

    Install poetry if not already installed.
    Set up a virtual environment.
    Install all dependencies specified in pyproject.toml.

📌 How to Run Tests

Each model has its own test file under the tests/ directory.

To run all tests, use:

```
poetry run pytest python_lib/interest_rate_models/tests

```

To run a specific test file, use:

```
poetry run pytest python_lib/interest_rate_models/tests/test_ho_lee_model.py

```

📌 How to Run the Main File

The main.py file demonstrates how to use all the models together.

Run it with:

```
poetry run python python_lib/interest_rate_models/main.py

```

📌 Logging

Extensive logging is applied across all tests and the main file. Logs include:

    Calibration process.
    Pricing process for all methods.
    Display of calculated prices.

Logs are displayed to the console in the format:

```
2025-03-19 10:32:45 - INFO - Testing Ho-Lee Model with Monte Carlo pricing...  
2025-03-19 10:32:50 - INFO - Ho-Lee Model Monte Carlo Price: 42.0  
```

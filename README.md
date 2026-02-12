# Data-Engineer-Recruitment-Task-Cloudfide
Implementation of a virtual column generator for Pandas DataFrames. Recruitment task for the Intern Data Engineer position at Cloudfide.

--- 

## 📝 Project Overview

The core of this project is the `add_virtual_column` function. It allows for dynamic creation of new DataFrame columns by performing basic arithmetic operations on existing ones, provided as a string expression.

### Key Features:
- **Dynamic Calculation**: Supports addition (`+`), subtraction (`-`), and multiplication (`*`).
- **Strict Validation**: 
    - Column names must only contain letters and underscores (`_`).
    - The function validates the existence of source columns.
    - Comprehensive error handling – returns an empty DataFrame on invalid input instead of crashing.
- **Robustness**: Handles extra spaces and various formatting in the operation string.

---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Library:** [Pandas](https://pandas.pydata.org/)
* **Testing:** Pytest / Standard Unit Testing

---

## ⚙️ Installation & Setup
**Clone the repository:**
```bash
    git clone https://github.com/vvovvel/Data-Engineer-Recruitment-Task-Cloudfide.git
    cd Data-Engineer-Recruitment-Task-Cloudfide
```
---

## 🧪 Running Tests

The project includes a suite of unit tests to ensure all validation rules and arithmetic operations work correctly.

To run the tests, execute the following command in the root directory:

```bash
    python tests.py
```
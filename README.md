
---

# Solar Challenge Week 1

## Overview

This project focuses on data profiling, cleaning, exploratory data analysis (EDA), and cross-country comparison of solar energy datasets from Benin, Sierra Leone, and Togo. It is developed as part of the B5W0 Solar Data Discovery Challenge.

## Key Objectives

* Perform systematic data profiling and missing value analysis
* Clean and preprocess solar datasets using robust statistical methods
* Apply exploratory data analysis techniques to uncover trends
* Compare energy patterns across multiple countries
* Maintain modular, readable, and well-documented codebase

---

## Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/abeelgetahun/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Analysis

You can explore and run the analysis using either Jupyter notebooks or Python scripts:

* 📓 Run the notebooks in the `notebooks/` directory for step-by-step EDA
* 🧼 Use Python scripts in `src/` to reproduce cleaning and profiling pipelines
* 📁 Cleaned datasets are exported to `data/cleaned/` (not tracked by Git)
* 📊 Visualizations and summaries are saved to `outputs/`

---

## Project Structure

```
solar-challenge-week1/
│
├── data/               # Raw datasets (not tracked by git)
├── data/cleaned/       # Cleaned datasets (not tracked by git)
├── notebooks/          # Jupyter Notebooks for EDA and analysis
├── src/                # Source code (modular functions & logic)
│   ├── cleaning.py     # Dataset cleaning functions
│   ├── eda.py          # EDA utilities (modularized)
│   └── profiling.py    # Data profiling functions
├── outputs/            # Visualizations, reports, and stats (not tracked)
├── requirements.txt    # Project dependencies
├── .gitignore
├── .github/workflows/ci.yml  # Continuous Integration workflow
└── README.md
```

---

## GitHub Actions CI

The workflow in `.github/workflows/ci.yml` automatically:

* Sets up the Python environment
* Installs dependencies
* Validates code structure
* Runs checks to ensure reliability and reproducibility

---

## Code Quality & Best Practices

✅ Modular Code:

* Core logic for cleaning, profiling, and analysis is organized into `src/` as importable modules

✅ Documentation:

* Functions and scripts include **docstrings** and **inline comments** explaining logic

✅ Version Control:

* Active use of **Git**, with visible commit history and descriptive messages
* Development occurs via **feature branches** merged through pull requests

---


## Commit & Branching Policy

* Major features are developed in **feature branches**
* Merges into `main` occur via **Pull Requests**
* Each commit is descriptive and aligned with the project's goals

---

## Contact

For questions, issues, or suggestions:
📨 [Open an issue](https://github.com/abeelgetahun/solar-challenge-week1/issues)
🔗 Contact the repository maintainer via GitHub

---


# Solar Challenge Week 1

## Project Overview

This project involves data profiling, cleaning, exploratory data analysis (EDA), and cross-country comparisons using solar datasets from Benin, Sierra Leone, and Togo.

## Environment Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/doffn/solar-challenge-week1
   cd solar-challenge-week1
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Analysis

* Execute Jupyter notebooks located in the `notebooks/` directory or run scripts found in the `src/` folder as needed.
* Cleaned datasets are saved in `data/cleaned/` (this folder is excluded from version control).
* Visualizations, charts, and statistical outputs are saved to the `outputs/` directory.

## Project Structure

```
solar-challenge-week1/
│
├── data/               # Raw datasets (not tracked by git)
├── data/cleaned/       # Cleaned datasets (not tracked by git)
├── notebooks/          # Jupyter notebooks for EDA and analysis
├── src/                # Source code (functions, classes, scripts)
├── outputs/            # Generated plots, charts, and reports (not tracked by git)
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules
├── .github/            # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml      # Continuous Integration workflow
└── README.md           # Project documentation
```

## Continuous Integration (CI)

The GitHub Actions workflow located at `.github/workflows/ci.yml` ensures the environment is correctly set up and runs automated tests on the codebase.

## Contribution & Branching

* Develop new features on separate feature branches.
* Merge changes to `main` branch only through Pull Requests with clear, descriptive commit messages.

## Contact

For questions or support, please open an issue on GitHub or reach out to the repository maintainer.

---

If you want, I can help you format this as Markdown or tailor it further!

# Bhatbhateni Sales Cleaning & Analysis

A beginner-friendly data cleaning and analysis project using the Bhatbhateni supermarket sales dataset.

## Dataset

- **File:** `Bhatbhateni_sales.csv`
- **Rows:** 18,812
- **Columns:** 11
- **Issues:** Injected nulls and duplicate rows

## What This Project Does

1. Loads and inspects the raw dataset
2. Cleans duplicate rows and missing values
3. Engineers new features (date parts, city from branch)
4. Validates financial calculations
5. Runs univariate and time-series analysis
6. Analyzes branch, city, product, customer, and payment performance
7. Detects outliers and checks correlations
8. Builds a simple predictive model
9. Summarizes business insights

## Data Cleaning Decisions

| Issue                         | Action                                      |
| ----------------------------- | ------------------------------------------- |
| 724 duplicate rows            | Removed exact duplicates                    |
| 568 missing `CustomerName`    | Filled with `"missing"`                     |
| 282 missing `ProductCategory` | Filled with most frequent value (`Grocery`) |
| 371 missing `UnitPrice`       | Calculated as `TotalAmount / Quantity`      |
| 468 missing `PaymentMethod`   | Filled with `"Unknown"`                     |

## Folder Structure

```
week4/
├── data/
│   └── Bhatbhateni_sales.csv
├── notebooks/
│   └── bhatbhateni.ipynb
├── images/
│   └── (visualizations go here)
└── README.md
```

## How to Run

1. Open `bhatbhateni.ipynb` in Jupyter Notebook or VS Code
2. Run cells top to bottom
3. Make sure `Bhatbhateni_sales.csv` is in the same folder

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Key Insights

- **Top branch by revenue:** Kathmandu - New Road
- **Top city:** Kathmandu
- **Most used payment method:** Cash
- **Highest revenue day:** Saturday
- **Top category:** Grocery

## Next Steps

- Add visualizations to the `images/` folder
- Push to GitHub with the folder structure above
- Extend the model with more features

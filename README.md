# Mutual Fund Analytics Project

## Project Overview

This project is a Mutual Fund Analytics platform developed as part of the Bluestock Fintech internship program.

The project focuses on:

* Data cleaning and validation
* SQLite database design
* Exploratory Data Analysis (EDA)
* Financial data visualization
* Mutual fund performance analysis

---

## Project Structure

```text
mutual_fund_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── bluestock_mf.db
│
├── notebooks/
│   └── EDA_Analysis.ipynb
│
├── reports/
│   └── charts/
│
├── schema.sql
├── queries.sql
├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

## Tasks Completed

### Data Cleaning

* Cleaned NAV history dataset
* Cleaned investor transactions dataset
* Cleaned scheme performance dataset
* Removed duplicates
* Validated numerical fields
* Standardized categorical values

### Database Development

* Designed SQLite star schema
* Created dimension tables
* Created fact tables
* Loaded cleaned datasets into SQLite database

### Exploratory Data Analysis

Generated 15+ visualizations including:

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trends
* Category Heatmaps
* Investor Demographics
* Geographic Distribution
* Folio Growth Analysis
* Correlation Matrix
* Sector Allocation Analysis

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

---

## Key Insights

* SIP inflows showed consistent growth over the analysis period.
* Investor participation increased significantly across categories.
* Mutual fund folios experienced steady expansion.
* Several fund categories attracted strong inflows.
* Geographic participation expanded beyond metro cities.

---

## Author

Abhilash Nutenki

Bluestock Fintech Internship Project

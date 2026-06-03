import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert returns to numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check anomalies (missing after conversion)
anomalies = df[df[return_cols].isnull().any(axis=1)]

print("Anomalies Found:", len(anomalies))

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:", len(invalid_expense))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Cleaned scheme_performance saved")
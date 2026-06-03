import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.columns)

# Date conversion
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV > 0
df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Cleaned nav_history saved")
print(df.columns)
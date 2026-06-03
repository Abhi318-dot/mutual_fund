import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Fix date format
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Check KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:")
print(len(invalid_kyc))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Cleaned investor_transactions saved")
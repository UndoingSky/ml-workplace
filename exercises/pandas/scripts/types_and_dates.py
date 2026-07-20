import pandas as pd

# Example script extracted from exercises/pandas

df = pd.DataFrame({
    "age": ["19", "21", "20"],
    "joined": ["2026-01-10", "2026-03-05", "2026-04-20"],
})

# Convert text to numeric
df["age"] = df["age"].astype(int)

# Convert text to datetime
df["joined"] = pd.to_datetime(df["joined"])

print(df.dtypes)

# You can now extract useful date parts
df["join_year"] = df["joined"].dt.year
df["join_month"] = df["joined"].dt.month
print(df)

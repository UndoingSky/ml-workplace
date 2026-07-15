import pandas as pd
from io import StringIO

csv_data = StringIO("""name,age,score,passed
Asha,19,72,yes
Ben,21,85,yes
Chen,20,90,yes
Dia,18,,no
""")

df = pd.read_csv(csv_data)

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
print(df.isna().sum())
import pandas as pd

fln = 'movies_metadata.csv'

"""Load movie dataset from a CSV file."""
df = pd.read_csv(fln, low_memory=False)
# Select relevant columns and drop rows with missing descriptions
df = df[['title', 'overview']].dropna()
# Rename 'overview' to 'description' for consistency
df.rename(columns={'overview': 'description'}, inplace=True)

print(df.head())
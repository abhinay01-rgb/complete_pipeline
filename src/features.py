import pandas as pd

df = pd.read_csv("data/processed_dataset.csv")

# Ensure correct column name (e.g., 'age' instead of 'existing_column')
if 'age' in df.columns:
    df["new_feature"] = df["age"] * 2  # Example transformation
else:
    raise KeyError("Column 'age' not found in the dataset.")

df.to_csv("data/features.csv", index=False)

print("Feature engineering complete.")

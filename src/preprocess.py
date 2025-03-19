import pandas as pd

df=pd.read_csv("data/raw_dataset.csv")

df.dropna(inplace=True)

df.to_csv("data/processed_dataset.csv",index=False)
print("data set pre processed")
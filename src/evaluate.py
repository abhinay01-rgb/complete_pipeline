import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/features.csv")
X = df.drop(columns=["target", "new_feature"])  # Exclude 'new_feature' before training

y = df["target"]

model = joblib.load("models/model.pkl")
predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)
with open("metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy}\n")

print("Model evaluation complete.")


import json

metrics = {
    "accuracy": accuracy,
    "loss": 1-accuracy
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)
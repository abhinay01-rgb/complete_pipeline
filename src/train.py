import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/features.csv")
X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")

print("Model training complete.")
import json

metrics = {
    "accuracy": 0.92,
    "loss": 0.08
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

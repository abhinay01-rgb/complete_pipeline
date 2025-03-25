import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib
import json
import yaml

# Load hyperparameters from params.yaml
with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

# Extract model parameters
algorithm = params['model']['algorithm']
C = params['model']['C']
max_iter = params['model']['max_iter']
n_estimators = params['model']['n_estimators']
max_depth = params['model']['max_depth']
kernel = params['model']['kernel']
gamma = params['model']['gamma']

# Load the dataset
df = pd.read_csv("data/features.csv")

X = df.drop(columns=["id","target", "new_feature"])  # Exclude 'new_feature' before training

y = df["target"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Select model based on the algorithm specified in params.yaml
if algorithm == "logistic_regression":
    model = LogisticRegression(C=C, max_iter=max_iter)
elif algorithm == "random_forest":
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
elif algorithm == "svm":
    model = SVC(kernel=kernel, gamma=gamma)
else:
    raise ValueError(f"Unknown algorithm: {algorithm}")

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/model.pkl")
print(f"{algorithm.capitalize()} model training complete.")


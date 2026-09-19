import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# Load dataset
df = pd.read_csv("dataset/breast-cancer.csv")

# Keep only important columns
df = df[[
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "diagnosis"
]]

# Convert diagnosis values
df["diagnosis"] = df["diagnosis"].map({
    "M": 1,
    "B": 0
})

# Inputs
X = df[[
    "radius_mean",
    "texture_mean",
    "perimeter_mean"
]]

# Output
y = df["diagnosis"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model/breast_cancer_model.pkl")
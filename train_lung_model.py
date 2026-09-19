import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# Load dataset
df = pd.read_csv("dataset/lung_cancer_examples.csv")

# Input features
X = df[[
    "Age",
    "Smokes",
    "AreaQ"
]]

# Output target
y = df["Result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Lung Cancer Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model/lung_cancer_model.pkl")

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

print("Model trained successfully!")

# Save model
joblib.dump(model, "model.pkl")
# Calculate model accuracy
predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Model Accuracy:", accuracy * 100, "%")
print("Model saved successfully!")

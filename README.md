
## Step 1: Create Project Folder

Create a folder named `ML_API`.

Open the folder in Visual Studio Code.

## Step 2: Open Terminal

Go to Terminal → New Terminal.

Check Python version:

```bash
python --version
```

Check pip version:

```bash
pip --version
```

## Step 3: Install Required Libraries

```bash
pip install flask scikit-learn joblib
```

## Step 4: Create model.py

Create a file named `model.py`.

Add the following code:

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

print("Model trained successfully!")

# Calculate accuracy
predictions = model.predict(X)
accuracy = accuracy_score(y, predictions)

print("Model Accuracy:", accuracy * 100, "%")

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")
```

## Step 5: Train and Save Model

Run the command:

```bash
python model.py
```

Check the output. The `model.pkl` file will be created automatically.

Observed training accuracy: 100%.

## Step 6: Create app.py

Create another file named `app.py`.

Add the following code:

```python
from flask import Flask, request, jsonify
import joblib

# Create Flask application
app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Flower names
flowers = ["Setosa", "Versicolor", "Virginica"]

# Home API
@app.route("/")
def home():
    return "ML API is working!"

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    features = data["features"]

    prediction = model.predict([features])
    result = flowers[int(prediction[0])]

    return jsonify({
        "prediction": result
    })

# Run application
if __name__ == "__main__":
    app.run(debug=True)
```

## Step 7: Start Flask Server

Run the command:

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

Output:

```text
ML API is working!
```

Keep the Flask server running.

## Step 8: Open Thunder Client

1. Open Thunder Client in VS Code.
2. Click on New Request.
3. Select POST method.
4. Enter the URL:

```text
http://127.0.0.1:5000/predict
```

## Step 9: Enter JSON Input

Select Body → JSON.

Enter the following data:

```json
{
    "features": [5.1, 3.5, 1.4, 0.2]
}
```

Click on Send.

## Step 10: Check API Response

Expected response:

```json
{
    "prediction": "Setosa"
}
```

HTTP Status: 200 OK

## Step 11: Analyze Response Time

Check the response time displayed in Thunder Client.

Observed Response Time: 44 ms.

## Step 12: Check Model Accuracy

Run:

```bash
python model.py
```

Observed Training Accuracy: 100%.

Note: Accuracy is calculated on the training dataset itself.

## Step 13: Project Folder Structure

```text
ML_API/
│
├── model.py
├── model.pkl
├── app.py
└── README.md
```

## Step 14: Final Result

The Flask REST API was successfully created and integrated with a trained Machine Learning model.

The prediction endpoint was tested using Thunder Client and successfully returned the flower prediction with HTTP status 200 OK.

**Observed Results:**

- Prediction: Setosa
- API Status: 200 OK
- Response Time: 44 ms
- Training Accuracy: 100%

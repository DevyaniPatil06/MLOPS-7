'''
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Create home API
@app.route("/")
def home():
    return "Welcome! My ML API is working."

# Run application
if __name__ == "__main__":
    app.run(debug=True)
'''



from flask import Flask, request, jsonify
import joblib

# Create Flask application
app = Flask(__name__)

# Load trained ML model
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

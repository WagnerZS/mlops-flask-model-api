from flask import Flask, jsonify
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("models", "model.joblib")
METRICS_PATH = os.path.join("models", "metrics.json")

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello World, Flask API is running!"})

@app.route('/health-check', methods=['GET'])
def health():
    return jsonify({"message": "OK"})

@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({"message": "OK"})

if __name__ == '__main__':
    app.run(debug=True)

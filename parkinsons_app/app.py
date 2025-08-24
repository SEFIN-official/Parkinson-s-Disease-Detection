from flask import Flask, render_template, request
import joblib
import numpy as np
import datetime
from pymongo import MongoClient

app = Flask(__name__)

# Load ML model and scaler
model = joblib.load('parkinsons_model.pkl')
scaler = joblib.load('scaler.pkl')

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Change if using Atlas
db = client["parkinsons_db"]
collection = db["predictions"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect features
        features = [float(request.form[f"f{i}"]) for i in range(1, 23)]

        # Scale features and predict
        final = scaler.transform([features])
        prediction = model.predict(final)[0]

        # Result message
        result = "🔴 Parkinson's Detected" if prediction == 1 else "🟢 No Parkinson's Detected"

        # Save data to MongoDB
        data = {
            "features": features,
            "prediction": int(prediction),
            "result_text": result,
            "timestamp": datetime.datetime.now()
        }
        collection.insert_one(data)

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

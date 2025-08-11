from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('parkinsons_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f"f{i}"]) for i in range(1, 23)]

        final = scaler.transform([features])
        prediction = model.predict(final)[0]

        result = "🔴 Parkinson's Detected" if prediction == 1 else "🟢 No Parkinson's Detected"
        return render_template('index.html', prediction_text=result)
    
    except:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numbers for all fields.")

if __name__ == '__main__':
    app.run(debug=True)

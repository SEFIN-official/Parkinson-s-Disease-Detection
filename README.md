# 🧠 Parkinson's Disease Detection using Machine Learning

This project is a web-based application for detecting Parkinson's disease using machine learning.  
It provides a **user-friendly interface** where users can input medical features such as tremors, jitter, and voice characteristics.  
The model then predicts whether the patient is likely to have Parkinson’s disease (binary classification: Yes/No).

---

## 🚀 Features
- User-friendly **Flask web interface**  
- Input medical features manually or use **Auto-Fill Sample Data**  
- Real-time prediction using trained ML model  
- Clean and simple UI for easy use  

---

## 🛠️ Technologies Used
- **Python 3.10+**
- **Flask** (Web Framework)
- **Scikit-learn** (Machine Learning)
- **Pandas & NumPy** (Data Handling)
- **Joblib** (Model Serialization)

---

## 📂 Project Structure
parkinson-detection/
│── static/ # CSS/JS files (if any)
│── templates/
│ └── index.html # Frontend UI
│── model.pkl # Trained ML model
│── app.py # Flask backend
│── requirements.txt # Dependencies




---

## ⚙️ Installation & Setup

1. Clone the repository:
  
   git clone https://github.com/your-username/parkinson-detection.git
   cd parkinson-detection
Create a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies:


pip install -r requirements.txt
Run the Flask app:
python app.py


---
Open in browser:
http://127.0.0.1:5000/

---
📊 Machine Learning Model
The model is trained using Parkinson’s dataset (UCI ML Repository).

Features include MDVP jitter, shimmer, NHR, HNR, spread1, spread2, PPE, etc.

Binary classification using Random Forest / SVM / Logistic Regression.

Model saved as model.pkl with joblib.


---
🧑‍💻 What You Learn
UI Development with Flask & HTML

Feature Engineering on medical data

Binary Classification ML pipeline

Model Deployment with Flask








Ask ChatGPT

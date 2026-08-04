# 🧠 Mental Health Score Predictor

An end-to-end Machine Learning project that predicts an individual's **Mental Health Score** based on demographic, academic, social media usage, and lifestyle-related features.

The project demonstrates a complete production-ready ML workflow, including data preprocessing, feature engineering, model training, hyperparameter tuning, FastAPI backend development, frontend integration, and cloud deployment.

---

# 🌐 Live Demo

🚀 **Live Application**

https://mental-health-score-predictor-u5yr.onrender.com/

---

# 💻 GitHub Repository

📂 Repository

https://github.com/Sarthak-Rajvaidya/Mental_Health_Score

---

# 📌 Project Overview

This project predicts an individual's mental health score using Machine Learning Regression techniques.

The complete pipeline includes:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Machine Learning Pipelines
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- FastAPI Backend
- Frontend Integration
- Cloud Deployment on Render

---

# 🎯 Objectives

- Understand the dataset through Exploratory Data Analysis
- Build reusable preprocessing pipelines
- Compare multiple regression models
- Improve model performance through Hyperparameter Tuning
- Build a production-ready prediction API
- Deploy the complete application on the cloud

---

# 🚀 Features

✅ Interactive Web Interface

✅ Real-time Mental Health Score Prediction

✅ Input Validation using Pydantic

✅ End-to-End Scikit-learn Pipeline

✅ Automatic Feature Preprocessing

✅ Production Ready FastAPI Backend

✅ Cloud Hosted on Render

---

# 🛠 Tech Stack

## Programming Language

- Python

---

## Machine Learning

- Scikit-learn
- Random Forest Regressor
- Linear Regression

---

## Data Processing

- NumPy
- Pandas

---

## Data Visualization

- Matplotlib
- Seaborn

---

## Backend

- FastAPI
- Pydantic

---

## Frontend

- HTML
- CSS
- JavaScript

---

## Deployment

- Render

---

# 📂 Machine Learning Workflow

## 1️⃣ Data Loading

- Loaded dataset
- Explored dataset shape
- Inspected data types
- Viewed sample records

---

## 2️⃣ Exploratory Data Analysis (EDA)

Performed comprehensive analysis including:

- Target Distribution
- Correlation Heatmap
- Stress Level vs Mental Health Score
- Numerical Feature Analysis
- Outlier Detection (IQR)
- Skewness Analysis

---

## 3️⃣ Feature Engineering

Separated features into:

- Skewed Numerical Features
- Numerical Features
- Ordinal Features
- Nominal Features

---

## 4️⃣ Data Preprocessing

Created independent preprocessing pipelines using Scikit-learn.

### Skewed Features

- Log Transformation
- Standard Scaling

### Numerical Features

- Standard Scaling

### Ordinal Features

- Ordinal Encoding

### Nominal Features

- One-Hot Encoding

---

## 5️⃣ Column Transformer

Combined all preprocessing pipelines into a single reusable `ColumnTransformer`.

This ensures:

- Cleaner Code
- Reusability
- Consistent Transformations
- Production-ready Workflow

---

## 6️⃣ Train-Test Split

Split the dataset into Training and Testing sets.

---

## 7️⃣ Model Building

Implemented:

### Linear Regression

Used as the baseline model.

### Random Forest Regressor

Improved prediction performance by learning non-linear relationships within the dataset.

---

## 8️⃣ Hyperparameter Tuning

Optimized the Random Forest model using:

- RandomizedSearchCV
- Cross Validation

Tuned parameters included:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf

---

## 9️⃣ Model Evaluation

Compared models using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The tuned Random Forest model achieved the best overall performance.

---

## 🔟 Model Serialization

Saved the trained model using Joblib (`.pkl`) for deployment.

---

## 1️⃣1️⃣ Backend API

Developed a REST API using FastAPI.

Endpoints include:

### GET /

Returns the home page.

### POST /predict

Accepts user inputs and returns the predicted Mental Health Score.

---

## 1️⃣2️⃣ Frontend

Built an interactive frontend using:

- HTML
- CSS
- JavaScript

Users can:

- Enter required details
- Submit prediction requests
- View predicted Mental Health Score instantly

---

## 1️⃣3️⃣ Deployment

The application is deployed on **Render**.

Live Demo:

https://mental-health-score-predictor-u5yr.onrender.com/

---

# 📁 Project Structure

```
Mental_Health_Score/
│
├── main.py
├── Mental_Heath_Model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── Mental_Health_Score_Predictor.ipynb
└── dataset.csv
```

---

# 🎓 Machine Learning Concepts Implemented

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Skewness Handling
- Log Transformation
- Standard Scaling
- Ordinal Encoding
- One-Hot Encoding
- Scikit-learn Pipeline
- ColumnTransformer
- Train-Test Split
- Linear Regression
- Random Forest Regression
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- FastAPI
- Pydantic Validation
- REST API Development
- Deployment

---

# 📸 Application Preview

> Add screenshots of the Home Page and Prediction Result here.

---

# 📈 Future Improvements

- User Authentication
- Prediction History
- Dashboard & Analytics
- Explainable AI (SHAP/LIME)
- Docker Containerization
- CI/CD Pipeline
- AWS Deployment
- Model Monitoring

---

# 👨‍💻 Author

**Sarthak Rajvaidya**

GitHub:
https://github.com/Sarthak-Rajvaidya

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
# 🧠 Mental Health Score Predictor

## 📌 Project Overview

The **Mental Health Score Predictor** is an end-to-end Machine Learning project that predicts an individual's mental health score based on demographic, academic, lifestyle, and social media usage data.

The project demonstrates the complete ML lifecycle—from data preprocessing and model training to deploying the trained model through a FastAPI backend with a responsive web interface.

---

# 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Feature Engineering
- ⚙️ Scikit-learn Pipelines
- 🔄 ColumnTransformer-based Preprocessing
- 🌲 Random Forest Regression
- 🎯 Hyperparameter Tuning using RandomizedSearchCV
- 📈 Model Evaluation using R², MAE & RMSE
- 💾 Model Serialization using Joblib
- ⚡ FastAPI REST API
- 🛡️ Pydantic Input Validation
- 🌐 Interactive Frontend using HTML, CSS & JavaScript

---

# 🛠️ Tech Stack

### Machine Learning

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

### Backend

- FastAPI
- Pydantic
- Joblib
- Uvicorn

### Frontend

- HTML5
- CSS3
- JavaScript

---

# 📂 Project Workflow

## ✅ 1. Data Loading

- Imported required libraries
- Loaded the dataset
- Checked shape and feature types
- Inspected sample records

---

## ✅ 2. Exploratory Data Analysis

Performed detailed EDA including:

- Distribution of Mental Health Score
- Stress Level vs Mental Health Score
- Correlation Heatmap
- Outlier Detection (IQR)
- Skewness Analysis
- Numerical Feature Analysis

---

## ✅ 3. Feature Engineering

- Categorized features into:
  - Skewed Numerical Features
  - Numerical Features
  - Ordinal Features
  - Nominal Features
- Grouped countries into top countries and "Other"

---

## ✅ 4. Data Preprocessing

Created reusable preprocessing pipelines using Scikit-learn:

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

## ✅ 5. ColumnTransformer

Implemented ColumnTransformer to combine multiple preprocessing pipelines into a single reusable preprocessing workflow.

---

## ✅ 6. Train-Test Split

Split the dataset into training and testing sets using `train_test_split()`.

---

## ✅ 7. Baseline Model

Implemented Linear Regression as the baseline model.

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)

---

## ✅ 8. Random Forest Regression

Implemented Random Forest Regressor.

Compared with Linear Regression using:

- Training R²
- Testing R²
- MAE

---

## ✅ 9. Hyperparameter Tuning

Optimized Random Forest using `RandomizedSearchCV`.

Tuned Parameters:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf

---

## ✅ 10. Model Evaluation

Compared all models using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## ✅ 11. Model Serialization

Saved the best-performing model using Joblib for deployment.

```
Mental_Health_Model.pkl
```

---

## ✅ 12. FastAPI Backend

Built REST APIs for prediction.

### Endpoints

```
GET /
```

Returns a welcome message.

```
POST /predict
```

Accepts student information and returns the predicted Mental Health Score.

---

## ✅ 13. Pydantic Validation

Validated incoming request data using Pydantic models.

Validation includes:

- Numeric ranges
- Required fields
- Categorical value constraints using Literal
- Automatic request validation

---

## ✅ 14. Frontend

Built a responsive frontend using:

- HTML
- CSS
- JavaScript

Features:

- User-friendly input form
- Sends POST request to FastAPI
- Displays predicted Mental Health Score
- Responsive design

---

# 📁 Project Structure

```text
Mental-Health-Score-Predictor/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
├── Mental_Health_Model.pkl
├── Mental_Health_Score_Predictor.ipynb
├── dataset.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Evaluation Metrics

- R² Score
- MAE
- RMSE

---

# 🚀 Future Improvements

- Docker Containerization
- Cloud Deployment (Render / Railway / AWS)
- CI/CD Pipeline
- User Authentication
- Prediction History
- Database Integration
- Model Monitoring
- Explainable AI (SHAP)

---

# 📷 Application Flow

```
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
FastAPI Backend
   │
   ▼
Pydantic Validation
   │
   ▼
Preprocessing Pipeline
   │
   ▼
Random Forest Model
   │
   ▼
Predicted Mental Health Score
```

---

# 📈 Current Status

🟢 **Completed**

- ✅ End-to-End Machine Learning Pipeline
- ✅ Model Training & Evaluation
- ✅ Hyperparameter Tuning
- ✅ Model Serialization
- ✅ FastAPI Backend
- ✅ Pydantic Validation
- ✅ Frontend Integration

---

## 👨‍💻 Author

**Sarthak Rajvaidya**

B.Tech Computer Engineering | AI & Software Engineering Enthusiast

Building production-ready AI applications using Machine Learning, FastAPI, and modern web technologies.
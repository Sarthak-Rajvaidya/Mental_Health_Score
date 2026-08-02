# 🧠 Mental Health Score Predictor

## 📌 Project Overview

This project predicts an individual's **Mental Health Score** using Machine Learning techniques. It follows a complete end-to-end Machine Learning workflow, covering data exploration, feature engineering, preprocessing, model training, hyperparameter tuning, model evaluation, serialization, and deployment.

The goal is to build a production-ready machine learning pipeline capable of predicting mental health scores based on demographic, academic, lifestyle, and social media usage features.

---

# 🎯 Objectives

* Perform Exploratory Data Analysis (EDA)
* Understand relationships between features and the target variable
* Detect outliers and analyze feature distributions
* Engineer meaningful features for machine learning
* Build reusable preprocessing pipelines
* Compare multiple regression algorithms
* Optimize model performance using hyperparameter tuning
* Evaluate models using regression metrics
* Serialize the final trained model
* Deploy the model using FastAPI

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

## Development Environment

* Google Colab
* Jupyter Notebook
* Git & GitHub

---

# 📂 Project Workflow

## ✅ 1. Data Loading

* Imported required libraries
* Loaded the dataset
* Explored dataset dimensions
* Verified data types
* Inspected sample records

---

## ✅ 2. Exploratory Data Analysis (EDA)

Performed comprehensive exploratory analysis including:

* Target variable distribution
* Stress Level vs Mental Health Score analysis
* Correlation Heatmap
* Outlier Detection using IQR
* Skewness Analysis
* Numerical Feature Analysis

---

## ✅ 3. Feature Engineering

* Identified skewed numerical features
* Grouped numerical features
* Categorized ordinal features
* Categorized nominal features
* Prepared feature lists for preprocessing

---

## ✅ 4. Data Preprocessing

Implemented modular preprocessing pipelines using Scikit-learn.

### Skewed Features

* Log Transformation
* Standard Scaling

### Numerical Features

* Standard Scaling

### Ordinal Features

* Ordinal Encoding

### Nominal Features

* One-Hot Encoding

---

## ✅ 5. ColumnTransformer

Combined all preprocessing pipelines using **ColumnTransformer**.

Benefits:

* Cleaner code
* Modular preprocessing
* Automatic feature transformation
* Production-ready preprocessing workflow

---

## ✅ 6. Train-Test Split

Prepared the dataset for machine learning by splitting it into:

* Training Dataset
* Testing Dataset

using Scikit-learn's `train_test_split()`.

---

## ✅ 7. Baseline Model

### Linear Regression

Implemented the baseline regression model using a Scikit-learn Pipeline.

Evaluation Metrics:

* R² Score
* Mean Absolute Error (MAE)

---

## ✅ 8. Advanced Model

### Random Forest Regressor

Implemented a Random Forest regression model integrated with the preprocessing pipeline.

Advantages:

* Captures non-linear relationships
* Handles feature interactions
* More robust than Linear Regression
* Better performance on structured tabular data

---

## ✅ 9. Hyperparameter Tuning

Optimized the Random Forest model using **RandomizedSearchCV**.

Tuned Parameters:

* n_estimators
* max_depth
* min_samples_split
* min_samples_leaf

Cross Validation:

* 5-Fold Cross Validation

Optimization Metric:

* R² Score

---

## ✅ 10. Model Evaluation

Compared multiple regression models using:

* R² Score
* Training R²
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

Models Compared:

* Linear Regression
* Random Forest (Default)
* Random Forest (Hyperparameter Tuned)

Selected the best-performing model based on overall evaluation metrics.

---

## ✅ 11. Model Serialization

Saved the final trained machine learning pipeline as a `.pkl` file using Pickle.

The serialized model contains:

* Complete preprocessing pipeline
* Encoders
* Scalers
* ColumnTransformer
* Tuned Random Forest model

This allows the model to be loaded directly during deployment without retraining.

---

# 📊 Evaluation Metrics

Regression metrics used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

# 📁 Project Structure

```text
Mental-Health-Score-Predictor/
│
├── Mental_Health_Score_Predictor.ipynb
├── mental_health_model.pkl
├── dataset.csv
├── README.md
└── .gitignore
```

---

# 🚀 Upcoming Work

* Build FastAPI backend
* Create API endpoints for prediction
* Validate requests using Pydantic
* Connect frontend with FastAPI
* Deploy the application
* Improve UI/UX
* Containerize using Docker (Optional)
* Deploy on Render/Railway/AWS

---

# 📈 Current Project Status

**Status:** 🟢 Machine Learning Phase Completed

### ✅ Completed

* Data Loading
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Data Preprocessing
* Scikit-learn Pipelines
* ColumnTransformer
* Train-Test Split
* Linear Regression Baseline
* Random Forest Regressor
* Hyperparameter Tuning
* Model Evaluation
* Model Comparison
* Model Serialization (.pkl)

---

## 🎯 Next Milestone

**FastAPI Backend Development**

Upcoming tasks include:

* Building REST APIs
* Request validation using Pydantic
* Loading the serialized model
* Serving real-time predictions
* Frontend integration
* Cloud deployment

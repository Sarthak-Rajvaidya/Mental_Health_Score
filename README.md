# 🧠 Mental Health Score Predictor

## 📌 Project Overview

This project predicts an individual's **Mental Health Score** using Machine Learning techniques. It follows a complete end-to-end Machine Learning workflow, covering data exploration, feature engineering, preprocessing, model building, evaluation, and deployment.

The primary objective is to build a production-ready ML pipeline capable of accurately predicting mental health scores based on demographic, academic, and lifestyle-related features.

---

# 🎯 Objectives

* Perform Exploratory Data Analysis (EDA)
* Understand relationships between features and the target variable
* Detect outliers and analyze feature distributions
* Engineer meaningful features for model training
* Build reusable preprocessing pipelines
* Train and evaluate baseline machine learning models
* Compare different regression algorithms
* Deploy the trained model using Flask

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

### Development Environment

* Jupyter Notebook
* Google Colab

---

# 📂 Project Workflow

## ✅ 1. Data Loading

* Imported required libraries
* Loaded the dataset
* Explored dataset dimensions
* Inspected sample records
* Verified feature data types

---

## ✅ 2. Exploratory Data Analysis (EDA)

Performed comprehensive EDA including:

* Distribution of Mental Health Score
* Relationship between Stress Level and Mental Health Score
* Correlation Heatmap
* Outlier Detection using IQR
* Skewness Analysis
* Numerical Feature Analysis

---

## ✅ 3. Feature Engineering

* Categorized numerical and categorical features
* Identified skewed numerical columns
* Separated:

  * Skewed Features
  * Numerical Features
  * Ordinal Features
  * Nominal Features

---

## ✅ 4. Data Preprocessing

Implemented preprocessing using Scikit-learn Pipelines.

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

Built a centralized preprocessing pipeline using `ColumnTransformer` to apply different preprocessing techniques to different feature groups.

This ensures:

* Cleaner code
* Reusable preprocessing
* Consistent transformations
* Production-ready workflow

---

## ✅ 6. Train-Test Split

Prepared the dataset for model training by splitting it into:

* Training Set
* Testing Set

using Scikit-learn's `train_test_split()`.

---

## ✅ 7. Baseline Model

Implemented the first baseline regression model.

### Linear Regression

* Built using Scikit-learn Pipeline
* Integrated preprocessing and model training
* Generated predictions
* Evaluated using:

  * R² Score
  * Mean Absolute Error (MAE)

---

# 📊 Evaluation Metrics

Current metrics used:

* R² Score
* Mean Absolute Error (MAE)

Additional metrics will be added while comparing advanced models.

---

# 🚀 Upcoming Work

* Train Random Forest Regressor
* Compare multiple regression algorithms
* Hyperparameter Tuning
* Model Selection
* Save trained model using Pickle
* Build Flask API
* Deploy the complete application
* Create an interactive prediction interface

---

# 📁 Project Structure

```text
Mental-Health-Score-Predictor/
│
├── Mental_Health_Score_Predictor.ipynb
├── dataset.csv
├── README.md
└── .gitignore
```

---

# 📈 Current Project Status

**Status:** 🟢 In Progress

### Current Milestone

* ✅ Exploratory Data Analysis Completed
* ✅ Feature Engineering Completed
* ✅ Data Preprocessing Completed
* ✅ ColumnTransformer Implemented
* ✅ Train-Test Split Completed
* ✅ Baseline Linear Regression Model Completed

**Next Milestone:** Model Comparison using Random Forest and other regression algorithms.

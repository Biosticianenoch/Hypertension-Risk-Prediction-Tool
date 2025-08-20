# 🩺 Hypertension Prediction Project

This project applies **Data Science** and **Machine Learning** techniques to predict **Hypertension status** based on patient lifestyle, clinical, and demographic information.  
The workflow covers **data preprocessing, exploratory data analysis (EDA), feature engineering, model building, hyperparameter tuning, and evaluation** using multiple machine learning algorithms.

---

## 📌 Table of Contents
1. [Overview](#-overview)
2. [Dataset](#-dataset)
3. [Project Workflow](#-project-workflow)
   - [1. Data Loading & Cleaning](#1-data-loading--cleaning)
   - [2. Exploratory Data Analysis (EDA)](#2-exploratory-data-analysis-eda)
   - [3. Feature Engineering](#3-feature-engineering)
   - [4. Model Training](#4-model-training)
   - [5. Model Evaluation](#5-model-evaluation)
4. [Machine Learning Models](#-machine-learning-models)
5. [Results](#-results)
6. [Dependencies](#-dependencies)
7. [How to Run](#-how-to-run)
8. [Future Improvements](#-future-improvements)

---

## 🚀 Overview
Hypertension is one of the leading risk factors for cardiovascular diseases. Early prediction of hypertension risk helps clinicians and patients take preventive measures.  
This project builds multiple **classification models** to detect hypertension from patient data and compares their performance.

---

## 📂 Dataset
- **File:** `hypertension_dataset.csv`
- **Shape:** Rows × Columns *(after cleaning)*
- **Target Variable:** `has_hypertension` (1 = Yes, 0 = No)

### Example Features
- **Numerical:** age, bmi, cholesterol, blood_sugar, etc.  
- **Categorical:** bp_history, medication, family_history, exercise_level, smoking_status  

---

## 🛠 Project Workflow

### 1. Data Loading & Cleaning
- Loaded CSV using `pandas` and cleaned column names (`pyjanitor`).
- Checked data types, missing values, and duplicates.
- Dropped missing values and standardized data types.

### 2. Exploratory Data Analysis (EDA)
- **Univariate Analysis:** Histograms, KDE plots, boxplots.  
- **Categorical Distribution:** Count plots for smoking status, exercise level, etc.  
- **Bivariate Analysis:** Boxplots of features vs hypertension.  
- **Correlation Analysis:** Heatmap for numerical variables.  
- **Chi-square Tests:** Relationship between categorical features and target.

### 3. Feature Engineering
- Label encoding for categorical variables.  
- Split dataset into **training (80%)** and **testing (20%)** sets with stratification.  
- Applied **MinMax Scaling** for numerical features.  

### 4. Model Training
Implemented and tuned the following models:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machines (SVM)  
- XGBoost  
- K Nearest Neighbors (KNN)  
- Gradient Boosting Machines (GBM)  
- AdaBoost  
- Ensemble Models: Voting Classifier & Stacking Classifier  
- Stochastic Gradient Descent (SGD)

### 5. Model Evaluation
Each model was evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**
- **ROC Curve / AUC (where applicable)**

---

## 🤖 Machine Learning Models

| Algorithm | Description | Strengths |
|-----------|-------------|-----------|
| Logistic Regression | Baseline linear classifier | Simple, interpretable |
| Decision Tree | Tree-based split model | Easy visualization |
| Random Forest | Ensemble of decision trees | Reduces overfitting, robust |
| Support Vector Machine | Maximizes margin between classes | Good with high-dimensional data |
| XGBoost | Gradient boosting algorithm | High performance, handles imbalance |
| KNN | Distance-based classifier | Non-parametric, simple |
| Gradient Boosting | Sequential boosting | Effective with weak learners |
| AdaBoost | Adaptive boosting of decision stumps | Focuses on hard-to-classify cases |
| Voting Classifier | Soft-voting ensemble | Combines multiple learners |
| Stacking Classifier | Meta-learning approach | Boosts performance |
| SGD Classifier | Linear model with stochastic optimization | Efficient on large datasets |

---

## 📊 Results

- **Best Performing Models:**  
   - XGBoost  
   - Random Forest  
   - Gradient Boosting  
   - Stacking Classifier  

- **Metrics:**  
   - F1-Macro Score was emphasized due to possible class imbalance.  
   - Confusion matrices and ROC curves highlighted strengths in sensitivity (recall) vs precision trade-offs.

---

## 📦 Dependencies
Install the following Python libraries before running:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost pyjanitor

# 🏦 Loan Approval Prediction Model

This project uses machine learning to predict whether a loan application will be approved based on user data such as income, employment status, and credit history.

---

## 📊 Dataset Overview

Each row in the dataset represents a loan application with the following fields:

| Column              | Description                           |
|---------------------|---------------------------------------|
| Loan_ID             | Unique loan identifier                |
| Gender              | Male / Female                         |
| Married             | Applicant's marital status            |
| Dependents          | Number of dependents                  |
| Education           | Graduate / Not Graduate               |
| Self_Employed       | Yes / No                              |
| ApplicantIncome     | Income of the applicant               |
| CoapplicantIncome   | Income of the co-applicant            |
| LoanAmount          | Loan amount requested (in thousands)  |
| Loan_Amount_Term    | Term of loan (in days)                |
| Credit_History      | 1 (good), 0 (poor), NaN (unknown)     |
| Property_Area       | Urban / Semiurban / Rural             |
| Loan_Status         | ✅ Y (Approved), ❌ N (Rejected)       |

---

## 🎯 Problem Statement

Given an applicant's profile, predict whether their **loan will be approved** (`Loan_Status`).

**Type**: Binary Classification  
**Target**: `Loan_Status`

---

## ⚙️ Models Used

Multiple models were tested using `scikit-learn`:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest ✅ (best performer)
- K-Nearest Neighbors
- Naive Bayes

> Final model: **Random Forest Classifier** – selected based on best accuracy.

---

## 🧠 Skills & Tools Practiced

- Data Preprocessing (handling missing values, encoding)
- Feature Engineering
- Train-Test Split
- Model Training and Evaluation
- Accuracy Score and Confusion Matrix
- Data Visualization

**Libraries**:
- `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

---
loan-prediction/
├── load.py                      # Streamlit web app
├── Loan_prediction_model.sav    # Saved logistic regression model (using joblib or pickle)
├── loan_prediction.ipynb        # Jupyter notebook with full ML workflow
├── dataset.csv                  # Raw dataset for training
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation

# customer-churn-prediction
End-to-end customer churn prediction using data analysis and machine learning techniques.

# Customer Churn Prediction System

## Overview
This project focuses on analyzing customer behavior data to predict churn and identify key factors that influence customer retention. The goal is to build a clear, interpretable, and scalable data-driven pipeline that can support business decision-making.

The project follows an end-to-end workflow, from data exploration and preprocessing to model training, evaluation, and insight generation.

---

## Problem Statement
Customer churn is a critical challenge for subscription-based businesses. Retaining existing customers is often more cost-effective than acquiring new ones.  
This project aims to answer the following question:

**Which customers are more likely to churn, and what factors contribute most to that behavior?**

---

## Dataset
- **Name:** Telco Customer Churn Dataset  
- **Source:** Public dataset (Kaggle)  
- **Description:**  
  The dataset contains customer demographic information, account details, service usage patterns, and churn labels.

---

## Project Structure

churn-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
│
├── reports/
│   └── figures/
│
├── README.md
├── requirements.txt
└── .gitignore

---

## Methodology
1. Data cleaning and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature engineering  
4. Baseline model development  
5. Model improvement and evaluation  
6. Interpretation of results and insights  

---

## Models Used
- Logistic Regression (Baseline)
- Random Forest Classifier

---

## Evaluation Metrics
- Precision  
- Recall  
- F1-score  
- ROC-AUC  
- Confusion Matrix  

Accuracy alone is not considered sufficient due to potential class imbalance.

---

## Key Insights
- Customers with shorter tenure show higher churn risk  
- Month-to-month contracts are strongly correlated with churn  
- Lack of additional services increases churn probability  

---

## Tools & Technologies
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## Future Improvements
- Hyperparameter tuning  
- Model explainability (e.g. SHAP)  
- Deployment as a simple API  

---

## Author
Developed as a learning-focused, portfolio-ready project to demonstrate data analysis and machine learning fundamentals.

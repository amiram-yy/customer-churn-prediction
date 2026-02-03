# Customer Churn Prediction

An end-to-end machine learning project focused on predicting customer churn using structured customer data.  
The project covers the full pipeline from data preprocessing and feature engineering to model training, evaluation, and visualization.

---

## 📌 Project Overview

Customer churn prediction is a common business problem where the goal is to identify customers who are likely to stop using a service.  
This project demonstrates how classical machine learning models can be used to analyze customer behavior and build predictive models in a clean and reproducible way.

---

## 🗂️ Project Structure

	├── data/
	│   ├── raw/
	│   └── processed/
	├── notebooks/
	│   ├── 01_eda.ipynb
	│   ├── 02_preprocessing.ipynb
	│   └── 03_modeling.ipynb
	├── src/
	│   ├── config.py
	│   ├── preprocessing.py
	│   ├── features.py
	│   ├── train.py
	│   ├── evaluate.py
	│   └── utils.py
	├── requirements.txt
	└── README.md

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 🔄 Workflow

1. Exploratory Data Analysis (EDA)
2. Data cleaning and preprocessing
3. Feature engineering
4. Model training (Logistic Regression, Random Forest)
5. Model evaluation and comparison
6. Visualization of results

---

## 📊 Model Evaluation

Models are evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Random Forest and Logistic Regression are used as baseline models, with performance compared using confusion matrices and ROC curves.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>

2.	Install dependencies:
	```bash
	pip install -r requirements.txt

4.	Run notebooks in order:
	```bash
	•	01_eda.ipynb
	•	02_preprocessing.ipynb
	•	03_modeling.ipynb

 ---

 ## 🫵🏻 Medium (More Details)

	https://medium.com/@amirrezagholizadeh642/customer-churn-prediction-using-machine-learning-c13f95d3dcfa

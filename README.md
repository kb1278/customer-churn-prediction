# 📊 Customer Churn Prediction using RFM Analysis

## 🧠 Project Overview

This project analyzes online retail customer behavior using RFM (Recency, Frequency, Monetary) analysis and machine learning models to predict customer churn.

The objective is to identify customers who are likely to stop purchasing and understand the key behavioral factors behind churn.

---

## 📁 Dataset

Dataset used: Online Retail II Dataset

The dataset contains:

- Invoice numbers
- Product details
- Quantity purchased
- Invoice dates
- Product prices
- Customer IDs
- Country information

---

## 🎯 Objectives

- Perform customer segmentation using RFM analysis
- Identify customer churn behavior
- Build machine learning models for churn prediction
- Evaluate model performance
- Analyze key drivers of churn

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed missing customer IDs
- Handled missing product descriptions
- Filtered invalid transactions
- Created total purchase value feature
- Converted date columns to datetime format

---

## 📊 RFM Feature Engineering

The following customer metrics were calculated:

- **Recency** → Days since last purchase
- **Frequency** → Number of purchases
- **Monetary** → Total customer spending

Initial churn definition:

- Customers with Recency greater than 90 days were labeled as churned.

---

## 📉 Exploratory Data Analysis

Key insights:

- Most customers are recently active
- Revenue is highly skewed
- High-frequency customers tend to spend more
- Higher recency is associated with lower spending

Visualizations included:

- Histograms
- Scatter plots
- Correlation heatmap
- Confusion matrix
- Feature importance chart

---

## 🤖 Machine Learning Models

### Logistic Regression

A baseline Logistic Regression model was trained using RFM features.

The model achieved near-perfect accuracy due to target leakage because churn was directly derived from Recency.

### Random Forest Classifier

A more realistic time-based churn prediction approach was implemented using:

- Frequency
- Monetary

This model produced more realistic churn predictions.

---

## 📈 Model Results

### Random Forest Performance

- Accuracy: ~0.58
- Moderate precision and recall
- More realistic than the baseline model

### Feature Importance

Most important churn predictors:

1. Monetary value
2. Frequency

---

## 📌 Business Insights

- High-value customers are critical to retain
- Low-frequency customers are more likely to churn
- Customer engagement strongly impacts retention
- Spending behavior is a strong churn indicator

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---



---

## 🚀 Future Improvements

- Add XGBoost or LightGBM models
- Use ROC-AUC evaluation metrics
- Build interactive dashboards
- Deploy as a Streamlit app

---

## 👤 Author

Kulwinder Bhamra

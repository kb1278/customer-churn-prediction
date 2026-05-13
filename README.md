📊 Customer Churn Prediction using RFM Analysis
🧠 Project Overview

This project analyzes online retail customer behavior using RFM (Recency, Frequency, Monetary) analysis and applies machine learning models to predict customer churn.

The goal is to identify customers who are likely to stop purchasing and understand the key behavioral factors behind churn.

📁 Dataset

The dataset used is the Online Retail II dataset, which contains transactional data of an online retail store including:

Invoice number
Product details
Quantity
Invoice date
Price
Customer ID
Country
🎯 Objective
Perform customer segmentation using RFM analysis
Define and identify customer churn
Build predictive models for churn classification
Evaluate model performance using real-world methodology
Identify key drivers of churn behavior
🧹 Data Preprocessing
Removed missing Customer IDs
Handled missing product descriptions
Filtered invalid transactions (Quantity ≤ 0, Price ≤ 0)
Created total purchase value (TotalPrice)
Converted date fields to datetime format
📊 RFM Feature Engineering

For each customer, the following features were computed:

Recency → Days since last purchase
Frequency → Number of unique purchases
Monetary → Total spending

Churn definition (baseline approach):

Customers with Recency > 90 days were labeled as churned.

📉 Exploratory Data Analysis (EDA)

Key insights:

Most customers are recently active
Revenue is highly skewed (few customers contribute most revenue)
Strong relationship between frequency and monetary value
Higher recency is associated with lower spending

Visualizations include:

Histograms (Recency, Frequency, Monetary)
Scatter plots (feature relationships)
Correlation heatmap
🤖 Machine Learning Models
1. Logistic Regression (Baseline Model)
Used RFM features as inputs
Achieved near-perfect accuracy due to target leakage
Highlighted importance of proper feature-target separation
2. Time-Based Churn Modeling (Improved Approach)

To simulate a real-world scenario:

Dataset split based on time
Churn defined using future customer activity
Prevented data leakage
3. Random Forest Classifier

Final model used:

Features: Frequency, Monetary
Target: Future-based churn label
📈 Model Evaluation
Random Forest Results
Accuracy: ~0.58
Moderate precision and recall
More realistic performance compared to baseline model
Confusion Matrix

The model shows:

Reasonable churn detection capability
Some misclassification between churned and active customers
🔍 Feature Importance

Most important features for churn prediction:

Monetary Value (dominant factor)
Frequency

Insight:

High-value customers behave differently and are key drivers of churn prediction.

⚠️ Key Insight: Target Leakage

The initial Logistic Regression model showed artificially perfect accuracy because:

Churn was directly derived from Recency
Recency was also used as an input feature

This led to target leakage, which was corrected in the improved model.

📌 Business Insights
High-value customers are the most critical segment to retain
Low-frequency customers are more likely to churn
Engagement and repeat purchases strongly influence retention
Monetary behavior is the strongest predictor of churn
🛠️ Tech Stack
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
🚀 How to Run This Project
git clone https://github.com/yourusername/churn-rfm-analysis.git
cd churn-rfm-analysis
pip install -r requirements.txt

Run the notebook:

jupyter notebook
📊 Project Structure
├── data/
├── notebooks/
├── images/
├── churn_rfm_analysis.ipynb
├── README.md

📌 Future Improvements
Add XGBoost / LightGBM models
Use ROC-AUC for better evaluation
Try clustering-based customer segmentation
Deploy model as a dashboard (Streamlit)

👤 Author
Kulwinder Bhamra
Data Science & Machine Learning Enthusiast

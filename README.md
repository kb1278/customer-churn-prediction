# 📊 Customer Churn Prediction Using RFM Analysis

## 🧠 Project Overview

This project analyses online retail customer purchasing behaviour using RFM (Recency, Frequency, Monetary) analysis and machine learning techniques to predict customer churn.

The project combines exploratory data analysis, feature engineering, predictive modelling, and an interactive Streamlit dashboard to identify customers at risk of churn and provide actionable business insights for customer retention strategies.

---

## 📁 Dataset

**Dataset:** Online Retail II Dataset

The dataset contains transactional records from an online retailer, including:

- Invoice numbers
- Product information
- Quantities purchased
- Transaction dates
- Product prices
- Customer IDs
- Country information

The dataset contains over 500,000 retail transactions and thousands of unique customers.

---

## 🎯 Project Objectives

- Analyse customer purchasing behaviour using RFM metrics
- Identify characteristics of customers likely to churn
- Build machine learning models to predict churn risk
- Evaluate model performance using realistic validation methods
- Develop an interactive dashboard for customer churn prediction
- Generate business insights to support customer retention efforts

---

## 🧹 Data Preparation

The following preprocessing steps were performed:

- Removed records with missing customer IDs
- Filled missing product descriptions
- Filtered invalid transactions (negative quantities and prices)
- Created Total Purchase Value features
- Converted date fields into datetime format
- Prepared customer-level datasets for RFM analysis

---

## 📊 RFM Feature Engineering

Customer behaviour was summarised using three key metrics:

### Recency
Number of days since the customer's most recent purchase.

### Frequency
Number of unique purchases made by each customer.

### Monetary
Total amount spent by each customer.
These metrics provide a concise representation of customer engagement and value.

---

## 📈 Exploratory Data Analysis

Several visualisations were created to understand customer behaviour patterns:

- Recency distribution
- Frequency distribution
- Monetary distribution
- Correlation heatmap
- Frequency vs Monetary scatter plot
- Recency vs Monetary scatter plot
- Confusion matrix
- Feature importance analysis

### Key Findings

- Most customers remained recently active.
- Customer spending was highly skewed, with a small number of customers contributing a large proportion of revenue.
- Customers purchasing more frequently generally spent more overall.
- Spending behaviour varied considerably across customer segments.

---

## 🤖 Machine Learning Models

### Logistic Regression (Baseline)

A Logistic Regression model was initially trained using Recency, Frequency, and Monetary features.

The model achieved near-perfect accuracy because churn labels were directly derived from Recency, creating target leakage and unrealistic performance estimates.

### Random Forest Classifier (Improved Approach)

To create a more realistic prediction framework:

- The dataset was split chronologically using transaction dates
- Customer activity occurring after the training period was used to define churn
- A time-based validation approach was implemented
- Frequency and Monetary variables were used to predict future customer activity

This approach better reflects real-world customer churn prediction scenarios.

---

## 📉 Model Performance

### Random Forest Results

| Metric | Value |
|---|---:|
| Accuracy | ~63% |
| ROC-AUC | 0.671 |
| Validation Method | Time-Based Split |
| Features Used | Frequency, Monetary |

The Random Forest model achieved a ROC-AUC score of **0.671**, indicating a moderate ability to distinguish between customers likely to churn and those likely to remain active.

The model was evaluated using a chronological validation approach, providing a more realistic estimate of performance on future customer behaviour.

---

## 🔍 Feature Importance

Feature importance analysis identified the most influential predictors of customer churn:

1. **Monetary Value**
2. **Purchase Frequency**

### Business Interpretation

- Higher-spending customers exhibited different churn patterns compared with lower-value customers
- Customers purchasing less frequently were generally more likely to churn
- Customer value and engagement were strong indicators of future purchasing behaviour

---

## 🌐 Interactive Streamlit Dashboard

An interactive Streamlit application was developed to make churn predictions accessible through a simple user interface.

### Dashboard Features

- churn prediction
- Customer purchase frequency input
- Customer spending value input
- Churn probability estimation
- Risk classification (High Risk / Low Risk)
- Machine learning model integration using a trained Random Forest classifier

The application loads a saved machine learning model (`rf_model.pkl`) and generates predictions instantly based on user inputs.

---





## 📸 Dashboard Preview

<img width="1140" height="614" alt="Screenshot 2026-05-25 002058" src="https://github.com/user-attachments/assets/3456e4c4-590e-4960-b8ab-e885b513ffb3" />




---
## 🚀 Running the Streamlit Application

### 1. Clone the repository

```bash
git clone https://github.com/kb1278/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install required packages

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib
```

### 3. Run the application

```bash
streamlit run app.py
```

### 4. Open in your browser

```text
http://localhost:8501

```



## 📽️ Presentation

A PowerPoint slide deck was created to communicate insights to a non-technical audience.

 📎 File: `Customer Churn.pptx`

---

## 🛠️ Technologies Used

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualisation
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Logistic Regression
- Random Forest Classifier

### Deployment
- Streamlit
- Joblib

### Development Environment
- Jupyter Notebook
- Git
- GitHub



---

## 💡 Business Recommendations

Based on the analysis:

- Prioritise retention efforts for high-value customers
- Monitor customers with declining purchase frequency
- Implement targeted marketing campaigns for at-risk customer segments
- Develop loyalty initiatives to encourage repeat purchases
- Use predictive models proactively to identify churn risk before customer disengagement occurs

---

## 🚀 Future Improvements

- Deploy the dashboard using Streamlit Community Cloud
- Experiment with XGBoost and LightGBM models
- Incorporate additional behavioural features
- Add customer segmentation visualisations to the dashboard
- Build a full business intelligence dashboard in Power BI

---



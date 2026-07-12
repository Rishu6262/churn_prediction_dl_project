# 🏦 Customer Churn Prediction Using Machine Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 🌐 Live Demo

### 🚀 Try the Application

https://churnpredictionp19-evkjk4fzrarzujckjevh9h.streamlit.app/

---

# 📖 Table of Contents

- Project Overview
- Problem Statement
- Why This Project?
- Business Use Case
- Project Objectives
- Dataset Information
- Feature Description
- Technology Stack
- Project Structure
- Project Workflow
- Exploratory Data Analysis
- Data Preprocessing
- Feature Engineering
- Machine Learning Models
- Model Evaluation
- Streamlit Application
- Installation Guide
- Requirements
- Results
- Learning Outcomes
- Future Improvements
- Conclusion
- Author
- License

---

# 📌 Project Overview

Customer churn prediction is one of the most important applications of Machine Learning in the banking industry. Financial institutions continuously lose customers due to competition, poor customer satisfaction, better offers from competitors, and changing customer needs.

Understanding which customers are likely to leave allows banks to take preventive actions before the customer actually closes their account.

This project builds an intelligent Machine Learning model capable of predicting whether a customer will churn based on demographic information, banking history, and financial behavior.

The prediction system is deployed as an interactive Streamlit web application where users can enter customer details and instantly receive a churn prediction along with the prediction probability.

The complete project follows the end-to-end Machine Learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, model selection, deployment, and testing.

---

# ❓ Problem Statement

Customer retention is one of the biggest challenges for banks.

Acquiring a new customer is significantly more expensive than retaining an existing one. If organizations can identify customers who are at risk of leaving, they can provide personalized offers, discounts, better customer support, or financial advice to improve customer satisfaction.

The objective of this project is to develop a Machine Learning classification model capable of identifying customers who are likely to leave the bank.

The final model helps support data-driven business decisions by predicting customer churn before it occurs.

---

# 💡 Why I Chose This Project

I selected this project because customer churn prediction is a practical Machine Learning problem with significant real-world business value.

Through this project, I wanted to strengthen my understanding of:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Classification Algorithms
- Model Evaluation
- Streamlit Deployment
- End-to-End Machine Learning Workflow

This project also helped me understand how Machine Learning can assist businesses in improving customer retention and increasing profitability.

---

# 🏢 Business Use Case

Banks and financial institutions manage millions of customers every year.

Losing valuable customers directly affects business revenue and long-term growth.

Using Machine Learning predictions, banks can:

- Identify high-risk customers.
- Improve customer satisfaction.
- Reduce customer churn.
- Increase customer loyalty.
- Design personalized retention campaigns.
- Improve business decision-making.
- Reduce customer acquisition costs.
- Increase long-term profitability.

Customer churn prediction has become an essential business intelligence application in the banking sector.

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Predict whether a customer will leave the bank.
- Analyze important customer attributes affecting churn.
- Perform comprehensive Exploratory Data Analysis.
- Clean and preprocess customer data.
- Train multiple Machine Learning classification models.
- Compare different algorithms.
- Select the best-performing model.
- Deploy the model using Streamlit.
- Create an easy-to-use prediction interface.
- Demonstrate an end-to-end Machine Learning pipeline.

---

# 📊 Dataset Information

### Dataset Name

**Bank Customer Churn Dataset**

### Dataset Size

- Total Records: **10,000**
- Features: **10 Input Features**
- Target Variable: **Exited**

### Dataset Type

Structured CSV Dataset

### Problem Type

Binary Classification

### Target Classes

- 0 → Customer Stayed
- 1 → Customer Churned

The dataset contains demographic information, financial details, and customer account information used to train Machine Learning models for churn prediction.

---

# 📁 Dataset Features

| Feature | Description |
|----------|-------------|
| CreditScore | Customer credit score |
| Geography | Customer country |
| Gender | Male or Female |
| Age | Customer age |
| Tenure | Number of years with the bank |
| Balance | Current account balance |
| NumOfProducts | Banking products owned |
| HasCrCard | Credit card holder |
| IsActiveMember | Customer activity status |
| EstimatedSalary | Estimated annual salary |
| Exited | Target variable |

---

# 🔍 Feature Description

### Credit Score

Represents the customer's creditworthiness and financial reliability.

Higher credit scores generally indicate better financial stability.

### Geography

Indicates the country where the customer belongs.

Different regions may show different churn behaviors due to market conditions.

### Gender

Represents the customer's gender.

It helps determine whether customer behavior differs across demographic groups.

### Age

Customer age is one of the most important predictors.

Older and younger customers often exhibit different banking behaviors.

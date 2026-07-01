# 🏦 Customer Churn Prediction Using Machine Learning

---

## 🔗 Live Demo

**Try the Application Here:**
https://churnpredictionp19-evkjk4fzrarzujckjevh9h.streamlit.app/

---

# 📌 Project Overview

Customer churn is one of the biggest challenges faced by banks and businesses. Losing existing customers can significantly impact revenue and growth. This project uses Machine Learning to predict whether a customer is likely to leave the bank based on demographic, financial, and account-related information.

The application analyzes customer characteristics such as credit score, age, geography, account balance, tenure, number of products, and account activity to predict churn. This helps businesses identify high-risk customers and take proactive retention measures.

---

# ❓ Why I Chose This Project?

Customer retention is more cost-effective than acquiring new customers. I selected this project to:

* Understand customer behavior using data.
* Learn classification algorithms.
* Improve data preprocessing and feature engineering skills.
* Build a real-world business prediction system.
* Gain hands-on experience with Machine Learning deployment.

This project enhanced my practical understanding of predictive analytics and business intelligence.

---

# 🚀 Project Objectives

* Predict whether a customer will churn.
* Analyze factors affecting customer retention.
* Perform Exploratory Data Analysis (EDA).
* Compare multiple Machine Learning classification models.
* Select the best-performing model.
* Deploy the model using Streamlit.

---

# 📊 Dataset Information

### Dataset Name

**Bank Customer Churn Dataset**

### Dataset Size

* 10,000 Customer Records

### Features

| Feature         | Description                               |
| --------------- | ----------------------------------------- |
| Credit Score    | Customer Credit Score                     |
| Geography       | Customer Country                          |
| Gender          | Male/Female                               |
| Age             | Customer Age                              |
| Tenure          | Years with Bank                           |
| Balance         | Bank Account Balance                      |
| NumOfProducts   | Number of Products                        |
| HasCrCard       | Credit Card Holder                        |
| IsActiveMember  | Active Customer Status                    |
| EstimatedSalary | Estimated Salary                          |
| Exited          | Target Variable (0 = Stayed, 1 = Churned) |

---

# 🔍 Understanding the Features

### Credit Score

Represents the customer's creditworthiness.

### Geography

Country where the customer belongs.

### Age

Customer's current age.

### Tenure

Number of years the customer has been associated with the bank.

### Balance

Current bank account balance.

### Number of Products

Total banking products used by the customer.

### Credit Card

Indicates whether the customer owns a credit card.

### Active Member

Shows whether the customer actively uses banking services.

### Estimated Salary

Estimated annual salary of the customer.

### Exited

Target variable indicating customer churn.

---

# 🛠 Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

## Machine Learning

* Classification Algorithms
* Feature Engineering
* Model Evaluation

---

# 📂 Project Structure

```bash
Customer_Churn_Prediction/

│
├── app.py
├── model.pkl
├── Churn_Modelling.csv
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
└── assets/
    └── screenshots/
```

---

# 🔎 Exploratory Data Analysis (EDA)

The following analyses were performed:

### Data Inspection

* Dataset Shape
* Data Types
* Missing Values
* Duplicate Records

### Statistical Analysis

* Summary Statistics
* Correlation Analysis
* Customer Distribution

### Visualizations

* Churn Distribution
* Age Distribution
* Credit Score Distribution
* Geography-wise Customers
* Correlation Heatmap
* Box Plots
* Count Plots

---

# 📈 Data Preprocessing

The following preprocessing steps were applied:

### Data Cleaning

* Checked Missing Values
* Removed Duplicates

### Feature Encoding

Categorical variables were encoded into numerical values.

### Feature Scaling

Numerical features were standardized before training.

### Train-Test Split

```python
train_test_split()
```

Dataset divided into training and testing sets.

---

# 🤖 Machine Learning Models Used

## Logistic Regression

* Fast and Interpretable
* Strong Baseline Model

---

## Decision Tree Classifier

* Captures Nonlinear Relationships
* Easy to Interpret

---

## Random Forest Classifier

* High Accuracy
* Reduced Overfitting
* Better Generalization

---

## K-Nearest Neighbors (KNN)

* Instance-Based Learning
* Effective for Small to Medium Datasets

---

# ⚙️ Model Training

Training Workflow:

1. Load Dataset
2. Data Cleaning
3. Perform EDA
4. Feature Engineering
5. Encode Categorical Variables
6. Split Dataset
7. Train Multiple Models
8. Evaluate Performance
9. Save Best Model

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* ROC-AUC Score

---

# 🏆 Best Model Selection

The best model was selected based on:

* Highest Accuracy
* Highest Precision
* Highest Recall
* Best F1 Score
* Better Generalization

Models Compared:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors

---

# 💻 Streamlit Web Application

A simple and interactive Streamlit application was developed.

### User Inputs

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Active Member
* Estimated Salary

### Output

* Customer Churn Prediction
* Churn Probability

The prediction is generated instantly using the trained Machine Learning model.

---

# ▶️ Installation Guide

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

### Navigate to Project Folder

```bash
cd customer-churn-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Classification Modeling
* Model Evaluation
* Hyperparameter Tuning
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

# 🔮 Future Improvements

* Real-Time Banking Data Integration
* Deep Learning Models
* Explainable AI (SHAP/LIME)
* Customer Retention Recommendation System
* Interactive Analytics Dashboard
* Cloud Deployment

---

# 📜 Disclaimer

This project is developed for educational and research purposes only.

The predictions generated by the model are based on historical customer data and should not be considered business decisions without further analysis.

---

# ✅ Conclusion

The **Customer Churn Prediction System** demonstrates how Machine Learning can be used to identify customers who are likely to leave a bank by analyzing demographic and financial information. Through data preprocessing, exploratory data analysis, feature engineering, and the evaluation of multiple classification algorithms, the project successfully predicts customer churn with high accuracy. The Streamlit web application provides a simple and interactive interface for generating real-time predictions. Overall, this project showcases a complete end-to-end machine learning workflow and highlights the practical application of predictive analytics in customer relationship management. With future enhancements such as real-time data integration, explainable AI, and advanced deep learning models, the system can become a valuable decision-support tool for improving customer retention strategies.

---

# 👨‍💻 Author

**Rishu Gurjar**

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

## Technical Skills

* Python
* SQL
* Machine Learning
* Deep Learning
* Data Analysis
* Streamlit
* Power BI
* Scikit-Learn
* Git & GitHub

### Connect With Me

**LinkedIn:** https://www.linkedin.com/in/rishu-gurjar-58072a333

**GitHub:** https://github.com/Rishu6262

---

# 📜 License

This project is developed for educational, research, and learning purposes.

You are free to use, modify, and improve the project with proper attribution.

---

# ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.

Your support motivates future development and helps others discover the project.

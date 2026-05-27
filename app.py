import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_assets():
    model = load_model("model.h5", compile=False)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_assets()

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

.metric-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.predict-box {
    background: #111827;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">📊 Customer Churn Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered banking churn prediction using Deep Learning</div>', unsafe_allow_html=True)

# ---------------- INPUTS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    credit_score = st.number_input("Credit Score", 300, 900, 650)
    age = st.slider("Age", 18, 100, 35)
    tenure = st.slider("Tenure", 0, 10, 5)

with col2:
    balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
    estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])

with col3:
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    has_credit_card = st.selectbox("Has Credit Card", [0, 1])
    is_active_member = st.selectbox("Is Active Member", [0, 1])

# ---------------- ENCODING ----------------
gender_male = 1 if gender == "Male" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

input_data = np.array([[
    credit_score,
    age,
    tenure,
    balance,
    num_products,
    has_credit_card,
    is_active_member,
    estimated_salary,
    gender_male,
    geo_germany,
    geo_spain
]])

scaled_data = scaler.transform(input_data)

# ---------------- METRICS ----------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f'<div class="metric-card"><h3>{credit_score}</h3><p>Credit Score</p></div>', unsafe_allow_html=True)

with m2:
    st.markdown(f'<div class="metric-card"><h3>{age}</h3><p>Age</p></div>', unsafe_allow_html=True)

with m3:
    st.markdown(f'<div class="metric-card"><h3>{num_products}</h3><p>Products</p></div>', unsafe_allow_html=True)

with m4:
    st.markdown(f'<div class="metric-card"><h3>{geography}</h3><p>Region</p></div>', unsafe_allow_html=True)

st.write("")

# ---------------- PREDICTION ----------------
st.markdown('<div class="predict-box">', unsafe_allow_html=True)

if st.button("🔮 Predict Churn"):
    prediction = model.predict(scaled_data)
    probability = prediction[0][0]

    st.subheader("Prediction Result")

    if probability > 0.5:
        st.error(f"⚠️ High Churn Risk: {probability:.2%}")
    else:
        st.success(f"✅ Customer Likely to Stay: {(1-probability):.2%}")

    st.progress(float(probability))

st.markdown('</div>', unsafe_allow_html=True)

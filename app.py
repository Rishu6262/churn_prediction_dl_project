import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Customer Churn Predictor",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
@st.cache_resource
def load_assets():
    model = load_model("model.h5", compile=False)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    return model, scaler

model, scaler = load_assets()

# ---------------------------
# Background + Custom CSS
# ---------------------------
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1518770660439-4636190af475");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        .main-title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px cyan;
        }

        .sub-text {
            text-align: center;
            color: #dcdcdc;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .glass {
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(14px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        }

        .stButton > button {
            width: 100%;
            border-radius: 12px;
            height: 55px;
            border: none;
            font-size: 20px;
            font-weight: bold;
            color: white;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            box-shadow: 0px 4px 15px rgba(0,114,255,0.6);
            transition: 0.3s;
        }

        .stButton > button:hover {
            transform: scale(1.03);
            background: linear-gradient(90deg, #ff00cc, #3333ff);
        }

        section[data-testid="stSidebar"] {
            background: rgba(0, 0, 0, 0.65);
        }

        label {
            color: white !important;
            font-weight: bold !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# ---------------------------
# Title
# ---------------------------
st.markdown('<div class="main-title">🚀 AI Customer Churn Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Deep Learning Powered Banking Churn Prediction System</div>', unsafe_allow_html=True)

# ---------------------------
# Sidebar Inputs
# ---------------------------
st.sidebar.title("📊 Customer Details")

credit_score = st.sidebar.number_input("Credit Score", 300, 900, 650)

geography = st.sidebar.selectbox("Geography", ["France", "Germany", "Spain"])

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

age = st.sidebar.slider("Age", 18, 100, 35)

tenure = st.sidebar.slider("Tenure", 0, 10, 5)

balance = st.sidebar.number_input("Balance", 0.0, 300000.0, 50000.0)

num_products = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])

has_credit_card = st.sidebar.selectbox("Has Credit Card", [0, 1])

is_active_member = st.sidebar.selectbox("Active Member", [0, 1])

estimated_salary = st.sidebar.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

# ---------------------------
# Encoding
# ---------------------------
geo_france = 1 if geography == "France" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

gender_male = 1 if gender == "Male" else 0

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

# ---------------------------
# Main Layout
# ---------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("🧠 Predict Customer Churn")

    if st.button("🔮 Predict Now"):
        prediction = model.predict(scaled_data)
        probability = prediction[0][0]

        st.progress(float(probability))

        if probability > 0.5:
            st.error(f"⚠️ Customer likely to churn! Probability: {probability:.2%}")
        else:
            st.success(f"✅ Customer likely to stay! Probability: {(1-probability):.2%}")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=250
    )
    st.markdown("### 🤖 AI Banking Assistant")
    st.write("Predict customer retention using advanced deep learning models.")
    st.markdown("</div>", unsafe_allow_html=True)

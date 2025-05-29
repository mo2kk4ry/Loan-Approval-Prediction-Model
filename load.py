import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
model_filename = "loan_prediction_model.sav"
loan_prediction_model = pickle.load(open(model_filename, 'rb'))

# Function to take user input and process it
def user_input_features():
    # Streamlit form for user inputs
    st.sidebar.header("Input Features")
    
    Gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
    Married = st.sidebar.selectbox("Marital Status", ("Yes", "No"))
    Dependents = st.sidebar.selectbox("Number of Dependents", ("0", "1", "2", "3+"))
    Education = st.sidebar.selectbox("Education", ("Graduate", "Non-Graduate"))
    Self_Employed = st.sidebar.selectbox("Self Employed", ("Yes", "No"))
    ApplicantIncome = st.sidebar.number_input("Applicant Income", min_value=0, value=0)
    CoapplicantIncome = st.sidebar.number_input("Coapplicant Income", min_value=0, value=0)
    LoanAmount = st.sidebar.number_input("Loan Amount (in thousands)", min_value=0, value=0)
    Loan_Amount_Term = st.sidebar.slider("Loan Amount Term (months)", 12, 360, step=12)
    Credit_History = st.sidebar.selectbox("Credit History", ("Yes", "No"))
    Property_Area = st.sidebar.selectbox("Property Area", ("Urban", "Semiurban", "Rural"))
    
    # Feature processing
    Gender = 1 if Gender == "Male" else 0
    Married = 1 if Married == "Yes" else 0
    Dependents = 3 if Dependents == "3+" else int(Dependents)
    Education = 0 if Education == "Graduate" else 1
    Self_Employed = 1 if Self_Employed == "Yes" else 0
    Credit_History = 1 if Credit_History == "Yes" else 0
    Property_Area = {"Urban": 0, "Semiurban": 1, "Rural": 2}[Property_Area]
    LoanAmount_log = np.log(LoanAmount + 1)  # To avoid log(0)

    # Create a dictionary of inputs
    data = {
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area,
        "LoanAmount_log": LoanAmount_log,
    }
    
    # Convert to DataFrame
    features = pd.DataFrame([data])
    return features

# Streamlit app structure
st.title("Loan Prediction App")
st.write("This app predicts loan approval status based on user inputs.")

# Load user inputs
input_df = user_input_features()

# Show input features in the app
st.subheader("User Inputs")
st.write(input_df)

# Prediction
if st.button("Predict Loan Approval"):
    result = loan_prediction_model.predict(input_df)
    if result[0] == 1:
        st.success("Congratulations! The loan is likely to be approved.")
    else:
        st.error("Sorry, the loan is likely to be rejected.")

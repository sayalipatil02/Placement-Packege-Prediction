# import streamlit as st
# import joblib
# import numpy as np

# # Load trained model
# model = joblib.load("regression_model.joblib")

# # App title
# st.title("Package Prediction App")
# st.write("Enter your CGPA to predict the expected package.")

# # User input
# cgpa = st.number_input(
#     "Enter CGPA",
#     min_value=0.0,
#     max_value=10.0,
#     value=7.0,
#     step=0.1
# )

# # Predict button
# if st.button("Predict Package"):
#     input_data = np.array([[cgpa]])

#     prediction = model.predict(input_data)

#     st.success(f"Predicted Package: {prediction[0]:.2f} LPA")

import streamlit as st
import joblib
import numpy as np

# Load model
try:
    model = joblib.load("regression_model.joblib")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Title
st.title("Package Prediction App")
st.write("Enter your CGPA to predict the expected package.")

# Input
cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

# Prediction
if st.button("Predict Package"):
    input_data = np.array([[cgpa]])

    prediction = model.predict(input_data)

    predicted_value = float(np.array(prediction).flatten()[0])

    st.success(f"Predicted Package: {predicted_value:.2f} LPA")
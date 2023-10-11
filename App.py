import streamlit as st
import pickle

# Load the trained model
with open('trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app title and header
st.title('Churn Prediction Form')
st.write('Fill in the details and click the button to predict churn.')

# Form inputs
state = st.selectbox('State:', ['KS', 'OH', 'NY', 'Other'])  # Add more states
account_length = st.number_input('Account Length:')
area_code = st.number_input('Area Code:')
phone = st.text_input('Phone:')
intl_plan = st.selectbox('International Plan:', ['No', 'Yes'])
vmail_plan = st.selectbox('Voicemail Plan:', ['No', 'Yes'])
vmail_message = st.number_input('Voicemail Message:')
day_mins = st.number_input('Day Minutes:')

# Make predictions
if st.button('Predict Churn'):
    # Preprocess the input data and make a prediction
    intl_plan_val = 1 if intl_plan == 'Yes' else 0
    vmail_plan_val = 1 if vmail_plan == 'Yes' else 0
    preprocessed_data = [[account_length, area_code, intl_plan_val, vmail_plan_val, vmail_message, day_mins]]
    prediction = model.predict(preprocessed_data)

    # Display the prediction result
    result = "Churn Prediction: Yes" if prediction[0] == 1 else "Churn Prediction: No"
    st.write(result)

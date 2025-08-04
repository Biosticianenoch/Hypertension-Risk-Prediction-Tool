## Load the required data
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle
from PIL import Image
import os
import datetime
from sklearn.preprocessing import LabelEncoder

## Load the trained model
model = pickle.load(open("hypertension_xgb_model.sav", 'rb'))
## Visitor counter
counter_file = "heart_visitors.pkl"

if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {'count': 0, 'timestamps': []}

if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

## Sidebar menu
with st.sidebar:
    selected = option_menu("Navigation", 
        ["Welcome", "Prediction", "Recommendations", "Analytics", "FAQs", "Disclaimer", "Data Citation"],
        icons=['house', 'activity', 'lightbulb', 'bar-chart-line', 'question-circle', 'shield-lock', 'book'],
        menu_icon="cast", default_index=0)

## Welcome Page
if selected == "Welcome":
    st.markdown("<h1 style='color:#2c7be5;'>🩺 Hypertension Risk Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to the *Hypertension Risk Prediction App* — a powerful tool designed to help you assess your risk of developing high blood pressure using machine learning.

    ### What You Can Do:
    - 🔍 *Predict Your Risk*: Input health and lifestyle details to see your hypertension risk score.
    - 📋 *Get Recommendations*: Personalized advice based on your predicted risk.
    - ❓ *Learn More*: Explore FAQs to understand the app and hypertension better.
    - ⚠ *Disclaimer*: Read the ethical and professional limitations of this tool.

    """)

## Prediction Page
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center; color:#2c7be5;'>🧠 Predict Hypertension Risk</h2>", unsafe_allow_html=True)
    st.write("Please fill in the following medical and lifestyle information:")

    with st.form("hypertension_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=0, step=1)
            salt_intake = st.number_input("Salt Intake (grams/day)", min_value=0.0, step=0.1)
            stress_score = st.slider("Stress Score (1-10)", 1, 10, 5)
            sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, step=0.1)
            bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, step=0.1)

        with col2:
            bp_history = st.selectbox("Blood Pressure History", ['Normal', 'Prehypertension', 'Hypertension'])
            medication = st.selectbox("On Medication?", ['None', 'ACE Inhibitor', 'Other'])
            family_history = st.selectbox("Family History of Hypertension?", ['Yes', 'No'])
            exercise_level = st.selectbox("Exercise Level", ['Low', 'Moderate', 'High'])
            smoking_status = st.selectbox("Smoking Status", ['Smoker', 'Non-Smoker'])

        submitted = st.form_submit_button("🔍 Predict Hypertension Risk")

    if submitted:
        label_encoders = {
            "bp_history": LabelEncoder().fit(['Normal', 'Prehypertension', 'Hypertension']),
            "medication": LabelEncoder().fit(['None', 'ACE Inhibitor', 'Other']),
            "family_history": LabelEncoder().fit(['Yes', 'No']),
            "exercise_level": LabelEncoder().fit(['Low', 'Moderate', 'High']),
            "smoking_status": LabelEncoder().fit(['Smoker', 'Non-Smoker'])
        }

        input_features = [
            age,
            salt_intake,
            stress_score,
            label_encoders['bp_history'].transform([bp_history])[0],
            sleep_duration,
            bmi,
            label_encoders['medication'].transform([medication])[0],
            label_encoders['family_history'].transform([family_history])[0],
            label_encoders['exercise_level'].transform([exercise_level])[0],
            label_encoders['smoking_status'].transform([smoking_status])[0],
        ]

        input_array = np.array(input_features).reshape(1, -1)

        probability = model.predict_proba(input_array)[0][1]
        prediction = model.predict(input_array)[0]

        st.session_state['risk_score'] = probability
        st.session_state['risk_label'] = 'High' if probability >= 0.7 else 'Moderate' if probability >= 0.4 else 'Low'

        st.success(f"🧠 Estimated Risk of Hypertension: **{probability:.2%}**")

        if st.session_state['risk_label'] == 'High':
            st.error("🚨 High Risk! Immediate lifestyle changes and medical attention recommended.")
        elif st.session_state['risk_label'] == 'Moderate':
            st.warning("🟠 Moderate Risk. Consider adjusting your lifestyle.")
        else:
            st.success("🟢 Low Risk. Keep up the good lifestyle!")

## Recommendations Page
elif selected == "Recommendations":
    st.markdown("<h1 style='color:#2c7be5;'>💡 Personalized Recommendations</h1>", unsafe_allow_html=True)

    if 'risk_label' not in st.session_state:
        st.warning("⚠️ Please complete the prediction first to view personalized recommendations.")
    else:
        risk = st.session_state['risk_label']
        st.markdown(f"### 🧠 Based on your prediction, you are at **{risk} Risk** of Hypertension")

        if risk == 'High':
            st.error("🚨 **High Risk Recommendations**")
            st.markdown("""
            - 🧂 **Reduce Salt Intake**
            - 🧘‍♀️ **Manage Stress**
            - 🚶 **Exercise Regularly**
            - 🩺 **Consult a Healthcare Provider**
            - 🧾 **Monitor BP Frequently**
            - 🥗 **Adopt a Healthy Diet**
            """)
        elif risk == 'Moderate':
            st.warning("🟠 **Moderate Risk Recommendations**")
            st.markdown("""
            - 🍲 **Eat a Balanced Diet**
            - 🏃 **Stay Active**
            - 💨 **Avoid Smoking/Alcohol**
            - 😌 **Practice Relaxation**
            """)
        else:
            st.success("🟢 **Low Risk Maintenance Tips**")
            st.markdown("""
            - 🥗 **Maintain a Healthy Diet**
            - 🏃 **Continue Exercising**
            - 🛌 **Get Good Sleep**
            - 💧 **Stay Hydrated**
            - 📅 **Have Annual Checkups**
            """)

## Analytics Page
elif selected == "Analytics":
    st.markdown("<h1 style='color:#2c7be5;'>💡 Visitor Analytics</h1>", unsafe_allow_html=True)
    st.info(f"👥 *Total Visitors:* {visitor_data['count']}")
    if visitor_data['timestamps']:
        st.write("### 🕒 Visitor Log")
        st.dataframe(visitor_data['timestamps'])

## FAQs Page
elif selected == "FAQs":
    st.markdown(
        "<h1 style='color:#2c7be5;'> Frequently Asked Questions (FAQs)</h1>", 
        unsafe_allow_html=True
    )

    st.markdown("""
    Welcome to the FAQs section. Here you'll find answers to common questions about hypertension and how this app works.
    """)

    with st.expander("🔍 What is Hypertension?"):
        st.write("""
        Hypertension, or high blood pressure, is a chronic medical condition in which the blood pressure in the arteries is persistently elevated. 
        It increases the risk of heart disease, stroke, kidney problems, and other health issues if left untreated.
        """)

    with st.expander("📊 How accurate is the model?"):
        st.write("""
        Our model was trained on a reliable dataset and achieved strong performance metrics (e.g., accuracy, precision, recall). 
        However, this app is for informational purposes only and *should not be used as a substitute for professional medical advice or diagnosis*.
        """)

    with st.expander("🧠 What features are used to predict hypertension?"):
        st.write("""
        The model uses the following features:
        - Age
        - Salt Intake
        - Stress Score
        - Blood Pressure History
        - Sleep Duration
        - BMI (Body Mass Index)
        - Medication
        - Family History
        - Exercise Level
        - Smoking Status
        """)

    with st.expander("🩺 Can this app diagnose or treat hypertension?"):
        st.write("""
        No. This app is a *predictive tool only*. It cannot provide a clinical diagnosis or treatment plan. 
        If you are concerned about your blood pressure, please consult a qualified healthcare provider.
        """)

    with st.expander("🔐 How is my data handled?"):
        st.write("""
        Your data is processed locally and is *not stored* or shared. This app ensures user privacy by not collecting or transmitting any personal information.
        """)

    with st.expander("📱 Can I use this app on my phone?"):
        st.write("""
        Yes! The app is responsive and can be accessed through a mobile web browser for on-the-go predictions.
        """)

    with st.expander("📬 Who can I contact for support or feedback?"):
        st.markdown("""
        If you have any questions or feedback, feel free to reach out to us:

        - 📧 Email: [enochosenwafulah@gmail.com](mailto:enochosenwafulah@gmail.com)
        - 📱 WhatsApp: [+254701344230](https://wa.me/254701344230)
        """)


## Disclaimer Page
elif selected == "Disclaimer":
    st.markdown(
        "<h1 style='color:#2c7be5;'> ⚠ Disclaimer</h1>", 
        unsafe_allow_html=True
    )

    st.markdown("""
    ## Important Notice

    This application is designed as a *predictive tool for educational and informational purposes only. The content provided and the outputs generated by this system should **not* be interpreted as medical advice, diagnosis, or treatment.

    ### Please Note:

    - ✅ The prediction is based on patterns learned from historical data and *cannot account for individual-specific clinical factors*.
    - ✅ *Always consult with a qualified healthcare provider* for proper diagnosis, treatment options, and medical advice.
    - ✅ This tool *does not replace* clinical examinations, laboratory tests, or professional consultations.
    - ✅ *Do not make decisions* regarding your health based solely on this application's output.
    - ✅ While care has been taken in developing the model, *no guarantee of accuracy* is implied or should be assumed in all use cases.

    ### In Case of Medical Emergency:
    If you or someone else is experiencing a medical emergency, *call your doctor, visit the nearest hospital, or contact emergency services immediately*.

    ### Data Privacy:
    - No personal identifying data is collected, stored, or shared.
    - All inputs are processed locally during your session.

    ---  
    By using this application, you acknowledge and agree to the above terms.
    """)

    st.info("For more information or concerns, please consult a licensed medical professional.")

## Data Citation Page
elif selected == "Data Citation":
    st.markdown("<h1 style='color:#2c7be5;'>📚 Data Citation</h1>", unsafe_allow_html=True)

    st.markdown("""
    ### 📄 Dataset Information

    The machine learning model in this application was trained using a publicly available dataset that contains **anonymized clinical and lifestyle variables** relevant to hypertension risk prediction. These include age, salt intake, BMI, blood pressure history, medication use, stress level, sleep duration, and other lifestyle indicators.

    ### 🧾 Recommended Citation Format

    > Mia D. (2023). *Hypertension Risk Prediction Dataset*.  
    > Available at: [https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset](https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset).  
    > Accessed on: {datetime.datetime.today().strftime('%B %d, %Y')}.

    ### 📌 Usage Disclaimer

    - Please **cite the dataset creator** appropriately in any research, presentations, or applications using this data.
    - The dataset is intended **for academic, educational, and research purposes only**.
    - Always ensure data usage complies with ethical standards and Kaggle’s terms of service.

    🔗 **Source:** [Hypertension Risk Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset)
    """)


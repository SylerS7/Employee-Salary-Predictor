# streamlit app
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load models (with error handling)
@st.cache_resource
def load_models():
    try:
        model = joblib.load("model/salary_prediction_model.pkl")
        preprocessor = joblib.load("preprocessor/salary_preprocessor.pkl")
        return model, preprocessor
    except FileNotFoundError as e:
        st.error(f"Model files not found: {e}")
        st.stop()

model, preprocessor = load_models()

# App configuration
st.set_page_config(
    page_title="Employee Salary Predictor",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Employee Salary Predictor")
st.markdown("Predict employee salaries based on their profile and qualifications")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.header("Personal Information")
    
    # Fixed age range to match realistic dataset
    age = st.number_input("Age", min_value=18, max_value=65, value=25)
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    education = st.selectbox("Education Level", [
        "High School", "Bachelor's", "Master's", "PhD"
    ])

with col2:
    st.header("Professional Details")
    
    # Updated job titles from the fixed dataset
    job_title = st.selectbox("Job Title", [
        "Machine Learning Engineer", "Data Analyst", "Cyber Security Analyst", 
        "Data Scientist", "System Administrator", "Data Engineer", 
        "Senior Software Engineer", "Systems Engineer", "Cloud Architect", 
        "Software Engineer", "DevOps Engineer", "AI Researcher", 
        "Technical Support Engineer", "Full Stack Developer", "Business Analyst",
        "Software Development Intern", "Data Analytics Intern", "IT Support Intern", "Marketing Intern"
    ])
    
    # Fixed spelling: Employment Type
    employment_type = st.selectbox("Employment Type", ["Full-time", "Contract", "Internship"])
    
    industry = st.selectbox("Industry", [
        "Information Technology", "Finance", "Healthcare", "Education", "Retail",
        "Telecommunications", "E-commerce", "Manufacturing", "Government", "Consulting"
    ])

# Additional details in expandable section
with st.expander("Additional Details", expanded=True):
    col3, col4 = st.columns(2)
    
    with col3:
        # Fixed experience range and better validation
        experience = st.slider("Years of Experience", 0, 25, 2)
        
        # Updated locations from fixed dataset
        location = st.selectbox("Location", [
            "Mumbai", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Pune"
        ])
        
        # Better input handling for weekly hours
        weekly_hours = st.number_input("Weekly Hours", min_value=20, max_value=60, value=40)
    
    with col4:
        # Better input for certifications
        certifications = st.number_input("Number of Certifications", min_value=0, max_value=10, value=2)
        
        # Fixed remote work input
        remote_work = st.selectbox("Remote Work", ["Yes", "No"])

# Validation logic
def validate_inputs(age, experience, education, job_title, employment_type):
    errors = []
    
    # Age-experience validation
    min_graduation_age = {"High School": 18, "Bachelor's": 21, "Master's": 23, "PhD": 28}
    min_age_for_exp = min_graduation_age[education] + experience
    
    if age < min_age_for_exp:
        errors.append(f"Age ({age}) is too low for {experience} years of experience with {education} education. Minimum age should be {min_age_for_exp}")
    
    # Education-job validation
    if job_title == "AI Researcher" and education not in ["Master's", "PhD"]:
        errors.append("AI Researcher typically requires Master's or PhD education")
    
    if job_title in ["Machine Learning Engineer", "Data Scientist"] and education == "High School":
        errors.append(f"{job_title} typically requires at least Bachelor's degree")
    
    # Experience validation for senior roles
    if "Senior" in job_title and experience < 3:
        errors.append("Senior positions typically require at least 3 years of experience")
    
    if "Architect" in job_title and experience < 5:
        errors.append("Architect positions typically require at least 5 years of experience")
    
    # Internship validation
    if employment_type == "Internship" and experience > 2:
        errors.append("Internships are typically for candidates with 0-2 years of experience")
    
    return errors

# Real-time validation
validation_errors = validate_inputs(age, experience, education, job_title, employment_type)

if validation_errors:
    st.warning("⚠️ Please review the following:")
    for error in validation_errors:
        st.write(f"• {error}")

# Prediction button and logic
if st.button("🔮 Predict Salary", type="primary", disabled=bool(validation_errors)):
    
    with st.spinner("Calculating predicted salary..."):
        try:
            # Create input dataframe with correct column names and data types
            input_df = pd.DataFrame([{
                "Age": int(age),
                "Gender": gender,  # Keep as string, let preprocessor handle encoding
                "Education": education,
                "Job Title": job_title,
                "Experience": int(experience),
                "Employment Type": employment_type,  # Fixed spelling
                "Industry": industry,
                "Location": location,
                "Weekly Hours": int(weekly_hours),
                "Remote Work": remote_work,  # Keep as string
                "Certifications": int(certifications)
            }])
            
            # Transform the input using the preprocessor
            X_transformed = preprocessor.transform(input_df)
            
            # Make prediction
            predicted_salary = model.predict(X_transformed)[0]
            
            # Display results with improved formatting
            st.success("✅ Salary Prediction Complete!")
            
            # Create result display
            col_result1, col_result2, col_result3 = st.columns(3)
            
            with col_result1:
                st.metric(
                    label="Predicted Annual Salary",
                    value=f"₹{predicted_salary:.2f} Lakhs"
                )
            
            with col_result2:
                monthly_salary = predicted_salary / 12
                st.metric(
                    label="Monthly Salary",
                    value=f"₹{monthly_salary:.2f} Lakhs"
                )
            
            with col_result3:
                monthly_amount = (predicted_salary * 100000) / 12
                st.metric(
                    label="Monthly Amount",
                    value=f"₹{monthly_amount:,.0f}"
                )
            
            # Additional insights
            st.subheader("📊 Salary Insights")
            
            # Create insights based on the input
            insights = []
            
            if predicted_salary > 20:
                insights.append("🌟 This is a high-paying position in the Indian market")
            elif predicted_salary > 15:
                insights.append("💼 This is an above-average salary for the Indian market")
            elif predicted_salary > 8:
                insights.append("📈 This is a competitive salary in the Indian market")
            else:
                insights.append("📊 This is an entry-level salary range")
            
            if remote_work == "Yes":
                insights.append("🏠 Remote work capability may provide additional value")
            
            if experience > 10:
                insights.append("👨‍💼 Senior experience level commands premium salary")
            
            if education in ["Master's", "PhD"]:
                insights.append("🎓 Higher education contributes to salary premium")
            
            for insight in insights:
                st.write(insight)
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.write("Please ensure all model files are properly trained and saved with the correct feature names.")

# Additional information
with st.expander("ℹ️ About this Predictor"):
    st.write("""
    This salary predictor uses machine learning to estimate salaries based on:
    - Personal demographics (age, gender, education)
    - Professional details (job title, experience, industry)
    - Work arrangements (location, remote work, hours)
    - Qualifications (certifications)
    
    **Note**: Predictions are estimates based on training data and should be used as guidance only.
    Actual salaries may vary based on company size, specific skills, performance, and market conditions.
    """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit • Data Science Salary Predictor*")
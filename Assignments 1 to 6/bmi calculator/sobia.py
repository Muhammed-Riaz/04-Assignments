import streamlit as st

# 🎯 Web App Title
st.title("BMI Calculator 💪")

# 🎯 Input Fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01, format="%.2f")

heigth_change_meter = (feet * 0.3048) + (inches * 0.0254)

# 🎯 Display BMI Categories Before Calculation
st.markdown("""
### BMI Categories:
- **Underweight:** BMI < 18.5
- **Normal weight:** 18.5 – 24.9
- **Overweight:** 25 – 29.9
- **Obese:** BMI ≥ 30
""")

# 🎯 BMI Calculation
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)

        
        # Use `st.metric` for better visualization
        st.metric(label="Your BMI", value=f"{bmi:.2f}")
        
        # 🎯 Display BMI Category
        if bmi < 18.5:
            st.warning("🔹 You are Underweight 😔")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a Normal weight 😊")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are Overweight 😐")
        else:
            st.error("🚨 You are Obese 😞")
    else:
        st.error("Height must be greater than 0!")

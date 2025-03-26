# password_strength_checker.py

import streamlit as st
import re
def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (@$!%*?&#).")
    
    if strength == 4:
        return "Strong", "green", feedback
    elif strength == 3:
        return "Medium", "orange", feedback
    else:
        return "Weak", "red", feedback

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:20px;'>{strength}</span>", unsafe_allow_html=True)
    
    if feedback:
        st.subheader("Suggestions:")
        for tip in feedback:
            st.write(f"- {tip}")

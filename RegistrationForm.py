import streamlit as st

st.title("Registration Form")
st.write("Hello! Welcome to PBU")

name = st.text_input("Your Name: ")
if st.button("Submit"):
	st.success(f"Hai {name}! Welcome to PBU")

password = st.text("Password", type="password")

age = st.number_input("Age: ", min_value=1, max_value=100)

gender = st.radio("Gender: ", ["Male", "Female"])

course = st.selectbox("Select Course: ", ["Information Technology", "Business", "Engineering"])

agree = st.checkbox("I agree to the terms and conditions")

if st.button("Register"):
    if name == "" or password == "":
        st.warning("Please fill in all required fields!")
    elif not agree:
        st.warning("You must agree to the terms and conditions!")
    else:
        st.success("Registration Successful!")
        st.write("### User Details")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("Course:", course)

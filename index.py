import streamlit as st


def load_css():
    with open("style.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


st.title("Grade Calculator")
load_css()


marks = st.number_input("Enter your marks (0-100)", min_value=0, max_value=100, step=1)

if st.button("Calculate Grade"):
    grade = calculate_grade(marks)
    st.success(f"Your Grade: {grade}")

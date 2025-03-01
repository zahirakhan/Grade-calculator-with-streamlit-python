import streamlit as st


def load_css():
    with open("style.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def calculate_grade(obtained_marks, total_marks):
    percentage = (obtained_marks / total_marks) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade, percentage


st.title("Grade & Percentage Calculator")
load_css()


total_marks = st.number_input("Enter total marks", min_value=1, step=1)
obtained_marks = st.number_input("Enter obtained marks", min_value=0, step=1, max_value=total_marks if total_marks else 1)

if st.button("Calculate Result", key="grade_btn"):
    if obtained_marks > total_marks:
        st.error("Obtained marks cannot be greater than total marks!")
    else:
        grade, percentage = calculate_grade(obtained_marks, total_marks)
        st.success(f"Your Grade: {grade}")
        st.info(f"Your Percentage: {percentage:.2f}%")

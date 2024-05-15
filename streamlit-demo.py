
import streamlit as st

age = st.select_slider(
    "What is your age?",
    options=["5", "10", "15", "20", "25", "30", "35", "40", "45"])
st.write("Your age is", age)

import streamlit as st
 
st.title("MinAungThant's calculator")
 
st.write("---")
 
num1 = st.number_input(label="Enter first number")
 
num2 = st.number_input(label="Enter second number")
 
st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))
 
ans = 0
 
def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation=="Divide" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
 
    st.success(f"Answer = {ans}")
 
if st.button("Calculate result"):
    calculate()

import streamlit as st

option = st.selectbox(
    "What is your favourite food?",
    ("Shan Noodles", "Mont Hinn Garr", "Mont tee"))

st.write("Your favorite food is:", option, ",thats a good choice!")

import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)
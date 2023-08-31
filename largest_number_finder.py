import streamlit as st

st.title("Largest Number Finder")

st.markdown("""
Welcome to the Largest Number Finder! 🚀

Enter three numbers, and we'll help you discover the largest among them.
""")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find the Largest Number"):
    largest = max(num1, num2, num3)
    st.success(f"The largest number among {num1}, {num2}, and {num3} is: 
{largest}")


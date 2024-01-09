import streamlit as st

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

def main():
    st.title("Simple Calculator App")

    operation = st.sidebar.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")

    result = None

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        if num2 != 0:
            result = divide(num1, num2)
        else:
            st.error("Cannot divide by zero")

    if result is not None:
        st.write(f"Result: {num1} {operation.lower()} {num2} = {result}")

if __name__ == "__main__":
    main()

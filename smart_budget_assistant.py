import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import streamlit as st

# Load the data from the CSV file
file_path = r"C:\Users\Sathyapriya subbiah\Documents\MINOR PROJECT\BO_new\Newdatasheet.csv"
data = pd.read_csv(file_path)

st.title("Smart Budget Assistant for Students")

# Initialize predicted_expenses
predicted_expenses = None

# Ask for user's information
name = st.text_input("Enter your name: ")

salary = st.number_input("Enter your salary:")
rent = st.number_input("Enter your rent:")
utilities = st.number_input("Enter you utilities: ")

if st.button("Calculate Expenses"):
    # Prepare the data for non-linear regression
    X = data[['Salary', 'Rent', 'Utilities']]
    y = data[['Food', 'Transport', 'Entertainment', 'Healthcare', 'Grooming', 'Savings', 'Others']]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the non-linear regression model (Decision Tree Regressor)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    # Predict expenses for the user
    predicted_expenses = model.predict([[salary, rent, utilities]])

    st.write("### Your personalised Budget Summary is given below. Feel free to make slight changes!")

    st.write("### Recommended Expenses for", name)
    st.write(f"##### Food: ", predicted_expenses[0][0])
    st.write(f"##### Transport: ", predicted_expenses[0][1])
    st.write(f"##### Entertainment: ", predicted_expenses[0][2])
    st.write(f"##### Healthcare: ", predicted_expenses[0][3])
    st.write(f"##### Grooming: ", predicted_expenses[0][4])
    st.write(f"##### Savings: ", predicted_expenses[0][5])
    st.write(f"##### Others: ", predicted_expenses[0][6])

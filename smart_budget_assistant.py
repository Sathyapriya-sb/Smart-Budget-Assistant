import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import streamlit as st

# Load the data from the CSV file
file_path = "Datasheet.csv"
data = pd.read_csv(file_path)

st.title("Smart Budget Assistant for Students")

# Initialize predicted_expenses
predicted_expenses = None

# Ask for user's information
name = st.text_input("What is your name?")

salary = st.number_input("Enter your salary:")
rent = st.number_input("Enter your rent:")

if st.button("Calculate Expenses"):
    # Prepare the data for non-linear regression
    X = data[['Salary', 'Rent']]
    y = data[['Food', 'Transport', 'Entertainment', 'Utilities', 'Healthcare', 'Grooming', 'Savings', 'Others']]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the non-linear regression model (Decision Tree Regressor)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    # Predict expenses for the user
    predicted_expenses = model.predict([[salary, rent]])

    # Calculate the initial sum of predicted expenses and rent
    initial_total_expenses = predicted_expenses.sum().sum() + rent

    # Check if the sum of predicted expenses and rent is equal to the salary within a tolerance
    tolerance = 1e-4

    st.write("### Budget Summary")

    if abs(salary - initial_total_expenses) > tolerance:
        surplus_or_deficit = salary - initial_total_expenses

        if surplus_or_deficit > 0:  # It's a surplus
            # Divide the surplus among 8 expense categories
            surplus_per_category = surplus_or_deficit / 8
            adjusted_expenses = [x + surplus_per_category for x in predicted_expenses[0]]
        else:  # It's a deficit
            # Divide the deficit among 6 expense categories
            deficit_per_category = surplus_or_deficit / 6
            adjusted_expenses = [predicted_expenses[0][0], predicted_expenses[0][1]]
            adjusted_expenses += [x + deficit_per_category for x in predicted_expenses[0][2:]]

        # Ensure that adjusted expenses have two brackets
        adjusted_expenses = [adjusted_expenses]

        st.write("### Recommended Expenses for", name)
        st.write(f"##### Food: ", adjusted_expenses[0][0])
        st.write(f"##### Transport: ", adjusted_expenses[0][1])
        st.write(f"##### Entertainment: ", adjusted_expenses[0][2])
        st.write(f"##### Utilities: ", adjusted_expenses[0][3])
        st.write(f"##### Healthcare: ", adjusted_expenses[0][4])
        st.write(f"##### Grooming: ", adjusted_expenses[0][5])
        st.write(f"##### Savings: ", adjusted_expenses[0][6])
        st.write(f"##### Others: ", adjusted_expenses[0][7])
        
    else:
        # No adjustments needed, print the original predicted expenses
        st.write("### Recommended Expenses for", name)
        st.write(f"###### Food: ", '### ', predicted_expenses[0][0])
        st.write(f"##### Transport: ", predicted_expenses[0][1])
        st.write(f"##### Entertainment: ", predicted_expenses[0][2])
        st.write(f"##### Utilities: ", predicted_expenses[0][3])
        st.write(f"##### Healthcare: ", predicted_expenses[0][4])
        st.write(f"##### Grooming: ", predicted_expenses[0][5])
        st.write(f"##### Savings: ", predicted_expenses[0][6])
        st.write(f"##### Others: ", predicted_expenses[0][7])

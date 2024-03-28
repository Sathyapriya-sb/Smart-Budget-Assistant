import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load the data from the CSV file
file_path = r"C:\Users\Sathyapriya subbiah\Documents\MINOR PROJECT\BO_new\Budget Optimization final datasheet.csv"
data = pd.read_csv(file_path)

# Ask for user's information
name = input("What is your name? ")
living_status = input("Are you a bachelor or a family? ").lower()

num_shared = 1  # Default value for num_shared

if living_status == "bachelor":
    salary = float(input("Enter your salary: "))
    rent = float(input("Enter your rent: "))

elif living_status == "family":
    num_family_members = int(input("How many are there in the family? "))
    num_earning_members = int(input("How many are earning an income?"))

    salary = 0
    for i in range(num_earning_members):
        partial_salary = float(input(f"Enter the salary of family member {i+1}: "))
        salary += partial_salary
    rent = float(input("Enter your rent: "))

#salary = float(input("Enter your salary: "))
#rent = float(input("Enter your rent: "))

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
#print("Type of predicted_expenses:", type(predicted_expenses))

#converting to list
predicted_expenses_list = predicted_expenses.tolist()
#print("Type of predicted_expenses_list:", type(predicted_expenses_list))
#print("Predicted_expenses_list",(predicted_expenses_list))

# Calculate the initial sum of predicted expenses and rent
initial_total_expenses = predicted_expenses.sum().sum() + rent

#sum
initial_total_expenses_list = rent

for sublist in predicted_expenses_list:
    for value in sublist:
        initial_total_expenses_list += value

#print("Sum:", initial_total_expenses_list)

# Check if the sum of predicted expenses and rent is equal to the salary within a tolerance
tolerance = 1e-4

print(abs(salary - initial_total_expenses_list))
print(tolerance)
if abs(salary - initial_total_expenses_list) > tolerance:

    surplus_or_deficit = salary - initial_total_expenses_list

    if surplus_or_deficit > 0:  # It's a surplus
        # Divide the surplus among 8 expense categories
        surplus_per_category = surplus_or_deficit / 8
        print("surplus", surplus_per_category)
        adjusted_expenses = [x + surplus_per_category for x in predicted_expenses_list[0]]
    else:  # It's a deficit
        # Divide the deficit among 6 expense categories
        deficit_per_category = surplus_or_deficit / 6
        print("deficit", deficit_per_category)
        adjusted_expenses = [predicted_expenses_list[0][0], predicted_expenses_list[0][1]]
        adjusted_expenses += [x + deficit_per_category for x in predicted_expenses_list[0][2:]]

    # Ensure that adjusted expenses have two brackets
    adjusted_expenses = [adjusted_expenses]

    #print("Adjusted Expenses:", adjusted_expenses)

    # Print the adjusted expenses
    print(f"Recommended Expenses for {name}:")
    print(f"Food: {adjusted_expenses[0][0]}")
    print(f"Transport: {adjusted_expenses[0][1]}")
    print(f"Entertainment: {adjusted_expenses[0][2]}")
    print(f"Utilities: {adjusted_expenses[0][3]}")
    print(f"Healthcare: {adjusted_expenses[0][4]}")
    print(f"Grooming: {adjusted_expenses[0][5]}")
    print(f"Savings: {adjusted_expenses[0][6]}")
    print(f"Others: {adjusted_expenses[0][7]}")
else:
    # No adjustments needed, print the original predicted expenses
    print(f"Recommended Expenses for {name}:")
    print(f"Food: {predicted_expenses[0][0]}")
    print(f"Transport: {predicted_expenses[0][1]}")
    print(f"Entertainment: {predicted_expenses[0][2]}")
    print(f"Utilities: {predicted_expenses[0][3]}")
    print(f"Healthcare: {predicted_expenses[0][4]}")
    print(f"Grooming: {predicted_expenses[0][5]}")
    print(f"Savings: {predicted_expenses[0][6]}")
    print(f"Others: {predicted_expenses[0][7]}")
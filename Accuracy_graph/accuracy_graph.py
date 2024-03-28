import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = r"C:\Users\Sathyapriya subbiah\Documents\MINOR PROJECT\BO_new\Datasheet.csv"
data = pd.read_csv(file_path)

# Prepare the data for non-linear regression
X = data[['Salary', 'Rent']]
y = data[['Food', 'Transport', 'Entertainment', 'Utilities', 'Healthcare', 'Grooming', 'Savings', 'Others']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the non-linear regression model (Decision Tree Regressor)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Predict expenses for the testing data
predicted_expenses = model.predict(X_test)

# Calculate accuracy and validation percentage using R-squared (R2) score
accuracy = model.score(X_test, y_test)

# Categories of expenses
categories = list(y.columns)

# Plot separate graphs for each category
for i, category in enumerate(categories):
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(1, len(X_test) + 1), y_test[category], color='#d96242', label=f"Actual {category}")
    plt.plot(np.arange(1, len(X_test) + 1), predicted_expenses[:, i], color='#9e99eb', linestyle='--', label=f"Predicted {category}")

    plt.xlabel("Sample Index")
    plt.ylabel("Expenses")
    plt.legend()
    plt.title(f"Model Accuracy (R2 Score) for {category}: {accuracy:.2f}")
    plt.xticks(rotation=0)
    plt.show()

print(f"Overall Model Accuracy (R2 Score): {accuracy:.2f}")


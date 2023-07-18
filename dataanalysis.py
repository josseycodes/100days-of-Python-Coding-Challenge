import pandas as pd
import numpy as np

# Load the dataset (replace 'data.csv' with your dataset file name and path)
data = pd.read_csv('data.csv')

# Data Cleaning
# Remove any duplicate rows
data.drop_duplicates(inplace=True)

# Data Filtering
# Filter data based on specific conditions
filtered_data = data[data['age'] > 18]

# Data Aggregation
# Calculate the average age and income
average_age = data['age'].mean()
average_income = data['income'].mean()

# Data Visualization
import matplotlib.pyplot as plt

# Plot a histogram of ages
plt.hist(data['age'], bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()

# Plot a bar chart of income by gender
income_by_gender = data.groupby('gender')['income'].mean()
income_by_gender.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Average Income')
plt.title('Average Income by Gender')
plt.show()

# Display insights
print(f"Average Age: {average_age:.2f}")
print(f"Average Income: {average_income:.2f}")
print("Data Analysis Completed!")


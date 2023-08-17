import pandas as pd

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Display basic information about the dataset
print("Initial dataset info:")
print(data.info())

# Handling missing values
# Drop rows with missing values
data.dropna(inplace=True)

# Handling duplicates
data.drop_duplicates(inplace=True)

# Data type conversions
# Convert columns to appropriate data types if needed
data['numeric_column'] = pd.to_numeric(data['numeric_column'])
data['date_column'] = pd.to_datetime(data['date_column'])

# Outlier detection and removal (you may need more advanced techniques)
# z-score method for outlier removal
z_scores = (data['numeric_column'] - data['numeric_column'].mean()) / data['numeric_column'].std()
data = data[abs(z_scores) < 3]

# Categorical variable encoding
data = pd.get_dummies(data, columns=['categorical_column'], drop_first=True)

# Feature scaling (if needed)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data['scaled_numeric_column'] = scaler.fit_transform(data[['numeric_column']])

# Save the cleaned and preprocessed data to a new CSV file
data.to_csv('cleaned_data.csv', index=False)

# Display cleaned dataset info
print("Cleaned dataset info:")
print(data.info())

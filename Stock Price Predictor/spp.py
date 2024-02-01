import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Function to create sequences for LSTM model
def create_sequences(data, seq_length):
    sequences = []
    target = []
    for i in range(len(data) - seq_length):
        seq = data[i:i + seq_length]
        label = data[i + seq_length]
        sequences.append(seq)
        target.append(label)
    return np.array(sequences), np.array(target)

# Load historical stock data
# Replace 'your_stock_data.csv' with the path to your dataset
df = pd.read_csv('your_stock_data.csv')

# Choose the feature(s) you want to use for prediction
# For simplicity, we'll use only the 'Close' price for prediction
data = df['Close'].values.reshape(-1, 1)

# Normalize the data using MinMaxScaler
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Define the sequence length (number of past days to consider)
sequence_length = 10

# Create sequences for LSTM model
X, y = create_sequences(data_normalized, sequence_length)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build an LSTM model
model = Sequential()
model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=2)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Inverse transform the predictions and actual values to get back to the original scale
y_pred_inv = scaler.inverse_transform(y_pred)
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))

# Evaluate the model
mse = mean_squared_error(y_test_inv, y_pred_inv)
print(f'Mean Squared Error: {mse}')

# Now, you can use the trained model for predicting future stock prices
# For example, you can create sequences from the latest available data and predict the next day's closing price.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.ensemble import IsolationForest

# Load the dataset
df = pd.read_csv('time_series_data.csv')

# Convert the date column to datetime format and set it as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Visualize the time series
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Value')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Decompose the time series into trend, seasonal, and residual components
decomposition = seasonal_decompose(df['Value'], model='additive', period=12)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Visualize decomposition
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['Value'], label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonal')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residual')
plt.legend(loc='upper left')
plt.show()

# Plot ACF and PACF
plot_acf(df['Value'], lags=20)
plt.show()

plot_pacf(df['Value'], lags=20)
plt.show()

# Forecast using ARIMA model
model = ARIMA(df['Value'], order=(1,1,1)) # Example order, you can tune this
model_fit = model.fit()

# Forecast future values
forecast = model_fit.forecast(steps=12) # Example forecast for next 12 steps
print("Forecasted values:", forecast)

# Anomaly detection using Isolation Forest
# Assuming 'Value' column is the feature we're analyzing
model_iso = IsolationForest(contamination=0.05) # Ex

import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([10, 25, 15, 20, 12])

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

# Line graph
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Graph')
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Scatter Plot')
plt.show()


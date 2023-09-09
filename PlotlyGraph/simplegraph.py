import plotly.express as px

# Sample dataset
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 25, 15, 30]}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create an interactive bar chart using Plotly Express
fig = px.bar(df, x='Category', y='Value', title='Sample Bar Chart')

# Show the plot
fig.show()


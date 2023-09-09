import plotly.express as px

# Sample dataset with multiple columns
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Sales': [1200, 1500, 1800, 2100, 2500, 2800, 3000],
    'Profit': [100, 200, 300, 350, 400, 450, 500],
    'Region': ['North', 'North', 'North', 'South', 'South', 'East', 'East']
}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create an interactive scatter plot with customizations
fig = px.scatter(df, x='Year', y='Sales', size='Profit', color='Region',
                 labels={'Year': 'Year', 'Sales': 'Sales Amount'},
                 title='Sales Analysis Over Time',
                 hover_name='Region', facet_col='Region',
                 trendline='ols')

# Customize the appearance
fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')),
                  selector=dict(mode='markers+text'))

# Show the plot
fig.show()


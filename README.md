In this program, we use Pandas to load and manipulate the dataset. We perform data cleaning by removing duplicate rows. Next, we filter the data to include only rows where the age is greater than 18.

We then perform data aggregation to calculate the average age and average income from the dataset.

For data visualization, we use Matplotlib to create a histogram of ages and a bar chart of the average income by gender.

Finally, we display the insights, such as the average age and income, obtained from the dataset.

Let's define each function used in the Python program:

pd.read_csv('data.csv'): This function is used to read a CSV (Comma Separated Values) file and create a DataFrame. The DataFrame is a data structure provided by the Pandas library, and it is used to store and manipulate tabular data.

data.drop_duplicates(inplace=True): The drop_duplicates() function is a DataFrame method that removes any duplicate rows from the DataFrame. The inplace=True argument ensures that the changes are made directly to the original DataFrame, modifying it in place.

data[data['age'] > 18]: This is a data filtering operation. It uses boolean indexing to filter the DataFrame and create a new DataFrame filtered_data that includes only the rows where the 'age' column is greater than 18.

data['age'].mean(): This function calculates the mean (average) of the 'age' column in the DataFrame. The mean() method is provided by Pandas, and it computes the average of numerical data.

data['income'].mean(): Similar to the previous function, this calculates the mean of the 'income' column in the DataFrame.

plt.hist(data['age'], bins=10, edgecolor='black'): This function is used to create a histogram of the 'age' column using Matplotlib. A histogram shows the distribution of data within specific bins (intervals). The bins=10 argument specifies the number of bins, and edgecolor='black' sets the color of the histogram bars' edges.

income_by_gender = data.groupby('gender')['income'].mean(): This line groups the DataFrame by the 'gender' column and calculates the mean of the 'income' column for each group. The result is stored in a new Pandas Series called income_by_gender.

income_by_gender.plot(kind='bar'): This function creates a bar chart of the income_by_gender Series using Matplotlib. It displays the average income for each gender category as bars.

print(f"Average Age: {average_age:.2f}"): This line prints the average age with two decimal places using an f-string. The :.2f formatting specifies to display the number with two decimal places.

print(f"Average Income: {average_income:.2f}"): Similar to the previous line, this prints the average income with two decimal places.

plt.show(): This function is used to display the plots created with Matplotlib. It shows the histogram and bar chart in separate windows



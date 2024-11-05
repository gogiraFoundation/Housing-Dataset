import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# Set the file path
file_path = "/Users/mac/Desktop/n-dev/data/housing_datasets/housing_data/uk_housing_datasets/reviewed_datasets/"
data_file = file_path + "Uk_Local_Housing_Data.csv"

# Load the data
data = pd.read_csv(data_file)
print("Data loaded successfully.")
print(data[0:5])

# Function to plot data
def plot_data(data, x_col, y_col, title, xlabel, ylabel):
    """
    Plots the data using Seaborn and Matplotlib.

    Args:
        data (DataFrame): The dataset to be plotted.
        x_col (str): The name of the column to be plotted on the X-axis.
        y_col (str): The name of the column to be plotted on the Y-axis.
        title (str): The title of the plot.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=data[x_col], y=data[y_col], marker="o")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error in plotting data: {e}")


if __name__ == "__main__":
    # Replace 'Year' and 'Housing Units' with actual column names from your dataset
    plot_data(data, x_col='Year', y_col='Housing Units', 
              title='Housing Units Over the Years', 
              xlabel='Year', ylabel='Number of Housing Units')

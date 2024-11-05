#import all relevant modules

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
print(f"importing modules")




#customizable print function

def print_log(message):
    """
    Centralized function to handle all print statements.
    Logs messages to a file and prints them to the console.
    """
    # Ensure the message is a string before logging
    message_str = str(message)

    # Print the message to the console
    print(message_str)
    
    # Log the message to a file
    #with open(log_file, "a") as f:
     #   f.write(message_str + '\n')
        

        
        
def plot_barchart(x_column, y_column, label=None, color=None):
    try:
        # Plot the data using a bar chart
        plt.figure(figsize=(15, 8))
        
        # Add the label for the legend
        plt.bar(x_column, y_column, color=color, label=label)

        # Prompt user for the plot title and axis labels
        plot_title = input('Plot Title: ')
        x_axis_label = input('X-axis Label: ')
        y_axis_label = input('Y-axis Label: ')

        # Add title and labels to the plot
        plt.title(plot_title)
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        
        # Add the legend if a label was provided
        if label:
            plt.legend()

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

         

def plot_scatter(x_column, y_column):
    try:
        # Plot the data using a scatter plot
        plt.figure(figsize=(20, 10))
        plt.scatter(x_column, y_column, color='blue', marker='o')

        # Add titles and labels
        plt.title(input('Plot Title: '))
        plt.xlabel(input('X-axis Label: '))
        plt.ylabel(input('Y-axis Label: '))

        # Display the plot
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

def plot_heatmap(data, plot_title="Heatmap", x_label="X-axis", y_label="Y-axis"):
    """
    Function to plot a heatmap from a DataFrame.
    
    Args:
        data (DataFrame): Data for heatmap.
        plot_title (str): Title of the plot.
        x_label (str): Label for the X-axis.
        y_label (str): Label for the Y-axis.
    """
    try:
        # Ensure the data is in the correct format (2D)
        if data.ndim != 2:
            print("Error: Input data must be 2D.")
            return

        # Create the heatmap
        plt.figure(figsize=(40, 30))
        sns.heatmap(data, annot=True, cmap="crest", linewidths=1)

        # Add titles and labels
        plt.title(plot_title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

        

def plot_line(data, x_column, y_column):

    """
    Function to plot a line graph using seaborn.

    Args:
        data (DataFrame): Data for plotting.
        x_column (str): The name of the column to be used as X-axis.
        y_column (str): The name of the column to be used as Y-axis.
    """
    try:
        # Ensure that x_column and y_column exist in the data
        if x_column not in data.columns or y_column not in data.columns:
            print(f"Error: Columns '{x_column}' or '{y_column}' not found in the data.")
            return

        # Plot the line graph
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x=x_column, y=y_column)

        # Add titles and labels
        plt.title(input('Plot Title: '))
        plt.xlabel(input('X-axis Label: '))
        plt.ylabel(input('Y-axis Label: '))

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



def stage_data(file_path):    
    """
    Loads data from an Excel file and displays basic information.
    
    Args:
        file_path (str): The full path to the Excel file.
    
    Returns:
        tuple: Loaded DataFrames for starts and completions, or (None, None) if an error occurred.
    """
    try:
        # Load the Excel file and skip the first 5 rows
        data_file = pd.read_excel(file_path, sheet_name='UK_Starts', index_col='Revised', skiprows=5, engine='openpyxl')
        data_file2 = pd.read_excel(file_path, sheet_name='UK_Completions', index_col='Revised', skiprows=5, engine='openpyxl')
        print("File loaded successfully!")
        
        # Show data types
        print(f"\nData types of UK_Starts columns:\n{data_file.dtypes}")
        print(f"\nData types of UK_Completions columns:\n{data_file2.dtypes}")
        return data_file, data_file2

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None, None
    except ValueError as ve:
        print(f"Error: {ve}. Please check the sheet name or content.")
        return None, None
    except Exception as e:
        print(f"Operation Failed: {e}")
        return None, None


import pandas as pd
import numpy as np


# Function to calculate missing values
def missing_values(data):
    try:
        # Total number of cells in the dataset
        total_cells = np.product(data.shape)
        
        # Total number of missing values in the dataset
        total_missing_values = data.isnull().sum().sum()
        
        # Percentage of missing data from dataset
        percentage_missing = (total_missing_values / total_cells) * 100
        
        # Log results
       # print(f"The total number of cells is: {total_cells}")
       # print(f"The total number of missing values in the dataset: {total_missing_values}")
       # print(f"The percentage of missing values in dataset: {percentage_missing:.2f}%")
    
    except Exception as e:
        print(f"Operation failed: {e}")

# Function to clean the data
def cleaning_data(data):
    try:
        years = ['2009-2010', '2010-2011', '2011-2012', '2012-2013', '2013-2014',
         '2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019',
         '2019-2020', '2020-2021', '2021-2022', '2022-2023', '2023-2024']
        
        # Convert all columns (except the first four) to numeric, coercing non-numeric to NaN
        data_numeric = data.iloc[:, 3:].apply(pd.to_numeric, errors='coerce')
        
        # Combine the cleaned data with the first column (Local Authority Name)
        cleaned_data = pd.concat([data.iloc[:, 3], data_numeric], axis=1)
        
        
        # Convert all columns (starting from the 4th one) to numeric, coercing non-numeric values to NaN
        data_numeric = data.iloc[:, 3:].apply(pd.to_numeric, errors='coerce')
        
        # Combine the cleaned numeric data with the first three columns (assumed to be non-numeric identifiers)
        cleaned_data = pd.concat([data.iloc[:, :3], data_numeric], axis=1)

        
        return cleaned_data
    
    except Exception as e:
        print(f"Error: {e}")


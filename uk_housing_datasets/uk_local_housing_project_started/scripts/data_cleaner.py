import pandas as pd
import numpy as np
from print_log import print_log

class DataCleaner:
    def __init__(self, data):
        """
        Initialize the DataCleaner object with a pandas DataFrame.
        
        Args:
            data: The DataFrame to be cleaned.
        """
        self.data = data.copy()  # Create a copy of the dataset

    def missing_values(self):
        """
        Checks for missing values in the dataset and logs relevant information.
        """
        try:
            # Gets total number of cells in the dataset
            total_cells = np.product(self.data.shape)
            
            # Gets total number of missing values in the dataset
            total_missing = self.data.isnull().sum().sum()
            
            # Percentage of data missing
            percent_missing = (total_missing / total_cells) * 100
            
            # Logging the information
            print_log(f"The total number of cells is {total_cells}")
            print_log(f"The total number of missing values: {total_missing}")
            print_log(f"Percentage of missing values in dataset: {percent_missing:.2f}%\n")
            
            # Print and log missing values count per column
            missing_values_counts = self.data.isnull().sum()
            print_log("Missing values per column:\n" + str(missing_values_counts[missing_values_counts > 0]))
            
        except Exception as e:
            print_log(f"Operation failed: {e}")
        return self

    def fill_missing_values(self):
        """
        Fills missing values with 'unknown' in the dataset and logs the action.
        """
        try:
            # Filling NaN values with 'unknown'
            self.data = self.data.fillna("unknown")
            print_log("Filled missing values with 'unknown'.\n")
        except Exception as e:
            print_log(f"Error while filling missing values: {e}")
        return self

    def clean_data(self):
        """
        Cleans the data by:
        - Removing unnecessary columns (where all values are NaN)
        - Renaming columns for better readability
        """
        try:
            # Remove columns where all values are NaN
            cleaned_data = self.data.dropna(axis=1, how='all')
            # Check the current columns before renaming
            print_log(f"Columns in original dataset: {self.data.shape[1]}")
            print_log(f"Columns with missing values dropped: {cleaned_data.shape[1]}")

            # Ensure the data has the correct number of columns before renaming
            if len(cleaned_data.columns) == 19:
                cleaned_data.columns = [
                    'Region Type', 'Region or Country Name', 'Local Authority Code', 'Local Authority Name',
                    '2009-2010', '2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015',
                    '2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021',
                    '2021-2022', '2022-2023', '2023-2024'
                ]
                self.data = cleaned_data
            else:
                print_log(f"Warning: Expected 19 columns, but found {len(cleaned_data.columns)}. Column renaming skipped.")
            
            # Remove any rows where all values are NaN
            self.data = self.data.dropna(how='all')

            # Log the cleaned data structure
            print_log(f"\nColumn names after renaming: {list(self.data.columns)}")
            print_log("\nDataFrame info:")
            print_log(str(self.data.info()))  # Display DataFrame info

        except Exception as e:
            print_log(f"Error during data cleaning: {e}")
        return self

    def get_cleaned_data(self):
        """
        Returns the cleaned data.
        """
        return self.data
import pandas as pd


class FileUpload:
    def __init__(self):
        pass

    def stage_data(self, file_path):    
        try:
            # Load the Excel file and skip the first 5 rows
            data_file = pd.read_excel(file_path, sheet_name='UK_Starts', skiprows=5, engine='openpyxl')
            print("File loaded successfully!")
            
            # Show data types and first few rows
            print(f"\nData types of columns:\n{data_file.dtypes}")
            print(f"\nFirst few rows of the DataFrame:\n{data_file.head()}")
            
            return data_file
        
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
            return None
        except ValueError as ve:
            print(f"Error: {ve}. Please check the sheet name or content.")
            return None
        except Exception as e:
            print(f"Operation Failed: {e}")
            return None



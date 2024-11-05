import os  # To check if the directory exists
import pandas as pd
from uploadfile import FileUpload
from data_visualizer import plot_data
from data_cleaner import DataCleaner
from print_log import print_log
from save_file import FileSaver

class DataReview:
    def __init__(self, file_path):
        """
        Initializes the DataReview object.
        
        Args:
            file_path (str): The full path to the Excel file to be processed.
        """
        self.file_path = file_path
        self.file_upload = FileUpload()  # Create an instance of FileUpload

    def check_directory(self):
        """
        Checks if the directory of the provided file path exists.

        Returns:
            bool: True if the directory exists, False otherwise.
        """
        directory = os.path.dirname(self.file_path)  # Get the directory of the file path
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist.")
            return False
        print(f"Directory {directory} exists.")
        return True

    def run_app(self):
        """
        Runs the main application logic.
        """
        print_log("Starting Operation...")

        # Load data using the FileUpload class
        data = self.file_upload.stage_data(self.file_path)  # Use self.file_path directly

        if data is not None:
            print("Data processing can continue...")  
            try:
                # Step 1: Initialize the DataCleaner object and clean the data
                cleaner = DataCleaner(data)
                cleaner.missing_values().fill_missing_values().clean_data()
                cleaned_data = cleaner.get_cleaned_data()

                # Step 2: Initialize the FileSaver object with the desired saving directory
                saved_file_directory = os.path.join(directory_path, "uk_housing_datasets", "reviewed_datasets")
                os.makedirs(saved_file_directory, exist_ok=True)  # Ensure the directory exists
                file_saver = FileSaver(saved_file_directory)  # Pass the directory

                # Step 3: Save the cleaned data in various formats
                file_saver.save_file(cleaned_data, "Uk_Local_Housing_Data", "csv")  # Save as CSV
                # You can also save it as PDF or PNG based on the requirements
                # file_saver.save_file(cleaned_data, "Housing_data", "pdf")
                # file_saver.save_file(cleaned_data['column_to_plot'], "Housing_data_plot", "png")

                # Step 4: Visualize the data (if required)
                # Uncomment the line below to visualize the data after cleaning
                # plot_data(cleaned_data)

            except Exception as e:
                print_log(f"Operation Failed: {e}")

        else:
            print("Data loading failed, exiting application.")

if __name__ == "__main__":
    try:
        # Specify the directory path (replace with your actual path)
        directory_path = "/Users/mac/Desktop/n-dev/data/housing_datasets/housing_data"
        uk_housing_file_path = os.path.join(directory_path, "uk_housing_datasets", "uk_local_housing_project_started", "UK_local_authority_housing_data.xlsx")
        
        # Create an instance of DataReview
        data_review = DataReview(uk_housing_file_path)

        # Check if the directory exists
        if data_review.check_directory():
            data_review.run_app()  # Call the main application logic
    except Exception as e:
        print(f"Operation failed: {e}")

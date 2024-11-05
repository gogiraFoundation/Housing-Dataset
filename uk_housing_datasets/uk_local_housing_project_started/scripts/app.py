from data_cleaner import DataCleaner
from save_file import FileSaver
from uploadfile import data_file
from print_log import print_log

file_path = "/Users/mac/Desktop/n-dev/data/housing_datasets/housing_data/uk_housing_datasets/reviewed_datasets/"


def start_app():
    if __name__ == "__main__":
        try:

            print_log("Starting Operation...")

            # Step 1: Initialize the DataCleaner object and clean the data
            cleaner = DataCleaner(data_file)
            cleaner.missing_values().fill_missing_values().clean_data()
            cleaned_data = cleaner.get_cleaned_data()

            # Step 2: Initialize the FileSaver object with the desired file path
            file_saver = FileSaver(file_path)

            # Step 3: Save the cleaned data in various formats
            file_saver.save_file(cleaned_data, "Uk_Local_Housing_Data", "csv")  # Save as CSV
            # You can also save it as PDF or PNG based on the requirements
            # file_saver.save_file(cleaned_data, "Housing_data", "pdf")
            # file_saver.save_file(cleaned_data['column_to_plot'], "Housing_data_plot", "png")
        
        except Exception as e:
            print(f"Operation Failed: {e}")

import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from print_log import print_log

class FileSaver:
    def __init__(self, file_path):
        """
        Initializes the FileSaver object with the base file path where files will be saved.
        
        Args:
            file_path: The directory path where files will be saved.
        """
        self.file_path = file_path

    def save_as_csv(self, data, file_name):
        """
        Saves the data as a CSV file.
        
        Args:
            data: The DataFrame to be saved as CSV.
            file_name: The name of the file (without extension).
        """
        try:
            full_path = os.path.join(self.file_path, f"{file_name}.csv")
            data.to_csv(full_path, index=False)
            print_log(f"File saved as {file_name}.csv")
        except Exception as e:
            print_log(f"An error occurred while saving CSV: {e}")

    def save_as_pdf(self, data, file_name):
        """
        Saves the data as a PDF file, with each line of the data as text.
        
        Args:
            data: The data to be saved as a PDF file (expects an iterable).
            file_name: The name of the file (without extension).
        """
        try:
            full_path = os.path.join(self.file_path, f"{file_name}.pdf")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times New Roman", size=12)

            for line in data:
                pdf.cell(200, 10, txt=str(line), ln=True, align='L')

            pdf.output(full_path)
            print_log(f"File saved as {file_name}.pdf")
        except Exception as e:
            print_log(f"An error occurred while saving PDF: {e}")

    def save_as_png(self, data, file_name):
        """
        Saves the data as a PNG file, assuming the data can be plotted.
        
        Args:
            data: The data to be plotted and saved as a PNG file.
            file_name: The name of the file (without extension).
        """
        try:
            full_path = os.path.join(self.file_path, f"{file_name}.png")
            plt.figure(figsize=(6, 4))
            plt.plot(data)
            plt.savefig(full_path)
            plt.close()
            print_log(f"File saved as {file_name}.png")
        except Exception as e:
            print_log(f"An error occurred while saving PNG: {e}")

    def save_file(self, data, file_name, file_type):
        """
        Saves the data in the specified format (csv, pdf, png).
        
        Args:
            data: The data to be saved (expects different formats based on file type).
            file_name: The name of the file (without extension).
            file_type: The type of file ('csv', 'pdf', or 'png').
        """
        if file_type == 'csv':
            self.save_as_csv(data, file_name)
        elif file_type == 'pdf':
            self.save_as_pdf(data, file_name)
        elif file_type == 'png':
            self.save_as_png(data, file_name)
        else:
            print_log(f"Unsupported file type: {file_type}. Please choose 'csv', 'pdf', or 'png'.")


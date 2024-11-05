import zipfile



def extract_zip(zip_file_path, extract_to):
    """
    Extracts the contents of a zip file to the specified directory.
    
    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory where the zip file will be extracted.
    
    Returns:
        str: The path to the extracted Excel file if found, else None.
    """
    try:
        # Extract the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Zip file extracted to {extract_to}")
            
        # Find the Excel file in the extracted folder
        for root, dirs, files in os.walk(extract_to):
            for file in files:
                if file.endswith('.xlsx'):
                    return os.path.join(root, file)
        
        print("No Excel file found in the extracted contents.")
        return None

    except zipfile.BadZipFile:
        print("Error: The file is not a valid zip file.")
        return None
    except Exception as e:
        print(f"Operation Failed: {e}")
        return None




def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.

    Parameters:
        file_path (str): Path to the file to be read.

    Returns:
        str: Content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: For other unexpected errors.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

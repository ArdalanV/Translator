import ast

Languages = ["Persian", "Spanish", "Italian", "German", "French"]

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
    
def keyword_parser(code, language):
    """
    Iterates through the contents of a file's code, translates the keywords of the
    code to the language
    """
    

class KeywordTranslator(ast.NodeTransformer):
    keywords = {}

    def __init__(self, keyword_mapping):
        self.keywords_mapping = keyword_mapping

    def visit_Name(self, node):
        if node.id in self.keywords_mapping:
            node.id = self.keywords_mapping[node.id]
        return node
    
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.keywords_mapping:
            node.func.id = self.keywords_mapping[node.func.id]
        return self.generic_visit(node)


    

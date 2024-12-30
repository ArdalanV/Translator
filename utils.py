import ast
import translations

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
    
def keyword_parser(code, translation_mapping):
    """
    Iterates through the contents of a file's code, translates the keywords of the
    code to the language

    Parameters:
        code (str): The code of the file in a string after being 
                    translating built ins via ast_translation
        translation_mapping (dictionary): Dictionary of translations to be used

    Returns:
        str: File code with keywords successfully translated into target language
    """
    translated_lines = []
    for line in code.split("\n"):
        # Preserve the leading whitespace (indentation)
        leading_whitespace = len(line) - len(line.lstrip())
        indent = " " * leading_whitespace
        
        # Process the rest of the line
        words = line.split()  # Split the line into words
        translated_line = []
        for word in words:
            # Replace the word if it's a keyword in the translation dictionary
            if word in translation_mapping:
                translated_line.append(translation_mapping[word])
            else:
                translated_line.append(word)
        # Reconstruct the translated line with indentation
        translated_lines.append(indent + " ".join(translated_line))

    # Reconstruct the entire translated code
    translated_code = "\n".join(translated_lines)
    return translated_code

def ast_translation(code, translation_mapping):
    """
    Creates an abstract syntax tree (ast) with the file code, then traverses the 
    ast while translating the built ins

    Parameters:
        code (str): The original code of the file needed to be translated
        translation_mapping (dictionary): Dictionary of translations to be used

    Returns:
        str: File code with built ins successfully translated into target language
    """
    #Put file code into an ast
    tree = ast.parse(code)
    #Create translator 
    translator = KeywordTranslator(translation_mapping)
    #Traverse ast
    translated_built_ins = translator.visit(tree)
    modified_code = ast.unparse(translated_built_ins)
    return modified_code
    
def get_lang_mapping(language, direction):
    """
    Finds and picks which language mapping dictionary from translations.py
    to use for the translation algorithm.

    Parameters:
        language (str): Language mapping we want to use for translations
        direction (int): Which direction of translations desired
    """
    if language == "Spanish":
        return translations.Spanish[direction]
    elif language == "Persian":
        return translations.Persian[direction]
    elif language == "German":
        return translations.German[direction]
    elif language == "French":
        return translations.French[direction]
    elif language == "Italian":
        return translations.Italian[direction]
    
def other_to_english(file, language, index):
    pass
    
def english_to_other(input_file, language, index):
    translation_mapping = get_lang_mapping(language, index)
    code = ast_translation(input_file, translation_mapping)
    code = keyword_parser(code, translation_mapping)
    with open("file_testing/test.py", "w", encoding="utf-8") as file:
        file.write(code)
        print(f"Python file test.py successfully created")
    
    

class KeywordTranslator(ast.NodeTransformer):


    def __init__(self, keyword_mapping):
        self.keywords_mapping = keyword_mapping

    def visit_Name(self, node):
        # Translate identifiers like variables or functions
        if node.id in self.keywords_mapping:
            node.id = self.keywords_mapping[node.id]
        return node

    def visit_Call(self, node):
        # Translate the function being called
        if isinstance(node.func, ast.Name) and node.func.id in self.keywords_mapping:
            node.func.id = self.keywords_mapping[node.func.id]

        # Recursively visit arguments to handle nested translations
        node.args = [self.visit(arg) for arg in node.args]
        return self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        # Translate function definitions, including __init__
        if node.name in self.keywords_mapping:
            node.name = self.keywords_mapping[node.name]
        if len(node.args.args) > 0 and node.args.args[0].arg == "self":
            node.args.args[0].arg = self.keywords_mapping["self"]
        return self.generic_visit(node)


    

import utils
import translations
import argparse


def main():
    #Create argument parser
    parser = argparse.ArgumentParser(prog='Translation',
                                     description='Translates Python Files from one language to another',
                                     )
    #Defining command line arguments
    parser.add_argument("--input", required=True, help="Path to the input Python file")
    parser.add_argument("--lang", required=True, help="Target translation language i.e. 'Spanish', 'Farsi'")

    #Parse arguments
    args = parser.parse_args()

    #Get the inputs
    input_file = args.input
    target_language = args.lang

    #Try opening the file and reading
    try:
        file_content = utils.read_file(input_file)
        print(f"Successfully read file: {input_file}")
    except Exception as e:
        print(e)
        return
    
    #Translate from other language to English
    if target_language in utils.Languages:
        return utils.english_to_other(file_content, target_language, 0)
    
    #Check target language, if English then algorithm needs to collapse all languages to English
    elif target_language == "English":
        return utils.other_to_english(file_content, target_language, 1)
    else:
        print(f"Error: Target language '{target_language}' not supported.")
        return
    

if __name__ == "__main__":
    print("Starting script")
    main()
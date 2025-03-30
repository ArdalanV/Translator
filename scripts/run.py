import utils
import argparse
import translations


def main():
    #Create argument parser
    parser = argparse.ArgumentParser(prog='Translation',
                                     description='Translates Python Files from one language to another',
                                     )
    #Defining command line arguments
    parser.add_argument("--input", required=True, help="Path to the input Python file")
    parser.add_argument("--lang1", required=True, help="Language of file's contents")
    parser.add_argument("--lang2", required=True, help="Target language for translation")

    #Parse arguments
    args = parser.parse_args()

    #Get the inputs
    input_file = args.input
    target_language1 = args.lang1
    target_language2 = args.lang2

    #Try opening the file and reading
    try:
        file_content = utils.read_file(input_file)
        print(f"Successfully read file: {input_file}")
    except Exception as e:
        print(e)
        return
    
    #Translate from English to another language
    if target_language1 == "English" and target_language2 in utils.Languages:
        return utils.english_to_other(file_content, target_language2, 0)
    
    #Check target language, if English then algorithm needs to collapse all languages to English
    elif target_language1 in utils.Languages and target_language2 == "English":
        return utils.other_to_english(file_content, target_language1, 1)
    else:
        print(f"Error: Please select a valid translation mapping")
        return
    

if __name__ == "__main__":
    print("Starting script")
    main()
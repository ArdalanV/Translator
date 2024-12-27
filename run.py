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

    #try opening the file and reading
    try:
        file_content = utils.read_file(input_file)
        print(f"Successfully read file: {input_file}")
    except Exception as e:
        print(e)
        return
    
    #translation logic to go here





if __name__ == "main":
    main()
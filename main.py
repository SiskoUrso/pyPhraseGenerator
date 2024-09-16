import json
import sys
from app import PassphraseApp

def load_words_dictionary(file_path):
    """
    Load a words dictionary from the given file path.

    :param str file_path: The file path to the words dictionary.

    :raises FileNotFoundError: If the file at the given path is not found.
    :raises json.JSONDecodeError: If the file at the given path is not valid JSON.

    :return: The loaded words dictionary.
    :type: dict
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        sys.exit(1)

def main():
    words_dictionary = load_words_dictionary("words_dictionary.json")  # Word List with over 460,000 words
    app = PassphraseApp(words_dictionary)
    app.menu()

if __name__ == "__main__":
    main()



#TODO - Make animation that would visualize the password being generated, possible ascii art?
#TODO - find api or option to show password strength?
#TODO - make option to output to privatebin link?
#TODO - Eventually make into an app in django
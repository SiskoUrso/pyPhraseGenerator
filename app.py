import os
from passphrase_generator import PassphraseGenerator, WordGenerator, SpaceProcessor, PhraseProcessor

DEFAULT_CHAR_LIMIT = 40
DEFAULT_CAPITAL_LETTERS = True
DEFAULT_PHRASE_COUNT = 8
DEFAULT_SPACE_TYPE = "numbers"

class PassphraseApp:
    def __init__(self, words_dictionary):
        """
        Initialize a PassphraseApp with the given words dictionary.

        :param dict words_dictionary: A dictionary of words.
        """
        self.words_dictionary = words_dictionary
        self.space_type = DEFAULT_SPACE_TYPE
        self.char_limit = DEFAULT_CHAR_LIMIT
        self.capital_letters = DEFAULT_CAPITAL_LETTERS
        self.phrase_count = DEFAULT_PHRASE_COUNT
        self.personal_phrases_data = {"length": 0, "personal_phrase": ""}
        
        
    def menu(self):
        """
        Prints the main menu and gets user input to determine which method to run next.

        If the user chooses 1, generate_password() is called.
        If the user chooses 2, options() is called.
        If the user chooses 3, the program exits.
        """
        while True:
            self.clear()
            print("Menu\n1. Generate Password\n2. Options\n3. Exit\n" + "-" * 25)
            try:
                menu_choice = int(input("Choose an option: "))
                if menu_choice == 1:
                    self.generate_password()
                elif menu_choice == 2:
                    char_limit, capital_letters, personal_phrases_data, phrase_count, space_type = self.options()
                elif menu_choice == 3:
                    exit()
                else:
                    print("Invalid Choice, must be 1, 2, or 3.")
            except ValueError:
                print("Invalid Input, please enter a number from 1 - 3.")
                
    def generate_password(self):
        """
        Generate a passphrase given the current options.

        If the user has not entered a personal phrase, a random word is generated.

        The PhraseProcessor is called with the current options to generate a list of words.

        The PassphraseGenerator is then called with the selected words and the random space data
        to generate the final passphrase.

        The passphrase is then printed to the user, and the user is asked if they want to generate
        another passphrase.
        """
        self.clear()
        if not self.personal_phrases_data["personal_phrase"]:
            word_generator = WordGenerator(self.words_dictionary)
            default_random_word = word_generator.generate_word()
            self.personal_phrases_data = {"length": len(default_random_word), "personal_phrase": default_random_word}

        space_processor = SpaceProcessor(self.space_type)
        space_data = space_processor.space_processing()

        phrase_processor = PhraseProcessor(
            self.words_dictionary,
            char_limit=self.char_limit,
            capital_letters=self.capital_letters,
            personal_phrases_data=self.personal_phrases_data,
            phrase_count=self.phrase_count,
            space_data=space_data
        )

        selected_words = phrase_processor.process_phrase()
        
        passphrase_generator = PassphraseGenerator(selected_words, space_data)
        password = passphrase_generator.generate_password()

        print(f"Your password is: {password}\n")
        if input("Would you like to create another password? (y/n) \n").lower() != "y":
            exit()
        
    def options(self):
        """
        Let the user choose options for generating a passphrase.

        Asks the user to input the maximum number of characters, whether to include capital letters, a personal phrase,
        the number of phrases, and the type of space character.

        If the user enters nothing for a question, the default value is used.

        When the user is done, generate_password() is called to generate a passphrase with the selected options.
        """
        while True:
            self.clear()
            print("Let's setup your password options, press enter to use default options on any question.\n")
            try:
                char_limit_input = input(f"Enter the maximum number of characters in the password (default {self.char_limit}): ")
                if char_limit_input:
                    self.char_limit = int(char_limit_input)
            except ValueError:
                print("Invalid input. Keeping default character limit.")
                
            capital_letters_input = input(f"Would you like capital letters in your password? (y/n, default {'y' if self.capital_letters else 'n'}): ").lower()
            if capital_letters_input:
                self.capital_letters = capital_letters_input == "y"
            
            personal_phrase_input = input(f"Enter a personal phrase (default '{self.personal_phrases_data['personal_phrase']}'): ").lower().replace(" ", "")
            if personal_phrase_input:
                self.personal_phrases_data = {"length": len(personal_phrase_input), "personal_phrase": personal_phrase_input}
            
            try:    
                phrase_count_input = input(f"Enter the number of phrases in your password (default {self.phrase_count}): ")
                if phrase_count_input:
                    self.phrase_count = int(phrase_count_input)
            except ValueError:
                print("Invalid input. Keeping default phrase count.")
                
            print("Space Types\n1. Letters\n2. Numbers\n3. Symbols\n4. Whitespaces\n" + "-" * 25)
            try:
                space_choice_input = int(input("Choose a space type: "))
                if space_choice_input:
                    space_choice = int(space_choice_input)
                    self.space_type = {1: "letters", 2: "numbers", 3: "symbols", 4: "whitespaces"}.get(space_choice, self.space_type)
            except ValueError:
                print("Invalid input. Keeping default space type.")
            
            self.generate_password()
                
                
    def clear(self):
        """Clear the terminal screen.

        This function works on both Windows and Unix-like systems.
        """
        if os.name == "nt": 
            os.system("cls")           
        else: 
            os.system("clear")
import secrets

class WordGenerator:
    def __init__(self, words_dictionary):
        """
        Initialize a WordGenerator with a given words dictionary.

        :param dict words_dictionary: A dictionary of words.
        """
        self.words_dictionary = words_dictionary
        
    def generate_word(self):
        return secrets.choice(list(self.words_dictionary.keys()))
    
class PhraseProcessor:
    def __init__(self, words_dictionary, char_limit, capital_letters, personal_phrases_data, phrase_count, space_data):
        """
        Initialize a PhraseProcessor with the given parameters.

        :param dict words_dictionary: A dictionary of words.
        :param int char_limit: The maximum number of characters in the generated passphrase.
        :param bool capital_letters: Whether to include capital letters in the generated passphrase.
        :param dict personal_phrases_data: A dictionary containing the personal phrase data.
        :param int phrase_count: The number of phrases to include in the generated passphrase.
        :param callable space_data: A callable that returns a random space character.
        """
        self.words_dictionary = words_dictionary
        self.char_limit = char_limit
        self.capital_letters = capital_letters
        self.personal_phrases_data = personal_phrases_data
        self.phrase_count = phrase_count
        self.space_data = space_data
        
    def process_phrase(self):
        """
        Process a passphrase given a personal phrase, the number of phrases to include, and the maximum number of characters.

        :return: A list of words in the generated passphrase.
        """
        
        user_phrase_length = self.personal_phrases_data["length"]
        personal_phrase = self.personal_phrases_data["personal_phrase"]
        self.char_limit -= user_phrase_length
        
        user_phrase_word_count = 0
        max_word_count = self.phrase_count
        
        selected_words = []
        
        if self.capital_letters:
            personal_phrase = personal_phrase.title()
        selected_words.append(personal_phrase)

            
        while self.char_limit > 0 and user_phrase_word_count < max_word_count:
            total_spaces_length = user_phrase_word_count * len(self.space_data())
            effective_char_limit = self.char_limit - total_spaces_length
            
            filtered_keys = [key for key in self.words_dictionary.keys() if 3 <= len(key) <= effective_char_limit]    
            
            if not filtered_keys:                            
                break
            
            random_word = secrets.choice(filtered_keys)
            if self.capital_letters:
                random_word = random_word.title()
                
            selected_words.append(random_word)       
            self.char_limit -= len(random_word)
            user_phrase_word_count += 1
            
        return selected_words
    
class SpaceProcessor:
    def __init__(self, space_types):
        """
        Initialize a SpaceProcessor with the given space_types.

        :param str space_types: A string indicating the type of space character to use.
            Valid values are "letters", "numbers", "symbols", and "whitespaces".
        """
        self.space_types = space_types
        
    def space_processing(self):
        """
        Returns a function that generates a random space character based on the
        given space_types.

        :param str space_types: A string indicating the type of space character to use.
            Valid values are "letters", "numbers", "symbols", and "whitespaces".
        :return: A function that generates a random space character
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<',
    '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        
        def randomize_space_generator():
            if self.space_types == "letters":
                return secrets.choice(alphabet)
            elif self.space_types == "numbers":
                return str(secrets.randbelow(10))
            elif self.space_types == "symbols":
                return secrets.choice(symbols)
            elif self.space_types == "whitespaces":
                return " "
            
        return randomize_space_generator
    
class PassphraseGenerator:
    def __init__(self, selected_words, space_data):
        """
        Initialize a PassphraseGenerator with a list of selected words and a space data generator.

        :param list selected_words: A list of words to be used in the passphrase.
        :param callable space_data: A function that generates a random space character.
        """
        self.selected_words = selected_words
        self.space_data = space_data

    def generate_password(self):
        """
        Generate a passphrase by joining the selected words with spaces in between.
        
        :return: A string representing the generated passphrase.
        """
        password = "".join([str(self.selected_words[i]) + self.space_data() for i in range(len(self.selected_words) - 1)]) + self.selected_words[-1]
        
        return password


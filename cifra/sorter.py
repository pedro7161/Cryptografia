from helper.constants import ALPHABET_PHRASE
from helper.utils import print_debug

class Sorter():

    @staticmethod
    def create(word):
        alphabet = ALPHABET_PHRASE
        arr1 = Sorter.merge_arrays(word)
        for char in arr1:
            alphabet = alphabet.replace(char, '')

        print_debug(alphabet)
        arr1 = Sorter.merge_arrays(alphabet, arr1)

        return arr1

    @staticmethod
    def merge_arrays(word, arr1 = None):
        if arr1 is None:
            arr1 = []
        for char in word:
            arr1.append(char)
        return arr1

    @staticmethod
    def encrypt_text(sample_text = "", cifra = "", alphabet = ALPHABET_PHRASE):
        encryped_text = []

        for letter in sample_text:
            for position, value in enumerate(cifra):
                if alphabet[position] == letter:
                    encryped_text.append(value)
                elif letter.isspace():
                    encryped_text.append(" ")
                    break
        return encryped_text

    @staticmethod
    def encrypt_text_reverse(sample_text = "", cifra = None, alphabet = ALPHABET_PHRASE):
        if cifra is None:
            cifra = []
        encryped_text = []
        for letter in sample_text:
            for position, value in enumerate(cifra):
                if value == letter:
                    encryped_text.append(alphabet[position])
                elif letter.isspace():
                    encryped_text.append(" ")
                    break
        return encryped_text

    @staticmethod
    def convert_array_to_string(array: list):
        return ''.join(array)

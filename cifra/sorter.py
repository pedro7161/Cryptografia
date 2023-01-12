from helper.constants import ALPHABET_PHRASE, QWERTY_CIPHER
from helper.utils import print_debug

class Sorter():
    @staticmethod
    def create(word):
        querty_cypher = QWERTY_CIPHER
        arr1 = Sorter.merge_arrays(word)
        for char in arr1:
            querty_cypher = querty_cypher.replace(char, '')

        print_debug(querty_cypher)
        arr1 = Sorter.merge_arrays(querty_cypher, arr1)

        return arr1

    @staticmethod
    def merge_arrays(word, arr1 = None):
        if arr1 is None:
            arr1 = []
        for char in word:
            arr1.append(char)
        return arr1

    @staticmethod
    def apply_encryption(sample_text = "", cypher: list = None, reverse = False):
        if cypher is None:
            cypher = []

        encryped_text = []

        for letter in sample_text:
            for position, value in enumerate(cypher):
                if reverse and value == letter:
                    encryped_text.append(ALPHABET_PHRASE[position])
                elif not reverse and ALPHABET_PHRASE[position] == letter:
                    encryped_text.append(value)
                elif letter.isspace():
                    encryped_text.append(" ")
                    break
        return encryped_text

    @staticmethod
    def convert_array_to_string(array: list):
        return ''.join(array)

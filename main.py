from collections import OrderedDict
from cifra.sorter import Sorter

from helper.constants import QWERTY_CIPHER
from helper.utils import clear_screen, print_debug

def print_welcome_text():
    clear_screen()
    print("------------------ LEI Turma B -----------------\n")
    print("Realizado por: Pedro Pinto, Bruno Martins e Pedro Rodrigues\n\n")
    print("Shift/Keyboard Cipher - selecione uma das opções abaixo:\n")

def print_results(encrypted: str, decrypted: str):
    print("------------------ Results ----------------")
    print("\nText encrypted: ", encrypted)
    print("Text decrypted: ", decrypted, "\n")
    input("Press ENTER to return to menu")

def main():
    while True:
        print_welcome_text()
        choise = input("1 - QWERTY method \n2 - QWERTY with custom cypher method\
            \n0 - Finish the program \n\n>> ")

        if choise == "1":
            sample_text = input("\nWrite your text to be encoded using QWERTY cypher: \n>> ")
            qwerty_encrypted = Sorter.apply_encryption(sample_text.lower(), QWERTY_CIPHER)

            print_results(
                Sorter.convert_array_to_string(array = qwerty_encrypted),
                Sorter.convert_array_to_string(
                    Sorter.apply_encryption(qwerty_encrypted, QWERTY_CIPHER, reverse = True))
            )
        elif choise == "2":
            initial_word = "".join(OrderedDict.fromkeys(
                input("\nWrite your cypher text using QWERTY custom method: \n>> ")
            ))
            sampletext = input("\nWrite your text to be encoded: \n>> ")
            cifra = Sorter.create(initial_word.replace(" ", "").lower())
            encrypted_text = Sorter.apply_encryption(sampletext.lower(), cifra)

            print_debug(initial_word, "".join(cifra))

            print_results(
                Sorter.convert_array_to_string(encrypted_text),
                Sorter.convert_array_to_string(
                    Sorter.apply_encryption(encrypted_text, cifra, reverse = True)
                    )
            )
        elif choise == "0":
            break
        else:
            clear_screen()
            input("Invalid selected option. Press ENTER to return to menu")

if __name__ == "__main__":
    main()

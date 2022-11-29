
class sorter():

    def create(word):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        arr1 = sorter.MergeArrays(word)
        for char in arr1:
            alphabet = alphabet.replace(char, '')

        print(alphabet)
        arr1 = sorter.MergeArrays(alphabet, arr1)

        return arr1

    def MergeArrays(word, arr1=[]):
        for char in word:
            arr1.append(char)
        return arr1

    def encrypttext(sampletext, cifra, alphabet="abcdefghijklmnopqrstuvwxyz"):
        encryped_text = []
        for letter in sampletext:
            for position in range(0, len(alphabet)):
                if alphabet[position] == letter:
                    encryped_text.append(cifra[position])
        return encryped_text

    def encrypttextreverse(sampletext="", cifra=[], alphabet="abcdefghijklmnopqrstuvwxyz"):
        encryped_text = []
        for letter in sampletext:
            for position in range(0, len(cifra)):
                if cifra[position] == letter:
                    encryped_text.append(alphabet[position])
                    print(letter, position)

        return encryped_text

    def convertArrayToString(array, str1=""):
        for ele in array:
            str1 += ele
        return str1

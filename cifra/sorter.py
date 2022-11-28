
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

    def encrypttext(sampletext, cifra, textoencriptado=[], alphabet="abcdefghijklmnopqrstuvwxyz"):
        for letter in sampletext:
            for position in range(0, len(alphabet)):
                if alphabet[position] == letter:
                    textoencriptado.append(cifra[position])
        return textoencriptado

    def encrypttextreverse(sampletext, cifra, textoencriptado=[], alphabet="abcdefghijklmnopqrstuvwxyz"):
        for letter in sampletext:
            for position in range(0, len(cifra)):
                if cifra[position] == letter:
                    textoencriptado.append(alphabet[position])
        return textoencriptado

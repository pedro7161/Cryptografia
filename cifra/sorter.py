
class sorter():

    def create(word):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        arr1 = sorter.initialword(word)
        arr2 = []
        for char in arr1:
            for letter in alphabet:
                if letter == char:
                    # inserir o delete
                    print(letter, char)

        for letter in alphabet:
            arr1.append(letter)
        sorter.encrypttext()
        return arr1

    def initialword(word, arr1=[]):
        for char in word:
            arr1.append(char)
        return arr1

    def encrypttext(sampletext, cifra, textoencriptado=[], alphabet="abcdefghijklmnopqrstuvwxyz"):
        for letter in sampletext:
            for position in len(alphabet):
                if cifra[position] == letter:
                    textoencriptado.append(letter)
        return textoencriptado

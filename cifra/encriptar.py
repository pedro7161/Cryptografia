class qwerty():
    def create(word, arr1=[]):
        arr1.append(word)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for k in range(arr1):
            for letra in alphabet:
                if letra != arr1[k]:
                    arr1.append(letra)

from secrets import choice
from cifra.sorter import sorter

from collections import OrderedDict

cifraqwerty = "qwertyuiopasdfghjklzxcvbnm"
Choice = input("1-qwerty metode \n2-second metode \n")

if Choice == "1":
    
    sampletext=input("write your text\n")
    qwertyencrypted = sorter.encrypttext(
    sampletext, cifraqwerty)
    print("texto encriptado usando o metodo qwerty:\n",
    sorter.convertArrayToString(qwertyencrypted))

    print("texto desincreptado usando o metodo qwerty:\n",
    sorter.convertArrayToString(sorter.encrypttextreverse(qwertyencrypted, cifraqwerty)))

elif Choice == "2":

    initialword = input("write a word\n")
    sampletext = input("write your text\n")

    initialword = "".join(OrderedDict.fromkeys(initialword))
    print(initialword)
    cifra = sorter.create(initialword)
    print(cifra)
    encrypted_text = sorter.encrypttext(sampletext, cifra)

    print("texto encriptado: \n", sorter.convertArrayToString(encrypted_text))
    print("texto desincreptado: \n", sorter.convertArrayToString(
    sorter.encrypttextreverse(encrypted_text, cifra)))



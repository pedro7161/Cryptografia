from cifra.sorter import sorter

from collections import OrderedDict

cifraqwerty = "qwertyuiopasdfghjklzxcvbnm"
initialword = "antonio"
sampletext = "ola tudo bem"

initialword = "".join(OrderedDict.fromkeys(initialword))
print(initialword)
cifra = sorter.create(initialword)
print(cifra)
encrypted_text = sorter.encrypttext(sampletext, cifra)

print("texto encriptado: ", sorter.convertArrayToString(encrypted_text))
print("texto desincreptado: ", sorter.convertArrayToString(
    sorter.encrypttextreverse(encrypted_text, cifra)))

qwertyencrypted = sorter.encrypttext(
    sampletext, cifraqwerty)
print("texto encriptado usando o metodo qwerty: ",
      sorter.convertArrayToString(qwertyencrypted))

print("texto desincreptado usando o metodo qwerty: ",
      sorter.encrypttextreverse(qwertyencrypted, cifraqwerty))

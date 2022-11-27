from cifra.sorter import sorter

from collections import OrderedDict

initialword = "antonio"
sampletext = "ola tudo bem"

initialword = "".join(OrderedDict.fromkeys(initialword))
print(initialword)
cifra = sorter.create(initialword)
print(cifra)
textoencriptado = sorter.encrypttext(sampletext)

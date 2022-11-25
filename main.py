from cifra.sorter import sorter

initialword = "pao"
sampletext = "ola tudo bem"

cifra = sorter.create(initialword)
textoencriptado = sorter.encrypttext(sampletext)

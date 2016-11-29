def velocidade(n):
    tempo = ((n/1000)/3600)
    v = int(0.004/tempo)
    return str(v)

lista = []
for i in range(0,145):
    lista.append("0xEE")
for i in range(145,1024):
    lista.append("0x"+velocidade(i))

lista = str(lista)
lista = lista.replace("'","")
lista = lista.replace("[","")
lista = lista.replace("]","")
arquivo = open("pattern.ptn","w")

arquivo.write(lista)
arquivo.close()

print(lista)

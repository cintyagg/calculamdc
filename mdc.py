#Subprogramas
def mdc(i, j):
	return i if not j else mdc(j, i % j)

#Programa Principal
b = []
with open("valor.bin", "rb") as arq:
    byte = arq.read(4)
    while byte:
        b.append(int.from_bytes(byte, byteorder='big'))
        byte = arq.read(4)
i = []
j = []
restrito = b[1] + 1
medida = b[0]
b.pop(0)
comprimento = len(b)

for num in range(comprimento):
    if num % 2 == 0:
        i.append(b[num])
    else:
        j.append(b[num])
for ind in range(0, len(i)):
    print(mdc(i[ind], j[ind]))
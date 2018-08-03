"""
Entradas
	T:  #casaos de prueba
	N:  #numero de piedras
	D:	#distancia entre orillas

	N piedras:
	Una línea con N piedras:
	S: tamaño de la piedra
	M: distancia de la orilla izquierda a la piedra
"""

T= int(input())
for i in range(T):
	N, D = [int(x) for x in input().split()]
	piedras_aux = input().split()
	for idx,piedra in enumerate(piedras_aux):
		piedras_aux[idx] = [piedra.split("-")[0],int(piedra.split()]
	#print(piedras)
	maximo = 0
	piedras2 = []
	#lista de piedras considerando todas pequeñas
	for j in piedras:
		piedras2.append(j[])
		if j[0] == "B":
			piedras2.append(j[])
	piedras2 += [D,D]
	#Saltando piedras
	for idx,piedra in enumerate(piedras[2:]):
		maximo = max(maximo,piedra-piedras2[idx])
	for j in range(len(piedras2)/2):
		if piedras2[2*(j+1)] - piedras2[2*j] > maximo:
			maximo = piedras2[2*(j+1)] - piedras2[2j]
print("Caso {}: {}".format(i+1),maximo)
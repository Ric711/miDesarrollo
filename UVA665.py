# Entradas

# M:

# N:

M=int(input())
for i in range(M):
	#espacio
	input()
	#conjunto vacio
	monedas_falsas = set()
	N,K = [int(x) for x in input().split()]
	#Enumeramos las monedas y suponemos que todas son falsas
	monedas_falsas={x for x in range(1,N+1)}
	for pesaje in range (K):
		datos=[int(x) for x in input().split()]
		#Criterios
		criterio=input()
		# Si son iguales se eliminan
		if criterio == "=":
			monedas_falsas -= {x for x in datos[1:]}
			#si no son iguales se sigue en los datos
			elif criterio == ">" or criterio == "<":
				monedas_falsas &= {x for x in datos[1:]}
		if len(monedas_falsas) ==1:
			print([x for x in monedas_falsas][0])
			if i==M-1:
				pass
			else: 
				print()
		else:
			print(0)
			if i==M-1:
				pass
			else:
				print()







	


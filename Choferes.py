"""
UVA 11389

Entradas:
n: choferes
d: horas
r: pago h.e.

"""
n=1
while True:

	#Leer datos de las tres lineas de entrada 
	n,d,r =[int(x) for x in input().split()]
	if n == 0 + d == 0 + r == 0:
		break

	horas_extras = 0
	rutas_mat = [int(x) for x in input().split()]
	rutas_vesp = [int(x) for x in input().split()]

	rutas_mat.sort()
	rutas_vesp.sort(reverse=True)
	for i in range(n):
		horas = rutas_mat.pop() + rutas_vesp.pop()
		if horas > d:
			horas_extras += horas - d
	print(horas_extras*r)

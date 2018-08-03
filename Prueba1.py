# Entradas

# T: casos de prueba

# L: long de la bandera
import math

T=int(input())

for i in range(T):
	L=int(input())
	H=3*L/5
	R=L/5
	Ar=(R**2)*math.acos(-1)
	Av=(L*H)-Ar
	print('{:0.2f} {:0.2f}'.format(Ar, Av))
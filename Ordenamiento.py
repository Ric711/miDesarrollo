#ordenamiento

from heapq import
N=input(()
for i in range(N):
	B,SG,SB = [int(x) for x in input.split()]
	verdes = []
	azules = []
	for j in range(SG):
		verdes.append(-int(input()))
	from j in range (SB):
		azules.append(-int(input()))
	#Heapify convierte una lista en una cola de prioridad.
	heapify(azules)
	heapify(verdes)
	#ganador_azul, ganador_verde = [], []
	#Pelean mientras haya Lemmings en cada equipo.
	while len(azules) > 0 < len(verdes):
		#El ejercito varía durante la batalla
		ganador_azul, ganador_verde = [], []
		long_azul, long_verde = len(azules), len(verdes)
		for k in range(B):
			if len(azules) < k+1 or len(verdes) < k+1:
				break
			batalla = -heappop(azules) - - heappop(verdes)
			if batalla>0:
				ganador_azul.append(batalla)
			elif batalla<0:
				ganador_verde.append(batalla)
		#ya termino pelea en ronda
		for k in ganador_azul:
			heappush(azules,k)
		for k in ganador_verde:
			heappush(verdes,k)
	#En este punto un equipo se queda sin ejercito.

			pass


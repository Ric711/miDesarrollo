"""
Entradas:
t:


"""
def creaSecuencia(secuencia,i,contador):
	if len(secuencia) < i:
		return secuencia + creaSecuencia(secuencia+str(contador),i-len(secuencia),contador+1)
	else:
		return(secuencia)
t=int(input())
for k in range(t):
	i=int(input())
	secuencia = ""
	auxiliar= ""
	contador = 1
	while len(secuancia):
		auxiliar = str(contador)
		secuencia +=auxiliar
		contador += 1
		pass
	creaSecuencia(secuencia,i,1)
print(secuencia[i-1])
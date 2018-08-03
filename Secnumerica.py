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
	contador += 1
	creaSecuencia(secuencia,i,1)
print(creaSecuencia(secuencia,i,1)[i-1])
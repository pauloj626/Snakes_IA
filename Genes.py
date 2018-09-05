from individuo import *
from JogoCobra import *
from random import choice, randint
import os

def save_dados(I, n, m):
	arq = open("dados/G"+str(n)+"/I"+str(m)+"/dados.txt", "w")
	arq.write(str(I.crm).replace(", ", " ").replace("(", "").replace(")", "\n"))
	arq.write(str(I.lenght))
	arq.close()

Populacao = []
z = []
k = 0
tam_crm = 29
N_Invi  = 300
N_Gera  = 30

print("Wait for folders [...]")
for n in range(N_Gera+1):
	for m in range(N_Invi):
		try:
			os.makedirs("dados/G"+str(n)+"/I"+str(m))
		except:
			pass

while k < N_Invi:
	i = tuple((choice((RIGHT, LEFT, UP, DOWN)) for _ in range(tam_crm)))
	if not i in z:
		z.append(i)
		k += 1

#A parte abaixo foi usada para
#recomeçar a parti de uma dada geração
'''
while k < 1600:
	arq = open("dados/G8/I"+str(k)+"/dados.txt")
	crm = arq.readline().split()
	arq.close()
	print(k)
	l = []
	for i in range(tam_crm):
		l.append(int(crm[i]))
	z.append(tuple(l))
	k += 1

k = 0

while k < N_Invi-1600:
	arq = open("dados/G7/I"+str(k)+"/dados.txt")
	crm = arq.readline().split()
	arq.close()
	print(k+1600)
	l = []
	for i in range(tam_crm):
		l.append(int(crm[i]))
	z.append(tuple(l))
	k += 1
'''

for i in range(N_Invi):
	I = Individuo()
	I.set(z[i])
	Populacao.append(I)

for n in range(8, N_Gera):
	for m in range(N_Invi):
		Populacao[m].write()
		print("Generation : %d,  Individuo : %d"%(n, m))
		os.system("python3 JogoCobra.py")
		Populacao[m].get()
		save_dados(Populacao[m], n, m)
	
	Populacao.sort(reverse = True)

	N_Conse = int(0.45*N_Invi)
	N_Cross = int(0.45*N_Invi)
	N_Mutat = int(0.1*N_Invi)
	N_Rand  = N_Invi - N_Conse - N_Cross - N_Mutat

	Populacao = Populacao[:N_Conse]

	for i in range(N_Cross):
		P = choice(Populacao + 3*Populacao[:int(0.2*N_Conse)]) + choice(Populacao + 3*Populacao[:int(0.2*N_Conse)])
		Populacao.append(P)

	for i in range(N_Mutat):
		P = choice(Populacao)%randint(1, tam_crm)
		Populacao.append(P)

	k = 0
	z_len = len(z)

	while k < N_Rand:
		i = tuple((choice((RIGHT, LEFT, UP, DOWN)) for _ in range(tam_crm)))
		if not i in z:
			z.append(i)
			k += 1

	for i in range(N_Rand):
		I = Individuo()
		I.set(z[z_len+i])
		Populacao.append(I)

for m in range(len(Populacao)):
		Populacao[m].write()
		print("Generation : %d,  Individuo : %d"%(n+1, m))
		os.system("python3 JogoCobra.py")
		Populacao[m].get()
		save_dados(Populacao[m], n+1, m)

Populacao.sort(reverse = True)

Populacao[0].write()
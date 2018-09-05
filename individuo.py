from random import choice, randint
from JogoCobra import *
from time import sleep

RIGHT, LEFT, UP, DOWN = -1, 1, -2, 2

class Individuo:
	global RIGHT, LEFT, UP, DOWN

	def __init__(self):
		pass

	def set(self, Cormossomo):
		self.crm = Cormossomo

	def write(self):
		x = open("IA_example.py", 'r')
		s = x.read()
		x.close()
		
		s = s.replace("alguma_coisa", "%d")
		s = s%tuple(self.crm)

		x = open("IA.py", 'w')
		x.write(s)
		x.close()

	def __add__(self, other):
		I = Individuo()
		l = []
		for i in range(len(self.crm)):
			l.append(choice((self.crm[i], other.crm[i])))

		I.set(tuple(l))
		return I

	def __mod__(self, n):
		I = Individuo()
		l = list(self.crm[:])
		for _ in range(n):
			l[randint(0, len(l)-1)] = choice((RIGHT, LEFT, UP, DOWN))
		I.set(tuple(l))
		return I

	def pontos(self, lenght, time):
		self.lenght = lenght
		self.time = time

	def get(self):
		arq = open("pontos.txt", 'r')
		s = arq.read().split()
		x, y = int(s[0]), float(s[1])
		self.pontos(x, y)
		arq.close()

	def cromossomo(self):
		return tuple(self.crm)

	def __eq__(self, other):
		return (self.lenght == other.lenght) and (self.time == self.time)

	def __lt__(self, other):
		return (self.lenght < other.lenght) or ((self.lenght == other.lenght) and (self.time < self.time))

	def __le__(self, other):
		return (self == other) or (self < other)

	def __gt__(self, other):
		return other < self

	def __ge__(self, other):
		return other <= self

	def __str__(self):
		return "Individuo = " + str(self.crm)


if __name__ == '__main__':
	I = Individuo()
	i = tuple((choice((RIGHT, LEFT, UP, DOWN)) for _ in range(29)))
	I.set(i)
	I.write()
	
	Jogo()

	arq = open("pontos.txt", 'r')
	s = arq.read().split()
	x, y = int(s[0]), float(s[1])
	I.pontos(x, y)

	J = I%10

	J.write()
	
	Jogo()

	arq = open("pontos.txt", 'r')
	s = arq.read().split()
	x, y = int(s[0]), float(s[1])
	J.pontos(x, y)

	print(J < I)
	print(I)
	print(J)

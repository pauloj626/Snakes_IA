from random import choice, randint

x = [(50*i, 50*j) for i in range(20) for j in range(16)]

class Comida:
	def __init__(self, canvas_draw, nome): 
		self.nome = nome
		self.x, self.y = 50*randint(0, 19), 50*randint(0, 15)
		canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'red')

	def newFood(self, pos):
		y = x[:]
		for p in pos[1:]:
			try:
				y.remove(p[:2])
			except:
				pass
		if(len(y) == 0):
			return 0
		
		self.x, self.y = choice(y)

	def draw(self, canvas_draw, canvas_delete):
		canvas_delete(self.nome)
		canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'red')

	def getPos(self):
		return (self.x, self.y)


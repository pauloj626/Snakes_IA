RIGHT, LEFT, UP, DOWN = -1, 1, -2, 2

class ParteCobra:
	def __init__(self, x, y, direction, canvas_draw, nome): 
		self.x = x
		self.y = y
		self.nome = nome
		self.direction  = direction
		if(self.nome != '1'):
			canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'blue')
		else:
			canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'darkblue')

	def move(self, direction):
		global RIGHT, LEFT, UP, DOWN
		
		if(direction + self.direction != 0):
			self.direction = direction
		
		if  (self.direction == RIGHT):
			self.x += 50
		elif(self.direction == LEFT):
			self.x += -50
		elif(self.direction == UP):
			self.y += -50
		else:
			self.y += 50

	def draw(self, canvas_draw, canvas_delete):
		canvas_delete(self.nome)
		if(self.nome != '1'):
			canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'blue')
		else:
			canvas_draw(self.x, self.y, self.x+50, self.y+50, tag = self.nome, fill = 'darkblue')

	def getPos(self):
		return (self.x, self.y, self.direction)


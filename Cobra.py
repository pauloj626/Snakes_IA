from ParteCobra import *

RIGHT, LEFT, UP, DOWN = -1, 1, -2, 2

class Cobra:
	
	global RIGHT, LEFT, UP, DOWN

	def __init__(self, canvas_draw):
		self.direction = RIGHT
		self.cobra = [ParteCobra(50, 250, self.direction, canvas_draw, '1'), ParteCobra(0, 250, self.direction, canvas_draw, '2')]
		self.len   = 2

	def move(self, direction):
		pos_new = self.cobra[0].getPos()
		pos_old = 0
		for i in range(1, self.len):
			pos_old = self.cobra[i].getPos()
			self.cobra[i].move(pos_new[2])
			pos_new = pos_old[:]

		self.cobra[0].move(direction)

	def morreu(self):
		pos0 =  self.cobra[0].getPos()[:2]
		pos  = [self.cobra[i].getPos()[:2] for i in range(1, self.len)]
		if(pos0 in pos):
			return True
		if(pos0[0] < 0 or pos0[1] < 0 or pos0[0] > 950 or pos0[1] > 750):
			return True
		return False

	def get(self):
		return [self.cobra[i].getPos() for i in range(self.len)]

	def draw(self, canvas_draw, canvas_delete):
		for i in range(self.len):
			self.cobra[i].draw(canvas_draw, canvas_delete)

	def cresceu(self, canvas_draw, pos_comida):
		pos = [self.cobra[i].getPos()[:2] for i in range(self.len)]
		if pos_comida in [self.cobra[0].getPos()[:2]]:
			self.len += 1
			x = self.cobra[self.len-2].getPos()
			if x[2] == RIGHT:
				self.cobra.append(ParteCobra(pos[self.len-2][0]-50, pos[self.len-2][1], RIGHT, canvas_draw, str(self.len)))
			if x[2] == LEFT:
				self.cobra.append(ParteCobra(pos[self.len-2][0]+50, pos[self.len-2][1], LEFT , canvas_draw, str(self.len)))
			if x[2] == UP:
				self.cobra.append(ParteCobra(pos[self.len-2][0], pos[self.len-2][1]+50, UP   , canvas_draw, str(self.len)))
			if x[2] == DOWN:
				self.cobra.append(ParteCobra(pos[self.len-2][0], pos[self.len-2][1]-50, DOWN , canvas_draw, str(self.len)))
			return True
		return False
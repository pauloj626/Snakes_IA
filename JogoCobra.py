from Cobra import *
from Comida import *
from tkinter import *
from time import time, sleep
from random import choice

RIGHT, LEFT, UP, DOWN = -1, 1, -2, 2

class Jogo:
	
	global RIGHT, LEFT, UP, DOWN

	def __init__(self):
		self.root   = Tk()
		
		self.canvas = Canvas(self.root, width = 1000, height = 800, bg = 'white', takefocus = 1)
		self.canvas.pack()

		self.direction = RIGHT
		self.rect   = self.canvas.create_rectangle
		self.delete = self.canvas.delete
		self.cobra = Cobra(self.rect)
		self.tempo = time()
		self.comida= Comida(self.rect, 'comida')
		self.update()
		self.root.mainloop()

	def update(self):
		from IA import decision
		
		self.direction = decision(self.comida.getPos(), self.cobra.get(), time() - self.tempo)

		self.cobra.move(self.direction)

		if self.cobra.morreu() or time() - self.tempo > 5:
			self.root.destroy()
			arq = open("pontos.txt", "w")
			arq.write("%d %f"%(self.cobra.len, time() - self.tempo))
			arq.close()
			return 0

		if self.cobra.cresceu(self.canvas.create_rectangle, self.comida.getPos()):
			self.comida.newFood(self.cobra.get())
		
		self.canvas.delete("all")
		self.comida.draw(self.canvas.create_rectangle, self.canvas.delete)
		self.cobra.draw(self.canvas.create_rectangle,  self.canvas.delete)

		self.root.after(10, self.update)

if __name__ == '__main__':
	Jogo()
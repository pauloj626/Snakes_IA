from random import choice
from numpy import arctan2, sqrt
from math import pi
import numpy as np

RIGHT, LEFT, UP, DOWN = -1, 1, -2, 2

def morrera(cobra, direction):
	global RIGHT, LEFT, UP, DOWN

	if direction == RIGHT:
		x = (cobra[0][0]+50, cobra[0][1])

	if direction == LEFT:
		x = (cobra[0][0]-50, cobra[0][1])

	if direction == UP:
		x = (cobra[0][0], cobra[0][1]-50)

	if direction == DOWN:
		x = (cobra[0][0], cobra[0][1]+50)

	pos = [(cb[0], cb[1]) for cb in cobra]

	if x in pos[:len(pos)-1]:
		return True
	if x[0] < 0 or x[0] > 950 or x[1] < 0 or x[1] > 750:
		return True
	return False

def decision(comida, cobra, tempo):
	global RIGHT, LEFT, UP, DOWN

	dir_old = cobra[0][2]

	morre = [morrera(cobra, RIGHT), morrera(cobra, LEFT), morrera(cobra, UP), morrera(cobra, DOWN)]

	if dir_old == RIGHT:
		if morre[0] and morre[2]:
			return alguma_coisa

		if morre[0] and morre[3]:
			return alguma_coisa

		if morre[2] and morre[3]:
			return alguma_coisa

		if morre[0]:
			return alguma_coisa

		if morre[2]:
			return alguma_coisa

		if morre[3]:
			return alguma_coisa

	if dir_old == LEFT:
		if morre[1] and morre[2]:
			return alguma_coisa

		if morre[1] and morre[3]:
			return alguma_coisa

		if morre[2] and morre[3]:
			return alguma_coisa

		if morre[1]:
			return alguma_coisa

		if morre[2]:
			return alguma_coisa

		if morre[3]:
			return alguma_coisa

	if dir_old == UP:
		if morre[0] and morre[1]:
			return alguma_coisa

		if morre[0] and morre[2]:
			return alguma_coisa

		if morre[1] and morre[2]:
			return alguma_coisa

		if morre[0]:
			return alguma_coisa

		if morre[1]:
			return alguma_coisa

		if morre[2]:
			return alguma_coisa

	if dir_old == DOWN:
		if morre[0] and morre[1]:
			return alguma_coisa

		if morre[0] and morre[3]:
			return alguma_coisa

		if morre[1] and morre[3]:
			return alguma_coisa

		if morre[0]:
			return alguma_coisa

		if morre[1]:
			return alguma_coisa

		if morre[3]:
			return alguma_coisa

	a = cobra[0][0] - comida[0]
	b = cobra[0][1] - comida[1]

	if a > 0 and cobra[0][2] != RIGHT:
		return alguma_coisa
	elif a < 0 and cobra[0][2] != LEFT:
		return alguma_coisa
	elif b > 0 and cobra[0][2] != DOWN:
		return alguma_coisa
	elif b < 0 and cobra[0][2] != UP:
		return alguma_coisa
	return alguma_coisa
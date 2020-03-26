import os 
import time
import keyboard
from termcolor import colored

import config as c

# def print_pressed_keys(e):
#     print(e.name)


# keyboard.hook(print_pressed_keys)
# keyboard.wait()

def print_c():
	os.system('cls')
	for i in range(c.heigth):
		for j in range(c.weigth):
			if (i == c.start_h) and (j == c.start_w):
				print(colored(c.sumbol_1, 'red'), end='')
			else:
				print(c.matrix[i][j], end='')
		print()

print_c() 

def up():
	c.start_h-=1
	if c.start_h < 0:
		c.start_h = 1
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2
	print_c()	

def down():
	c.start_h+=1
	if c.start_h > c.heigth - 1:
		c.start_h = c.heigth - 1
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2
	print_c()

def right():
	c.start_w+=1
	if c.start_w > c.weigth - 1:
		c.start_w = c.weigth - 1
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2
	print_c()

def left():
	c.start_w-=1
	if c.start_w < 0:
		c.start_w = 0
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2
	print_c()

def mode():
	c.mode = 0 if c.mode else 1
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2

keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', right)
keyboard.add_hotkey('left', left)
keyboard.add_hotkey('m', mode)
keyboard.wait('Esc')
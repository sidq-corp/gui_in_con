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
	c.matrix[c.old_h][c.old_w] = c.sumbol_1 if c.mode else c.sumbol_2
	c.matrix[c.start_h][c.start_w] = colored(c.sumbol_1, 'red')
	c.old_h = c.start_h
	c.old_w = c.start_w
	for i in range(c.heigth):
		print(''.join(c.matrix[i]))

print_c() 

def circle():
	d = int(input())
	c.start_h += d//2
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2
	for i in range(round(d/2)):
		print_c()


def pall():
	c.matrix = [[c.sumbol_1 for i in range(c.weigth) ] for i in range(c.heigth)]
	print_c()

def up():
	c.start_h-=1
	if c.start_h < 0:
		c.start_h = 1
	print_c()	

def down():
	c.start_h+=1
	if c.start_h > c.heigth - 1:
		c.start_h = c.heigth - 1
	print_c()

def right():
	c.start_w+=1
	if c.start_w > c.weigth - 1:
		c.start_w = c.weigth - 1
	print_c()

def left():
	c.start_w-=1
	if c.start_w < 0:
		c.start_w = 0
	print_c()

def mode():
	c.mode = 0 if c.mode else 1
	c.matrix[c.start_h][c.start_w] = c.sumbol_1 if c.mode else c.sumbol_2

keyboard.add_hotkey('c', circle)
keyboard.add_hotkey('n', pall)
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', right)
keyboard.add_hotkey('left', left)
keyboard.add_hotkey('m', mode)
keyboard.wait('Esc')
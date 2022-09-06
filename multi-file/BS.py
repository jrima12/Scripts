import random
import string
import sys
import time
import os
from unittest import removeHandler
from termcolor import *

List = open('dumbList.txt').readlines()

os.system('clear')

r = random.randint(0,100)
count = 0

r2 = random.randint(50, 200)
count2 = 0

rRed = random.randint(10,30)
countRed = 0

rCyan = random.randint(10,40)
countCyan = 0

rWhite = random.randint(10,30)
countWhite = 0

rMagenta = random.randint(10,40)
countMagenta = 0

rLoad = random.randint(20,30)
countLoad = 0

textColor = "green"

def delay_print(st):
	for c in st:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.008)
	sys.stdout.write("\n")


def progressBar():
	sys.stdout.write("Progress => ")
	for i in range(random.randint(40,100)):
		sys.stdout.write("=")
		sys.stdout.flush()
		time.sleep(random.randint(5, 15)/45)
	sys.stdout.write("\n")

def loadingBar():
	sys.stdout.write("Loading")
	for i in range(random.randint(40,100)):
		sys.stdout.write(".")
		sys.stdout.flush()
		time.sleep(.1)
	sys.stdout.write("\n")

while True:
	if count == r:
		sys.stdout.write(colored(random.choice(List),"red", attrs=["bold", "blink"]))
		time.sleep(1)
		progressBar()
		r = random.randint(0,100)
		count = 0
	else:
		if count2 == r2:
			os.system('clear')
			r2 = random.randint(5,20)
			count2 = 0
		else:
			if countRed == rRed:
				textColor =  "red"
				rRed = random.randint(10,40)
				countRed = 0
				for i in range(random.randint(0,4)):
					ch = string.ascii_letters + string.digits + string.punctuation
					st = colored("".join(random.choice(ch) for i in range(random.randint(20,200))), textColor)
					delay_print(st)
			if countCyan == rCyan:
				textColor =  "cyan"
				rCyan = random.randint(10,40)
				countCyan = 0
				for i in range(random.randint(0,4)):
					ch = string.ascii_letters + string.digits + string.punctuation
					st = colored("".join(random.choice(ch) for i in range(random.randint(20,200))), textColor)
					delay_print(st)
			if countWhite == rWhite:
				textColor =  "white"
				rWhite = random.randint(10,40)
				countWhite = 0
				for i in range(random.randint(0,4)):
					ch = string.ascii_letters + string.digits + string.punctuation
					st = colored("".join(random.choice(ch) for i in range(random.randint(20,200))), textColor)
					delay_print(st)
			if countMagenta == rMagenta:
				textColor =  "magenta"
				rMagenta = random.randint(10,40)
				countMagenta = 0
				for i in range(random.randint(0,4)):
					ch = string.ascii_letters + string.digits + string.punctuation
					st = colored("".join(random.choice(ch) for i in range(random.randint(20,200))), textColor)
					delay_print(st)
			if countLoad == rLoad:
				loadingBar()
				rLoad = random.randint(20, 100)
				countLoad = 0
			textColor = "green"
			ch = string.ascii_letters + string.digits + string.punctuation
			st = colored("".join(random.choice(ch) for i in range(random.randint(7,100))), textColor)
			delay_print(st)
	time.sleep(random.randint(0,10)/100)
	count+=1
	countRed+=1
	countCyan+=1
	countWhite+=1
	countMagenta+=1
	countLoad += 1

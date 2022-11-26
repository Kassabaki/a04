import random

def guess(x):
	random_number=random.randint(1,x)
	guess = 0
	print(f'congrats. you have guessed the number {x} correctly')

guess(10)

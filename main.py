import random

def guess(x):
	random_number=random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'guess a number between 1 and {x}: '))
		if guess < random_number:
			print('sorry guess again. number too low.')
		elif guess > random_number:
			print('Sorry guess again. Number too high.')
	print(f'congrats. you have guessed the number {x} correctly')

guess(10)

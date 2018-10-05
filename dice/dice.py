from random import randint

class Die():
	def __init__(self, num_size=6):
		self.num_size = num_size

	def roll(self):
		return randint(1, self.num_size)

		

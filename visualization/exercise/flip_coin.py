from random import randint
import pygal

class Coins():
	def __init__(self, sides=2):
		self.sides = sides

	def flip_coins(self):
		return randint(1, self.sides)

coins = Coins()

results = []

for flip_num in range(10000):
    result = coins.flip_coins()
    results.append(result)

frequencies = []
for value in range(1, coins.sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'results of flipping one coin 10000 times'
hist.x_labels = ['1', '2']
hist.x_title = 'result'
hist.y_title = 'frequency'

hist.add('coin', frequencies)
hist.render_to_file('flip_coin.svg')

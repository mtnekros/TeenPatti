from Card import *
import random

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ['Club','Spade','Diamond','Heart']:
			for value in range(1,14):
				self.cards.append(Card(value, suit))

	def shuffle(self):
		random.shuffle(self.cards)

	def drawCard(self):
		return self.cards.pop()

	def show(self):
		for i,card in enumerate(self.cards):
			print i, 
			card.show()

	def getNumberOfCards(self):
		return len(self.cards)
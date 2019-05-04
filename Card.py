class Card:
	cardRanks = tuple(['Ace'] + range(2,11) + ['Jack', 'Queen', 'King']) #used when printing the card to user

	def __init__(self, value, suit):
		self.suit = suit
		self.value = value

	# returns ace Corrected value(ace changed to 14 i.e highest, rest kept the same), useful when comparing card value
	@property
	def valueAceCorrected(self):
		return 14 if self.value==1 else self.value 

	# returns value for printing ('Ace' for 1 etc)
	@property
	def valueForShow(self):
		return Card.cardRanks[self.value - 1]

	def show(self):
		print '{} of {}'.format(self.valueForShow, self.suit)
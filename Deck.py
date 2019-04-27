import random 

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

class HandInfo:

	@staticmethod
	def isTrial(hand):
		return len(set([card.value for card in hand])) == 1

	@staticmethod
	def isPureSequence(hand):
		return HandInfo.isFlush(hand) and HandInfo.isSequence(hand)

	@staticmethod
	def isSequence(cards):
		values = sorted( [card.value for card in cards] )
		possibleSequence = range(min(values), min(values)+len(values))
		return values == possibleSequence or values == [1, 12, 13] # normal sequence or ace-king-queen

	@staticmethod
	def isFlush(hand):
		suit = hand[0].suit
		return all([suit == card.suit for card in hand])	

	@staticmethod
	def hasPair(hand):
		return len(set([card.value for card in hand])) == 2

	# returns ace Corrected value(ace changed to 14 or highest), useful when comparing pair
	@staticmethod
	def getPairValue(hand):
		assert( HandInfo.hasPair(hand) )
		handCardValues = [card.valueAceCorrected for card in hand] 
		return max( set( handCardValues ), key=handCardValues.count )
		return 0

	@staticmethod
	def getRank(hand): # returns tuple of int rank based on whether it's flush, sequence, trial, etc and the rank name as string
		if HandInfo.isTrial(hand):
			return 5, 'Trial'
		elif HandInfo.isPureSequence(hand):
			return 4, 'PureSequence'
		elif HandInfo.isSequence(hand):
			return 3, 'Sequence'
		elif HandInfo.isFlush(hand):
			return 2, 'Flush'
		elif HandInfo.hasPair(hand):
			return 1, 'Pair'
		else:
			return 0, 'High Card'


class HandCompare:
	@staticmethod
	def valuesCompare(hand1, hand2):
		# initalizing lists containing values of hand1 and hand2 cards
		hand1_values = [card.value for card in hand1]
		hand2_values = [card.value for card in hand2]
		# replacing Ace or 1 with 14 because Ace is actually the highest value
		hand1_values = list( map( lambda x: 14 if x==1 else x, hand1_values) )
		hand2_values = list( map( lambda x: 14 if x==1 else x, hand2_values) )
		#arranging the handvalues in descending order
		hand1_values.sort(reverse=True)
		hand2_values.sort(reverse=True)
		# using list comparison to compare cards arranged in descending order
		if  hand1_values > hand2_values: 
			return 1
		elif hand1_values < hand2_values:
			return -1
		else:
			return 0

	@staticmethod
	def pairCompare(hand1, hand2):
		pair1 = HandInfo.getPairValue(hand1)
		pair2 = HandInfo.getPairValue(hand2)
		if pair1 > pair2:
			return 1
		elif pair1 < pair2:
			return -1
		else:
			return HandCompare.valuesCompare(hand1, hand2)

	@staticmethod
	def compare(hand1, hand2):
		rankHand1 = HandInfo.getRank(hand1)
		print 'Hand1 is', rankHand1[1]
		rankHand2 = HandInfo.getRank(hand2)
		print 'Hand2 is', rankHand2[1],'\n'

		if rankHand1[0] > rankHand2[0]:
			return 1
		elif rankHand1[0] < rankHand2[0]:
			return -1
		else: # if rank is equal
			if rankHand1[1] == "Pair":
				return HandCompare.pairCompare(hand1, hand2)
			else:
				return HandCompare.valuesCompare(hand1, hand2)

def gameRound():
	deck = Deck()
	deck.shuffle()

	handOfPlayer1 = [Card(11,'Spade'),Card(12,'Diamond'),Card(13,'Diamond')]
	handOfPlayer2 = [Card(13,'Spade'),Card(1,'Diamond'),Card(12,'Diamond')]

	'''
	# distributing cards to player
	for i in range(3):
		handOfPlayer1.append(deck.drawCard())
		handOfPlayer2.append(deck.drawCard())
	'''

	print "Player1's hand is:"
	for card in handOfPlayer1:
		card.show()
	print

	print "Player2's hand is:"
	for card in handOfPlayer2:
		card.show()
	print

	result = HandCompare.compare(handOfPlayer1, handOfPlayer2)
	if result > 0:
		print "Player1 Won!"
	elif result < 0:
		print "Player2 Won!"
	else:
		print "It's a draw!"


if __name__ == '__main__':
	while True:
		gameRound()
		raw_input("Press Enter to continue!")



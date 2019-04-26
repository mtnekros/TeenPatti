import random 

class Card:
	def __init__(self, value, suit):
		self.suit = suit
		self.value = value

	def show(self):
		print '{} of {}'.format(self.value, self.suit)


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
		return values == possibleSequence

	@staticmethod
	def isFlush(hand):
		suit = hand[0].suit
		return all([suit == card.suit for card in hand])	

	@staticmethod
	def hasPair(hand):
		return len(set([card.value for card in hand])) == 2

	@staticmethod
	def getPairValue(hand):
		if (HandInfo.hasPair(hand)):
			return max(set(hand),key = hand.count)
		return 0

	@staticmethod
	def getRank(hand): # returns int rank based on whether it's flush, sequence, trial, etc
		if HandInfo.isTrial(hand):
			return 5,'Trial'
		elif HandInfo.isPureSequence(hand):
			return 4,'PureSequence'
		elif HandInfo.isSequence(hand):
			return 3,'Sequence'
		elif HandInfo.isFlush(hand):
			return 2,'Flush'
		elif HandInfo.hasPair(hand):
			return 1,'Pair'
		else:
			return 0,'None'


class HandCompare:
	@staticmethod
	def valuesCompare(hand1, hand2):
		hand1_values = list( reversed( sorted( [card.value for card in hand1] ) ) )
		hand2_values = list( reversed( sorted( [card.value for card in hand2] ) ) )
		if  hand1_values > hand2_values:
			return 1
		elif hand1_values < hand2_values:
			return -1
		else:
			return 0

	@staticmethod
	def pairCompare(hand1, hand2):
		if HandInfo.getPairValue(hand1) > HandInfo.getPairValue(hand2):
			return 1
		elif HandInfo.getPairValue(hand1) > HandInfo.getPairValue(hand2):
			return -1
		else:
			return HandCompare.valuesCompare(hand1, hand2)

	@staticmethod
	def compare(hand1, hand2):
		rankP1 = HandInfo.getRank(hand1)
		print 'Hand1 is', rankP1[1]
		rankP2 = HandInfo.getRank(hand2)
		print 'Hand2 is', rankP2[1]
		print

		if rankP1[0] > rankP2[0]:
			return 1
		elif rankP1[0] < rankP2[0]:
			return -1
		else: # if rank is equal
			if rankP1[1] == "Pair":
				return HandCompare.pairCompare(hand1, hand2)
			else:
				return HandCompare.valuesCompare(hand1, hand2)



if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()

	handOfPlayer1 = []
	handOfPlayer2 = []
	for i in range(3):
		handOfPlayer1.append( deck.drawCard() )
		handOfPlayer2.append( deck.drawCard() )

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
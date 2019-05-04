''' This module contains all the functions for getting the information of a players '''

def isTrial(hand):
	return len(set([card.value for card in hand])) == 1

def isPureSequence(hand):
	return isFlush(hand) and isSequence(hand)

def isSequence(cards):
	values = sorted( [card.value for card in cards] )
	possibleSequence = range(min(values), min(values)+len(values))
	return values == possibleSequence or values == [1, 12, 13] # normal sequence or ace-king-queen

def isFlush(hand):
	suit = hand[0].suit
	return all([suit == card.suit for card in hand])	

def hasPair(hand):
	return len(set([card.value for card in hand])) == 2

# returns ace Corrected value(ace changed to 14 or highest), useful when comparing pair
def getPairRankFrom(hand):
	assert( hasPair(hand) )
	handCardValues = [card.valueAceCorrected for card in hand] 
	return max( set( handCardValues ), key=handCardValues.count )
	return 0

def getRank(hand): # returns tuple of int rank based on whether it's flush, sequence, trial, etc and the rank name as string
	if isTrial(hand):
		return 5, 'Trial'
	elif isPureSequence(hand):
		return 4, 'Pure Sequence'
	elif isSequence(hand):
		return 3, 'Sequence'
	elif isFlush(hand):
		return 2, 'Flush'
	elif hasPair(hand):
		return 1, 'Pair'
	else:
		return 0, 'High Card'


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

def pairCompare(hand1, hand2):
	pair1 = getPairRankFrom(hand1)
	pair2 = getPairRankFrom(hand2)
	if pair1 > pair2:
		return 1
	elif pair1 < pair2:
		return -1
	else:
		return valuesCompare(hand1, hand2)

def compareTwoHands(hand1, hand2):
	rankHand1 = getRank(hand1)
	rankHand2 = getRank(hand2)

	if rankHand1[0] > rankHand2[0]:
		return 1
	elif rankHand1[0] < rankHand2[0]:
		return -1
	else: # if rank is equal
		if rankHand1[1] == "Pair":
			return pairCompare(hand1, hand2)
		else:
			return valuesCompare(hand1, hand2)

# to compare a list of hands
def compare(hands):
	handCopy = hands[:]
	for i in range(len(handCopy) - 1):
		if compareTwoHands(handCopy[i], handCopy[i+1]) == 1:
			handCopy[i], handCopy[i+1] = handCopy[i+1],handCopy[i]
	return handCopy[-1]
		
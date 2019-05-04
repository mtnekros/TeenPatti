import Hand
import Deck


def gameRound():
	deck = Deck.Deck()
	deck.shuffle()

	hands =[]
	# adding 5 player or hands of player in hand
	for i in range(5):
		hands.append([])

	# distributing cards to player
	for i in range(3):
		for hand in hands:
			hand.append(deck.drawCard())

	for i,hand in enumerate(hands):
		print "Player{}'s hand is:".format(i+1)
		for card in hand:
			card.show()
		print

	for i,hand in enumerate(hands):
		print 'Player{} has a {}'.format(i+1, Hand.getRank(hand)[1])
	print

	winningHand = Hand.compare(hands)
	iWinningPlayer = hands.index(winningHand)
	print "Player{} wins!!!".format(iWinningPlayer+1)

if __name__ == '__main__':
	while True:
		gameRound()
		raw_input("Press Enter to continue!\n")

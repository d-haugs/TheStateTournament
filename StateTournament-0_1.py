import random



class Bracket(object):
	def __init__(self):
		print "Bracket initialized vanilla constructor"

	def __init__(self, file):
		fileCheckResult = checkBracketFile(file)
		print "Bracket initialized by file: %s" % fileCheckResult
	def checkBracketFile(file):
		print "Checking %s" % file
		return "Success"

	# class BracketBranch(object):
	# 	BracketBranch left = 0
	# 	BracketBranch right = 0
	# 	def __init__(self):


class deck(object):
	_cards = 7
	_players = 2
	deckList = []
	playerHands = []
	cardDictionary = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
	#constructor
	def __init__(self):
		for y in {'C', 'D', 'H', 'S'}:	
			for x in {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}:
				self.deckList.append((x,y))

	#shuffle
	def shuffle(self):
		random.shuffle(self.deckList)

	#deal
	def defaultDeal(self, burn = 0):
		print "confirming parameters: cards %i, players %i" % (self._cards, self._players)
		print "Burn: %i" % burn
		if(burn < 52 - (self._cards * self._players)):
			print "Cards accounted for: %i" % (burn + self._cards * self._players)
			print "burn is good"
		else:
			print "Too many cards used"
			return
		for p in range(self._players):
			self.playerHands.append([])
			print "player %i has cards:" % (p + 1)
			for c in range(self._cards):
				card = self.deckList.pop() 
				print card
				self.playerHands[p].append(card)
			print ""
		print self.playerHands[0][0]

	def deal(self, cards = _cards, players = _players, burn = 0):
		cardsTemp = self._cards
		playersTemp = self._players
		self._cards = cards
		self._players = players
		self.defaultDeal(burn)
		self._cards = cardsTemp
		self._players = playersTemp

	def dealAndUpdate(self, cards = _cards, players = _players, burn = 0):
		cardsTemp = self._cards
		playersTemp = self._players
		self._cards = cards
		self._players = players
		self.defaultDeal(burn)

	#Comparison
	def compareAllSets(self):
		scores[self._players]
		for c in range(self._cards):
			

		return scores

	#Settings
	def setCards(self, newCardCount):
		self._cards = newCardCount

	def setPlayers(self, newPlayerCount):
		self._players = newPlayerCount

	def restoreDefaults(self):
		self._cards = 7
		self._players = 2

myDeck = deck()
myDeck.shuffle()
myDeck.deal(8)
print myDeck.playerHands[0][0]
print myDeck.playerHands[1][0]
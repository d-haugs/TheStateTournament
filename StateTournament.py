import random

CardList = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
SuitList = {'C', 'D', 'H', 'S'}

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
	deckList = []
	representativeList = []
	#constructor
	def __init__(self):
		for y in SuitList:	
			for x in CardList:
				self.deckList.append((x,y))

	#Selection
	def representativeSelection():
		#TODO: this function will decide on the cards to represent each team and elaborate on the decision making process.
		for c in CardList:
			self.representativeList.append(c)
		self.representativeList.shuffle()
		# A list of quips should be randomly selected from in order to keep it a little fresher over several runs
			#This is a frosting feature
		pass

	#shuffle
	def shuffle(self):
		random.shuffle(self.deckList)

	#draw
	def drawSingleCard(self):
		pass
	def drawAllCards(self):
		for x in range(7):
			drawSingleCard()

myDeck = deck()

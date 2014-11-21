#The Goals:
#Eventually, this code will become the prototype for a semiautomated State Tournament server. 
#The server will hold an internal list of MN cities and Towns. 
#The server is to maintain bracket seeding based on wins and losses from previous State Tournements
#The server will provide a "grace period" to allow human opporators to begin running ST matches manually during the "preseason". 
#To ensure the Tournament is held annually, the server is to begin executing matches at the beginning "season" and finish by the end of the "season."
#The "Season" is to be determined at a future date. It is intended to allow sufficient time to let humans play out the entirety of the tournament in a proactive fashion.
#The server is intended as a fall back for manually holding the State Tournament.
#The server will automatically generate brackets upon request or at the beginning of the season, which ever comes first.
#Once brackets are generated, they are to be final for the year.
#The time scale for the tournament bracket deadlines will give greater weight to allow later matches more time for hype.
#Partially as a programming exercise as much as anything, the server is intended to provide an RSS feed and/or operate a Twitter account.

import random

#At one point I was mistaken about this being like a 7 hand game of war. There are names and code reflecting this mistaken understanding.


CardList = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
SuitList = {'C', 'D', 'H', 'S'}
realMode = False


matchQuips = [
	"Matches will ahve quips before they occur",
	"Second Quip",
]

#TODO: make brackets useful
#Consider making Brackets a seperate source file since it should be reusable

#######
# http://codereview.stackexchange.com/questions/17703/using-python-to-model-a-single-elimination-tournament
# http://stackoverflow.com/questions/8355264/tournament-bracket-placement-algorithm
# http://stackoverflow.com/questions/2733663/tournament-bracket
#######
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
	rep1 = ''
	p1score = 0
	p1Suits = []
	rep2 = ''
	p2score = 0
	p2Suits = []
	#constructor
	def __init__(self):
		pass

	#Selection
	def representativeSelection(self):
		#TODO: this function will decide on the cards to represent each team and elaborate on the decision making process.
		for c in CardList:
			self.representativeList.append(c)
		random.shuffle(self.representativeList)
		# A list of quips should be randomly selected from in order to keep it a little fresher over several runs
			#This is a frosting feature
		self.rep1 = self.representativeList.pop()
		self.rep2 = self.representativeList.pop()

		for i in range(8):
			self.deckList.append(self.rep1)
			self.deckList.append(self.rep2)

	#shuffle
	def shuffle(self):
		random.shuffle(self.deckList)

	#draw
	def drawSingleCard(self):
		retStr = self.deckList.pop()# + random(SuitList)
		if retStr == self.rep1:
			self.p1score += 1
		else:
			if retStr == self.rep2:
				self.p2score += 1
			else:
				print "Scoring error"
		return retStr
	def drawAllCards(self):
		for x in range(7):
			drawSingleCard()

myDeck = deck()
myDeck.representativeSelection()
myDeck.shuffle()
print "Player 1 has selected %s to represent them this round." % myDeck.rep1
print "Player 2 has selected %s to represent them this round." % myDeck.rep2
for i in range(7):
	print matchQuips[random.randint(0, len(matchQuips)-1)]
	if realMode:
		raw_input(myDeck.drawSingleCard() + '\t P1(%s): %i  P2(%s): %i' % (myDeck.rep1, myDeck.p1score, myDeck.rep2, myDeck.p2score))
	else:
		print myDeck.drawSingleCard() + '\t P1(%s): %i  P2(%s): %i' % (myDeck.rep1, myDeck.p1score, myDeck.rep2, myDeck.p2score)



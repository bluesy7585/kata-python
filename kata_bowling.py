# kata bowling
class bowling:	
	'bowling class in bowling kata'	
	def __init__(self):
		self.rolls = [0 for i in range(0,21)]
		self.frameIndex = 0
		
	def roll(self,knot):		
		self.rolls[self.frameIndex] = knot					
		self.frameIndex = self.frameIndex+1
		
	def getScore(self):	
		score = 0
		rInd = 0;
		for frame in range(0,10):
			r1 = self.rolls[rInd]
			r2 = self.rolls[rInd+1]
			#if r1 == 10:				
			if self.isStrike(rInd):
				score += 10 + r2 + self.rolls[rInd+2]				
				rInd += 1
			elif self.isSpare(rInd):				
				score += 10 + self.rolls[rInd+2]				
				rInd += 2
			else:				
				score += r1 + r2
				rInd += 2
			
		return score
		
	def isStrike(self,rollIndex):
		return self.rolls[rollIndex] == 10
		
	def isSpare(self,rollIndex):
		return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10


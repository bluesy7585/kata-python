class MineSweeper():
	def __init__(self):		
		self.rowNum = 0
		self.colNum = 0
		self.field = []
	
	def resolve(self,input):	
	
		N,M = self.parseFieldSize(input)				
		# init mine field
		self.field = [[0 for x in range(M)] for y in range(M)] 	
		
		# record mine locations
		lines = input.split('\n')	
		lines = lines[1:]
		mineLocation = []	
		for row in range(0,N):	
			line = lines[row]
			for col in range(0,M):
				c = line[col]
				if c == '*':
					self.field[row][col] = '*'
					mineLocation.append([row,col])
				
		for lo in mineLocation:
			self.addValueToNeighbor(lo[0],lo[1])				
						
		return self.createOutputString()
	
	def createOutputString(self):
		out = ''
		# create output string
		for row in range(0,self.rowNum):		
			for col in range(0,self.colNum):	
				check = self.field[row][col]
				out += str(check)
			out += '\n'	
		return out.rstrip('\n')
	
	def addValueToNeighbor(self,row,col):		
		shift = [-1,0,1]		
		for rs in shift:
			for cs in shift:
				r = row + rs
				c = col + cs
				self.addValue(r,c)
	
	def addValue(self,row,col):
		if row >= 0 and row < self.rowNum and col >= 0 and col < self.colNum:
			if self.field[row][col] != '*':
				self.field[row][col] += 1
		
		
	def parseFieldSize(self,input):
		firstline = input.split('\n')[0]
		sp = firstline.split(' ')
		self.rowNum = int(sp[0])
		self.colNum = int(sp[1])
		return [self.rowNum,self.colNum]
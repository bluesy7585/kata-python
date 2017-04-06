class Calculator:
	'Calculator class in kata StringCalculator'
	def add(self,number):
		delim = ','
		
		if self.isCustomDelimiter(number):
			delim = self.GetCustomDelimiter(number)
			number = number[4:]
					
		if len(number) > 0:			
			numls = number.split(delim)						
			numls = self.splitThenAppend(numls,'\n')						
			return self.convertToNumber(numls)
		else:
			return 0
	
	def convertToNumber(self,numls):		
		sum = 0
		mesg = 'negatives not allowed:'		
		isNegative = False
		for num in numls:
			val = int(num)
			if val < 0:
				mesg += ' ' + num
				isNegative = True
			else:
				sum += val
		if isNegative:
			raise NegativeNumberException(mesg)	
		return sum	
		
	def splitThenAppend(self,num_list,sp):		
		num2conv = []
		for num in num_list:						
			if num.count(sp) > 0:
				split = num.split(sp)				
				num2conv.extend(split)
			else:
				num2conv.append(num)
		return num2conv	
		
	def isCustomDelimiter(self,line):
		return line.startswith('//')
		
	def GetCustomDelimiter(self,line):
		return line[2]

class NegativeNumberException(Exception):
	pass		
		

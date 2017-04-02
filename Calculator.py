class Calculator:
	'Calculator class in kata StringCalculator'
	def add(self,number):
		delim = ','
		
		if self.isCustomDelimiter(number):
			delim = self.GetCustomDelimiter(number)
			number = number[4:]
			
		re = 0
		if len(number) > 0:
			numls = number.split(delim)			
			numls = self.splitThenAppend(numls,'\n')
			for num in numls:
				re += int(num)
		return re
		
	def splitThenAppend(self,num_list,sp):		
		num2conv = []
		for num in num_list:						
			if num.count(sp) > 0:
				split = num.split(sp)
				num2conv.extend(split)
			else:
				num2conv.extend(num)
		return num2conv	
		
	def isCustomDelimiter(self,line):
		return line.startswith('//')
		
	def GetCustomDelimiter(self,line):
		return line[2]
		

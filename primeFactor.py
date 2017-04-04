class primeFactor:
	'primeFactor class in kata primeFactor'
	def generate(self,num):
		ls = []		
		den = 2
		while num > 1:
			while num % den == 0:
				ls.append(den)
				num /= den		
			den += 1				
		return ls		
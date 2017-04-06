import unittest
import kata_bowling as bow

class TestBowling(unittest.TestCase):
	def setup(self):
		pass
	def tearDown(self):
		pass

	def roll_many(self,obj,times,bins):
		for i in range(0,times):
			obj.roll(bins)
			
	def test_allZeros(self):
		b = bow.bowling()
		self.roll_many(b,20,0)
		self.assertEqual(b.getScore(),0)		
	
	def test_allOnes(self):
		b = bow.bowling()
		self.roll_many(b,20,1)
		self.assertEqual(b.getScore(),20)
	
	def test_sparse(self):
		b = bow.bowling()
		self.roll_many(b,1,5)
		self.roll_many(b,1,5)
		self.roll_many(b,1,3)
		self.roll_many(b,17,0)
		self.assertEqual(b.getScore(),16)
		
	def test_strike(self):
		b = bow.bowling()
		self.roll_many(b,1,10)
		self.roll_many(b,1,3)	
		self.roll_many(b,1,3)	
		self.roll_many(b,16,0)
		self.assertEqual(b.getScore(),22)		
	
	def test_perfect(self):
		b = bow.bowling()
		self.roll_many(b,12,10)
		self.assertEqual(b.getScore(),300)
		
if __name__ == '__main__':		
	unittest.main()		
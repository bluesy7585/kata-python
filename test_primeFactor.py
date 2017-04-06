import unittest
import primeFactor as pf

class TestPrimeFactor(unittest.TestCase):
	def setup(self):
		pass
	def tearDown(self):
		pass
		
	def generate(self,number):
		obj = pf.primeFactor()
		ls = obj.generate(number)
		return ls	
		
	def test_1(self):
		ls = self.generate(1)
		self.assertEqual(ls,[])		
	def test_2(self):
		ls = self.generate(2)
		self.assertEqual(ls,[2])				
	def test_4(self):
		ls = self.generate(4)
		self.assertEqual(ls,[2,2])
	def test_8(self):
		ls = self.generate(8)
		self.assertEqual(ls,[2,2,2])		
	def test_3(self):
		ls = self.generate(3)
		self.assertEqual(ls,[3])
	def test_6(self):
		ls = self.generate(6)
		self.assertEqual(ls,[2,3])			

if __name__ == '__main__':	
	unittest.main()


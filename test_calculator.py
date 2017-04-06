import unittest
import Calculator as cal

class TestCalculator(unittest.TestCase):
	def setup(self):
		pass
	def tearDown(self):
		pass	

	def test_empty(self):
		sc = cal.Calculator()
		out = sc.add('')
		self.assertEqual(out,0)
		
	def test_1Number(self):
		sc = cal.Calculator()
		out = sc.add('1')
		self.assertEqual(out,1)	  
		
	def test_2Number(self):
		sc = cal.Calculator()
		out = sc.add('2,3')
		self.assertEqual(out,5)	
		
	def test_3Number(self):
		sc = cal.Calculator()
		out = sc.add('4,5,6')
		self.assertEqual(out,15)	
		
	def test_newline(self):
		sc = cal.Calculator()
		out = sc.add('0\n1')
		self.assertEqual(out,1)	
		
	def test_newline_4Number(self):
		sc = cal.Calculator()
		out = sc.add('0\n1,2\n3')
		self.assertEqual(out,6)	
		
	def test_custom_delimiter(self):
		sc = cal.Calculator()
		out = sc.add('//*\n3*4\n5')
		self.assertEqual(out,12)	
		
	def test_exception(self):
		self.assertRaises(cal.NegativeNumberException,self.negativeNumber)
		
	def negativeNumber(self):
		sc = cal.Calculator()		
		out = sc.add('-1')
		
if __name__ == '__main__':		
	unittest.main()
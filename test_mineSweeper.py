import unittest
from MineSweeper import MineSweeper
class TestMineSweeper(unittest.TestCase):	

	def test_oneline(self):
		input = '1 4\n....'
		expect = '0000'
		ms = MineSweeper()		
		out = ms.resolve(input)
		self.assertEqual(expect,out)
	def test_twoline(self):
		input = '2 4\n....\n....'
		expect = '0000\n0000'
		ms = MineSweeper()		
		out = ms.resolve(input)
		self.assertEqual(expect,out)
	def test_oneline1mine(self):	
		input = '1 5\n*....'
		expect = '*1000'
		ms = MineSweeper()		
		out = ms.resolve(input)
		self.assertEqual(expect,out)		
	def test_twoline1mine(self):	
		input = '2 5\n*....\n.....'
		expect = '*1000\n11000'
		ms = MineSweeper()		
		out = ms.resolve(input)
		self.assertEqual(expect,out)		
	def test_threeline3mine(self):	
		input = '3 5\n*....\n.*...\n..*..'
		expect = '*2100\n2*210\n12*10'
		ms = MineSweeper()		
		out = ms.resolve(input)
		self.assertEqual(expect,out)		

if __name__ == '__main__':
	unittest.main()		
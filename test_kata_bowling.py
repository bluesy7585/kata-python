import unit_test as test
import kata_bowling as bow

def roll_many(obj,times,bins):
		for i in range(0,times):
			obj.roll(bins)
		
def test_allZeros():
	b = bow.bowling()
	roll_many(b,20,0)
	return b.getScore()	

def test_allOnes():
	b = bow.bowling()
	roll_many(b,20,1)
	return b.getScore()	

def test_sparse():
	b = bow.bowling()
	roll_many(b,1,5)
	roll_many(b,1,5)
	roll_many(b,1,3)
	roll_many(b,17,0)
	return b.getScore()	
	
def test_strike():
	b = bow.bowling()
	roll_many(b,1,10)
	roll_many(b,1,3)	
	roll_many(b,1,3)	
	roll_many(b,16,0)
	return b.getScore()		

def test_perfect():
	b = bow.bowling()
	roll_many(b,12,10)
	return b.getScore()			
		
test.run_test_case('all zeros',test_allZeros,0)
test.run_test_case('all ones',test_allOnes,20)
test.run_test_case('one sparse',test_sparse,16)
test.run_test_case('one strike',test_strike,22)	
test.run_test_case('perfect',test_perfect,300)	

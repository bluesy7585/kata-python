import unit_test as test
import primeFactor as pf

def test_number(number):
	obj = pf.primeFactor()
	ls = obj.generate(number)
	return ls

def test_1():
	return test_number(1)
	
def test_2():
	return test_number(2)	
	
def test_4():
	return test_number(4)
	
def test_8():
	return test_number(8)	

def test_3():
	return test_number(3)
	
def test_15():
	return test_number(15)		
	
test.run_test_case('test 1',test_1,[])
test.run_test_case('test 2',test_2,[2])
test.run_test_case('test 4',test_4,[2,2])
test.run_test_case('test 8',test_8,[2,2,2])
test.run_test_case('test 3',test_3,[3])
test.run_test_case('test 15',test_15,[3,5])


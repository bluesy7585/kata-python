import unit_test as test
import Calculator as cal

def test_empty():
    sc = cal.Calculator()
    out = sc.add('')
    return out
	
def test_1Number():
    sc = cal.Calculator()
    out = sc.add('1')
    return out  
    
def test_2Number():
    sc = cal.Calculator()
    out = sc.add('2,3')
    return out        
    
def test_3Number():
    sc = cal.Calculator()
    out = sc.add('4,5,6')
    return out    
    
def test_newline():
    sc = cal.Calculator()
    out = sc.add('0\n1')
    return out        
	
def test_newline_4Number():
    sc = cal.Calculator()
    out = sc.add('0\n1,2\n3')
    return out           
	
def test_custom_delimiter():
    sc = cal.Calculator()
    out = sc.add('//*\n3*4\n5')
    return out   	

test.run_test_case('empty',test_empty,0)
test.run_test_case('1 number',test_1Number,1)
test.run_test_case('2 number',test_2Number,5)
test.run_test_case('3 number',test_3Number,15)
test.run_test_case('new line',test_newline,1)
test.run_test_case('new line 4 number',test_newline_4Number,6)
test.run_test_case('custom delimiter',test_custom_delimiter,12)
def run_test_case(name,func,expect):	
	test_score = func()
	if test_score == expect:
		print('test %s pass'%name)
	else:
		print('test %s fail, expect:%s but was:%s'%(name,expect,test_score))	
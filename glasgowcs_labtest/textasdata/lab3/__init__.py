from . import testsuite
from glasgowcs_labtest.utils import run_labtests, setup_docstring

all_testcases = testsuite.make_tests()
	
def labtest(function):
	run_labtests(function, all_testcases)

setup_docstring(labtest, all_testcases)

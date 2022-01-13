from glasgowcs_labtest.utils import labtest_main,setup_docstring
from . import testsuite

def labtest(function):
	labtest_main(function, testsuite.testcases)

setup_docstring(labtest,testsuite.testcases)

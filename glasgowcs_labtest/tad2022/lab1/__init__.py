from glasgowcs_labtest.utils import labtest_main,setup_docstring
from . import testsuite

def labtest(function):
	labtest_main(function, testsuite.make_tests)

setup_docstring(labtest,testsuite.make_tests)

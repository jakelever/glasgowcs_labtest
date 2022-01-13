
from uofgcs_labtest.utils import labtest_main,setup_docstring
from . import testsuite

def labtest(function):
	labtest_main(testsuite, function)

setup_docstring(testsuite, labtest)


import unittest
import inspect
import sys
from types import ModuleType

class LabTest(unittest.TestCase):
	def __init__(self, function):
		super(LabTest, self).__init__()
		self.function = function
		
	def run_testcases(self, testcases):
		for testcase in testcases:
			assert isinstance(testcase['input'], tuple), "A testcase has been incorrectly set up. Inputs for testcases must be tuples"
			
			input_txt = str(testcase['input'])[1:-1].rstrip(',') # Strip off the brackets and potential right comma for nice output
		
			self.assertEqual(self.function(*testcase['input']), testcase['output'], msg=f"Expected the output of {self.function.__name__}({input_txt}) would be {testcase['output']}")


	
	
def setup_docstring(module, function):
	assert isinstance(module, ModuleType), "The test suite setup is malfunctioning as it is not correctly passing in the test suite for this lab"
	assert callable(function) and function.__name__ == 'labtest', "The test suite setup is malfunctioning as it is not correctly passing in the labtest function for this lab"
	
	classes_in_module = list_classes(module)

	available_tests = [ name[:-5] for name in classes_in_module.keys() if name.endswith('_test') ]
	
	assert len(available_tests) > 0, "There are appear to be tests available for this test suite"
	
	docstring = """Runs tests on a specific function in this lab. It will output test status and throw an error if any of the tests fail with information about the provided input and expected output.
	
	The functions that can be tested with this labtest are TESTLIST.
	
	To run a lab, pass the function directly and not the name as string. For example, to test the FUNCNAME function, run labtest(FUNCNAME) and not labtest("FUNCNAME").
	
	Example Usage:
	
		def FUNCNAME():
			# Definitely not the right thing to do
			return 42
			
		labtest(FUNCNAME)

	Args:
		function: The function that you want to test (and not the string).

	"""
	
	available_tests_str = str(available_tests).replace('"','').replace("'","")
	docstring = docstring.replace('TESTLIST',available_tests_str)
	docstring = docstring.replace('FUNCNAME',available_tests[0])
	
	function.__doc__ = docstring
	
	
	
def list_classes(module):
	classes_by_name = {}
	for name, obj in inspect.getmembers(module):
		if inspect.isclass(obj):
			classes_by_name[name] = obj
	return classes_by_name

def labtest_main(module, function):
	assert isinstance(module, ModuleType), "The labtest method is malfunctioning as it is not correctly passing in the test suite for this lab"
	classes_in_module = list_classes(module)
	
	assert not isinstance(function, str), "You've passed in a string to labtest (perhaps the name of function to test?). You need to pass in the actual function instead. For example do labtest({function}) instead of labtest(\"{function}\")"

	assert callable(function), f"Unable to call the function '{function_name}'. Is it a variable and not a function?"

	function_name = function.__name__

	test_name = function_name + '_test'
	
	assert test_name in classes_in_module, f"Couldn't find a test suite for function '{function_name}'. Does the name of the function match the description above?"
	TestClass = classes_in_module[test_name]
	
	suite = unittest.TestSuite()
	suite.addTest(TestClass(function))
	unittest.TextTestRunner(verbosity=2).run(suite)

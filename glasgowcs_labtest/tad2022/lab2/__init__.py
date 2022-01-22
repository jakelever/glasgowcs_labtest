from . import testsuite

import copy
import numpy as np
from scipy.sparse.csr import csr_matrix

def run_testcases(function, testcases):
	header = f"LABTEST: Running {len(testcases)} testcases"

	print("-"*len(header))
	print(header)
	print("-"*len(header))
	
	for testcase in testcases:
		assert isinstance(testcase['input'], tuple), "A testcase has been incorrectly set up. Inputs for testcases must be tuples"
		
		print(f"Input: {str(testcase['input'])}. Running... ",)
		
		original_testcase = copy.deepcopy(testcase['input'])
		input_txt = str(testcase['input'])[1:-1].rstrip(',') # Strip off the brackets and potential right comma for nice output
		
		# Run the function and get the output
		output = function(*testcase['input'])
		
		error_msg = f"\n\nERROR: Expected the output of {function.__name__}({input_txt}) to be {testcase['output']}. Got {output}."
		
		assert original_testcase == testcase['input'], f"ERROR: The input data to the function has been changed during execution.\n\nFunction call: {function.__name__}({input_txt}).\n\nThe original input data: {original_testcase}.\n\nThe input data after the function is called: {testcase['input']}.\n\nSee https://bit.ly/glasgowcs_objinput_explainer for more information."
		assert output == testcase['output'], error_msg
		
		print("OK.")
		
	
	footer = f"{len(testcases)} testcases PASSED"

	print("-"*len(header))
	print(footer)
	print("-"*len(header))
	
def run_scipy_sparse_testcases(function, testcases):
	header = f"LABTEST: Running {len(testcases)} testcases"

	print("-"*len(header))
	print(header)
	print("-"*len(header))

	for testcase in testcases:
		
		print(f"Input: {str(testcase['input'])}. Running... ",)
		
		original_testcase = copy.deepcopy(testcase['input'])
		input_txt = str(testcase['input'])[1:-1].rstrip(',') # Strip off the brackets and potential right comma for nice output
		
		result = function(*testcase['input'])

		expected_matrix = np.array(testcase['output'])

		func_name = function.__name__

		
		assert original_testcase == testcase['input'], f"ERROR: The input data to the function has been changed during execution.\n\nFunction call: {function.__name__}({input_txt}).\n\nThe original input data: {original_testcase}.\n\nThe input data after the function is called: {testcase['input']}.\n\nSee https://bit.ly/glasgowcs_objinput_explainer for more information."
		assert isinstance(result, csr_matrix), f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\n{func_name} is not returning the right type of data. It should be a csr_matrix which is the output of fit_transform function of a TfidfVectorizer. Instead it returned: {type(result)}"
		assert expected_matrix.shape == result.shape, f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\nThe output matrix shape does not match the expected {expected_matrix.shape}. Got {result.shape}"
		#assert 
		assert np.array_equal(expected_matrix, result.todense()), f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\nThe output matrix does not match the expected. \n\nExpected a sparse matrix equivalent to:\n{expected_matrix.tolist()}\n\nGot:\n{result.todense().tolist()}"

		print("OK.")


	footer = f"{len(testcases)} testcases PASSED"

	print("-"*len(header))
	print(footer)
	print("-"*len(header))


def validate_testcases(all_testcases):
	assert isinstance(all_testcases, dict), "The labtest method is malfunctioning as it is not correctly passing in the test suite for this lab"
	
	assert len(all_testcases) > 0, "The test suite for this lab contains no testcases"
	
	for func_name,testcases in all_testcases.items():
		if callable(testcases): # Test is a custom function to call with the function
			continue
	
		assert isinstance(func_name, str), "The testcases for this lab are malformed"
		assert isinstance(testcases, list), "The testcases for this lab are malformed"
		for testcase in testcases:
			assert isinstance(testcase, dict), "The testcases for this lab are malformed"
			assert "input" in testcase, "The testcases for this lab are malformed"
			assert "output" in testcase, "The testcases for this lab are malformed"
			assert isinstance(testcase["input"],tuple), "The testcases for this lab are malformed"
	
def setup_docstring(labtest_function):
	all_testcases = testsuite.make_tests()
	validate_testcases(all_testcases)

	assert callable(labtest_function) and labtest_function.__name__ == 'labtest', "The test suite setup is malfunctioning as it is not correctly passing in the labtest function for this lab"
		
	docstring = """Runs tests on a specific function in this lab. It will output test status and throw an error if any of the tests fail with information about the provided input and expected output.
	
	The functions that can be tested with this labtest are TESTLIST.
	
	To run a lab, pass the function directly and not the name as string. For example, to test the FUNCNAME function, run labtest(FUNCNAME) and not labtest("FUNCNAME").
	
	Example Usage:
	
		def FUNCNAME():
			return 42 # This function is wrong
			
		labtest(FUNCNAME) # This will test the function

	Args:
		function: The function that you want to test (and not the string).

	"""
	
	test_names = str(list(all_testcases.keys()))
	test_names = str(test_names).replace('"','').replace("'","")
	docstring = docstring.replace('TESTLIST',test_names)
	docstring = docstring.replace('FUNCNAME',list(all_testcases)[0])
	docstring = docstring.replace('\t','  ')
	
	labtest_function.__doc__ = docstring

def labtest(function):
	all_testcases = testsuite.make_tests()
	validate_testcases(all_testcases)
	
	assert not isinstance(function, str), "You've passed in a string to labtest (perhaps the name of function to test?). You need to pass in the actual function instead. For example do labtest({function}) instead of labtest(\"{function}\")"

	assert callable(function), f"Unable to call the function '{function_name}'. Is it a variable and not a function?"

	function_name = function.__name__

	assert function_name in all_testcases, f"Couldn't find a test suite for function '{function_name}'. Does the name of the function match the description above?"
	
	function_testcases = all_testcases[function_name]
	
	if callable(function_testcases): # The testcases are actually a custom function (so call it with the function)
		function_testcases(function)
	elif function_name in ["tfidf_vectorize_with_sklearn","tfidf_vectorize_with_sklearn_and_spacy"]:
		run_scipy_sparse_testcases(function, function_testcases)
	else:
		run_testcases(function, function_testcases)

setup_docstring(labtest)

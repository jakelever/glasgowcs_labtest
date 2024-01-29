
import copy
import numpy as np
from collections import Counter, defaultdict
from scipy.sparse import csr_matrix

def round_data(x, places):
	"""
	Takes a data structure (potentially of nested data) and rounds all the
	floating point values into to the given number of decimal places. It works
	with nested structures (e.g. list of lists, etc).

	Data structures can contain any of dict, list, float, int, string
	Counter or defaultdict.

	Args:
		x: The data structure to round any floats within
		places: Number of decimal places to round to

	Returns:
	A copy of the data structure with any floating point
	values rounded and everything else kept the same

	"""

	if isinstance(x, dict):
		return {key:round_data(val,places) for key,val in x.items() }
	elif isinstance(x, list):
		return [round_data(val,places) for val in x ]
	elif isinstance(x, set):
		return set(round_data(val,places) for val in x)
	elif isinstance(x, Counter) or isinstance(x, defaultdict):
		copied = copy.copy(x)
		for k in copied:
			copied[k] = round_data(copied[k],places)
		return copied
	elif isinstance(x, float):
		return round(x, places)
	elif isinstance(x, int) or isinstance(x, str):
		return x
	else:
		raise RuntimeError("ERROR: Data structure contains an element that is not a dict, list, float, int, string, Counter or defaultdict")

def round_sparse_matrix(m, places):
	"""
	Rounds a scipy sparse matrix (e.g. csr_matrix) to
	the given number of decimal places.

	Args:
		m: The sparse matrix
		places: Number of decimal places to round to

	Returns:
	A copy of the sparse matrix with all values rounded

	"""
	
	m_copy = copy.deepcopy(m)
	m_copy.data = np.round(m_copy.data, 2)
	return m_copy
	
	
def to_unique_types(x):
	"""
	Converts a variable into a set of unique types (excluding lists, dicts and other common data structures)
	
	Args:
		x: A variable of any time
		
	Returns:
	A representation of the types of the variable (either just the type, a list of types, dictionary of types, etc)
	"""
	
	if isinstance(x, list) or isinstance(x, set):
		return set().union( *[to_unique_types(j) for j in x] )
	elif isinstance(x, dict) or isinstance(x, Counter) or isinstance(x, defaultdict):
		return set().union( *[to_unique_types(j) for j in x.values()] )
	else:
		return set([type(x)])

def run_testcases(function, testcases, expect_csr_matrix=False):
	header = f"LABTEST: Running {len(testcases)} testcases"

	print("-"*len(header))
	print(header)
	print("-"*len(header))
	
	for testcase in testcases:
		assert isinstance(testcase['input'], tuple), "A testcase has been incorrectly set up. Inputs for testcases must be tuples"
		
		print(f"Input: {str(testcase['input'])}. Running... ",)
		
		# Copy to input test case to check if it has been changed
		original_testcase = copy.deepcopy(testcase['input'])
		
		# Run the function and get the output
		output = function(*testcase['input'])
		
		# Strip off the brackets and potential right comma for nice output
		input_txt = str(testcase['input'])[1:-1].rstrip(',')
		
		# Check that the input data hasn't been changed
		error_msg_inputchange = f"ERROR: The input data to the function has been changed during execution.\n\nFunction call: {function.__name__}({input_txt}).\n\nThe original input data: {original_testcase}.\n\nThe input data after the function is called: {testcase['input']}.\n\nSee https://bit.ly/glasgowcs_objinput_explainer for more information."
		assert original_testcase == testcase['input'], error_msg_inputchange
		
		if expect_csr_matrix:
			# Get the expected results
			expected_matrix = np.array(testcase['output'])
			
			assert isinstance(output, csr_matrix), f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\n{function.__name__} is not returning the right type of data. It should be a csr_matrix which is the output of fit_transform function of a TfidfVectorizer. Instead it returned: {type(output)}"
			assert expected_matrix.shape == output.shape, f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\nThe output matrix shape does not match the expected {expected_matrix.shape}. Got {output.shape}"
			
			# Do some numerical rounding for comparing numbers
			expected_matrix = round_sparse_matrix(expected_matrix, places=5)
			output = round_sparse_matrix(output, places=5)
			
			assert np.array_equal(expected_matrix, output.todense()), f"\n\nERROR: Problem with run of the output of {function.__name__}({input_txt}).\n\nThe output matrix does not match the expected. \n\nExpected a sparse matrix equivalent to:\n{expected_matrix.tolist()}\n\nGot:\n{output.todense().tolist()}"

		else:
			# Get the expected results and types
			expected_output = testcase['output']
			
			# Look at the expected output types (e.g. int, str, etc) and see if the function outputs any unexpected ones
			output_types = to_unique_types(output)
			expected_output_types = to_unique_types(expected_output)
			unexpected_types = output_types.difference(expected_output_types)
			error_msg_type = f"\n\nERROR: Expected the types of the output {function.__name__}({input_txt}) to include {expected_output_types}. Got unexpected types: {unexpected_types}."
			assert len(unexpected_types) == 0, error_msg_type
			
			# Do some numerical rounding (in case that matters for comparing numbers)
			output = round_data(output, places=5)
			expected_output = round_data(expected_output, places=5)
			
			error_msg_content = f"\n\nERROR: Expected the output of {function.__name__}({input_txt}) to be {expected_output}. Got {output}."
			assert output == expected_output, error_msg_content
		
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
		
		# Copy to input test case to check if it has been changed
		original_testcase = copy.deepcopy(testcase['input'])
		input_txt = str(testcase['input'])[1:-1].rstrip(',') # Strip off the brackets and potential right comma for nice output
		
		# Run the function and get the output
		result = function(*testcase['input'])

		
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
	
def setup_docstring(labtest_function, all_testcases):
	validate_testcases(all_testcases)

	assert callable(labtest_function) and labtest_function.__name__ == 'labtest', "The test suite setup is malfunctioning as it is not correctly passing in the labtest function for this lab"
		
	docstring = """Runs tests on a specific function in this lab. It will output test status and throw an error if any of the tests fail with information about the provided input and expected output. Any floating point values in the output will be rounded to five decimal places before comparison.
	
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

def run_labtests(function, all_testcases, expect_csr_matrix=False):
	validate_testcases(all_testcases)
	
	assert not isinstance(function, str), f"You've passed in a string to labtest (perhaps the name of function to test?). You need to pass in the actual function instead. For example do labtest({function}) instead of labtest(\"{function}\")"

	function_name = function.__name__

	assert callable(function), f"Unable to call the function '{function_name}'. Is it a variable and not a function?"
	assert function_name in all_testcases, f"Couldn't find a test suite for function '{function_name}'. Does the name of the function match the description above?"
	
	function_testcases = all_testcases[function_name]
	
	if callable(function_testcases): # The testcases are actually a custom function (so call it with the function)
		function_testcases(function)
	else:
		run_testcases(function, function_testcases, expect_csr_matrix)

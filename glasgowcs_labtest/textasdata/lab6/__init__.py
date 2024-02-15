from . import testsuite
from glasgowcs_labtest.utils import setup_docstring, validate_testcases
import copy

all_testcases = testsuite.make_tests()

def run_testcases_inplace(function, testcases, expect_csr_matrix=False):
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
		output = function(*original_testcase)
		
		# Strip off the brackets and potential right comma for nice output
		input_txt = str(testcase['input'])[1:-1].rstrip(',')
		
		# Check that nothing is being returned
		error_returned_data = f"\n\nERROR: Expected the call to {function.__name__}({input_txt}) to not return anything. Got {output}"
		assert output is None, error_returned_data
		
		# Get the expected results and types
		expected_output = testcase['output']
		
		error_msg_content = f"\n\nERROR: Expected the inputs of {function.__name__}({input_txt}) to be changed to {expected_output}. Got {original_testcase}."
		assert original_testcase == expected_output, error_msg_content
		
		print("OK.")
		
	footer = f"{len(testcases)} testcases PASSED"

	print("-"*len(header))
	print(footer)
	print("-"*len(header))
	

def run_labtests(function, all_testcases, expect_csr_matrix=False):
	validate_testcases(all_testcases)
	
	assert not isinstance(function, str), f"You've passed in a string to labtest (perhaps the name of function to test?). You need to pass in the actual function instead. For example do labtest({function}) instead of labtest(\"{function}\")"

	function_name = function.__name__

	assert callable(function), f"Unable to call the function '{function_name}'. Is it a variable and not a function?"
	assert function_name in all_testcases, f"Couldn't find a test suite for function '{function_name}'. Does the name of the function match the description above?"
	
	function_testcases = all_testcases[function_name]
	
	run_testcases_inplace(function, function_testcases)

	
def labtest(function):
	run_labtests(function, all_testcases)

setup_docstring(labtest, all_testcases)

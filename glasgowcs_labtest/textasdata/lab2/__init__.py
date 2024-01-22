from . import testsuite
from glasgowcs_labtest.utils import run_labtests, setup_docstring

all_testcases = testsuite.make_tests()
	
def labtest(function):
	expect_csr_matrix = function.__name__ in ["tfidf_vectorize_with_sklearn","tfidf_vectorize_with_sklearn_and_spacy"]
		
	run_labtests(function, all_testcases, expect_csr_matrix)

setup_docstring(labtest, all_testcases)

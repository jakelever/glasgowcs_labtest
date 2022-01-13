from glasgowcs_labtest.utils import LabTest

class multiply_by_three_test(LabTest):
	def runTest(self):
		testcases = [
			{'input': 1, 'output': 3},
			{'input': 2, 'output': 6},
			{'input': 3, 'output': 9},
			{'input': 4, 'output': 12},
			{'input': 5, 'output': 15},
		]
		
		self.run_testcases(testcases)

class tokenize_strsplit_test(LabTest):
	def runTest(self):
		testcases = [
			{'input':'John's father didn’t have £100.', 'output': ["John's", 'father', 'didn’t', 'have', '£100.']},
			{'input':'Where we're going, we won't need roads.', 'output': ['Where', "we're", 'going,', 'we', "won't", 'need', 'roads.']},
			{'input':'I'm going to make him an offer he can't refuse.', 'output': ["I'm", 'going', 'to', 'make', 'him', 'an', 'offer', 'he', "can't", 'refuse.']},
			{'input':'It's-a Me, Mario!', 'output': ["It's-a", 'Me,', 'Mario!']},
			{'input':'Mess with the best, die like the rest.', 'output': ['Mess', 'with', 'the', 'best,', 'die', 'like', 'the', 'rest.']},
		]
		
		self.run_testcases(testcases)

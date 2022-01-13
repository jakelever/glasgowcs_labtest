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

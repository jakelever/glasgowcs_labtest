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
			{"input": "John's father didn't have $100.", "output": ["John's", "father", "didn't", "have", "$100."]},
			{"input": "Where we're going, we won't need roads.", "output": ["Where", "we're", "going,", "we", "won't", "need", "roads."]},
			{"input": "I'm going to make him an offer he can't refuse.", "output": ["I'm", "going", "to", "make", "him", "an", "offer", "he", "can't", "refuse."]},
			{"input": "It's-a Me, Mario!", "output": ["It's-a", "Me,", "Mario!"]},
			{"input": "Mess with the best, die like the rest.", "output": ["Mess", "with", "the", "best,", "die", "like", "the", "rest."]},
		]
		
		self.run_testcases(testcases)
		
class tokenize_punctuation_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": "John's father didn't have $100.", "output": ["John", "'", "s", "father", "didn", "'", "t", "have", "$", "100", "."]},
			{"input": "Where we're going, we won't need roads.", "output": ["Where", "we", "'", "re", "going", ",", "we", "won", "'", "t", "need", "roads", "."]},
			{"input": "I'm going to make him an offer he can't refuse.", "output": ["I", "'", "m", "going", "to", "make", "him", "an", "offer", "he", "can", "'", "t", "refuse", "."]},
			{"input": "It's-a Me, Mario!", "output": ["It", "'", "s", "-", "a", "Me", ",", "Mario", "!"]},
			{"input": "Mess with the best, die like the rest.", "output": ["Mess", "with", "the", "best", ",", "die", "like", "the", "rest", "."]},

		]
		
		self.run_testcases(testcases)

class stem_onerule_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": ["We", "are", "going", "fishing", "."], "output": ["We", "are", "go", "fish", "."]},
			{"input": ["He", "walked", "home", "."], "output": ["He", "walked", "home", "."]},
			{"input": ["She", "loves", "Irn", "Bru", "."], "output": ["She", "loves", "Irn", "Bru", "."]},
			{"input": ["I", "love", "reading", "books", "."], "output": ["I", "love", "read", "books", "."]},
			{"input": ["David", "runs", "every", "day", "."], "output": ["David", "runs", "every", "day", "."]},
		]
		
		self.run_testcases(testcases)
		
class stem_morerules_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": ["We", "are", "going", "fishing", "."], "output": ["We", "are", "go", "fish", "."]},
			{"input": ["He", "walked", "home", "."], "output": ["He", "walk", "home", "."]},
			{"input": ["She", "loves", "Irn", "Bru", "."], "output": ["She", "love", "Irn", "Bru", "."]},
			{"input": ["I", "love", "reading", "books", "."], "output": ["I", "love", "read", "book", "."]},
			{"input": ["David", "runs", "every", "day", "."], "output": ["David", "run", "every", "day", "."]},
		]
		
		self.run_testcases(testcases)
		
		
class lowercase_tokens_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": ["We", "are", "go", "fish", "."], "output": ["we", "are", "go", "fish", "."]},
			{"input": ["He", "walk", "home", "."], "output": ["he", "walk", "home", "."]},
			{"input": ["She", "love", "Irn", "Bru", "."], "output": ["she", "love", "irn", "bru", "."]},
			{"input": ["I", "love", "read", "book", "."], "output": ["i", "love", "read", "book", "."]},
			{"input": ["David", "run", "every", "day", "."], "output": ["david", "run", "every", "day", "."]},
		]
		
		self.run_testcases(testcases)
		
class remove_stopwords_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": ["we", "are", "go", "fish", "."], "output": ["go", "fish", "."]},
			{"input": ["he", "walk", "home", "."], "output": ["walk", "home", "."]},
			{"input": ["she", "love", "irn", "bru", "."], "output": ["love", "irn", "bru", "."]},
			{"input": ["i", "love", "read", "book", "."], "output": ["love", "read", "book", "."]},
			{"input": ["david", "run", "every", "day", "."], "output": ["david", "run", "day", "."]},
		]
		
		self.run_testcases(testcases)
		
class tokenize_spacy_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": "John's father didn't have $100.", "output": ["John", "'s", "father", "did", "n't", "have", "$", "100", "."]},
			{"input": "You can't handle the truth!", "output": ["You", "ca", "n't", "handle", "the", "truth", "!"]},
			{"input": "I'm going to make him an offer he can't refuse.", "output": ["I", "'m", "going", "to", "make", "him", "an", "offer", "he", "ca", "n't", "refuse", "."]},
			{"input": "The flow of time is always cruel.", "output": ["The", "flow", "of", "time", "is", "always", "cruel", "."]},
			{"input": "Mess with the best, die like the rest.", "output": ["Mess", "with", "the", "best", ",", "die", "like", "the", "rest", "."]},
		]
		
		self.run_testcases(testcases)
		
class text_pipeline_spacy_test(LabTest):
	def runTest(self):
		testcases = [
			{"input": "John's father didn't have $100.", "output": ["john", "father", "$", "100"]},
			{"input": "You can't handle the truth!", "output": ["handle", "truth"]},
			{"input": "I'm going to make him an offer he can't refuse.", "output": ["go", "offer", "refuse"]},
			{"input": "The flow of time is always cruel.", "output": ["flow", "time", "cruel"]},
			{"input": "Mess with the best, die like the rest.", "output": ["mess", "good", "die", "like", "rest"]},
		]
		
		self.run_testcases(testcases)
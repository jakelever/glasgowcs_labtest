
def run_make_vocabulary_test(make_vocabulary):
	input_testcases = [
		[ ['irn','bru','good'], ['irn','bru','bad'] ],
		[ ['go','fish','today'], ['went','fish','yesterday'] ],
		[ ['glasgow','city','culture','1990'], ['university','glasgow','founded','1451'] ],
		[ ['expanse','season','six','excellent'] ]
	]
	
	header = f"LABTEST: Running {len(input_testcases)} testcases"

	print("-"*len(header))
	print(header)
	print("-"*len(header))
	
	for input_testcase in input_testcases:
		
		print(f"Input: {str(input_testcase)}. Running... ",)
		
		unique_tokens = set(sum(input_testcase, []))
		N = len(unique_tokens)
		
		usecase_txt = "make_vocabulary({input_testcase})"
		
		vocab = make_vocabulary(input_testcase)
		
		assert isinstance(vocab, dict), f"make_vocabulary MUST return a dictionary. Got a {type(vocab)}"
		assert len(vocab) == len(unique_tokens), f"Returned dictionary should have the length of the number of unique tokens. Got {len(vocab)}. Expected {len(unique_tokens)}."
		assert sorted(vocab.keys()) == sorted(unique_tokens), f"Returned dictionary keys should match the unique tokens (order doesn't matter). Got {sorted(vocab.keys())}. Expected {sorted(unique_tokens)}."
		assert sorted(vocab.values()) == list(range(0,N)), f"Returned dictionary values should start from 0 and go up to the number of tokens minus 1. Which token is given which number does not matter. Got {sorted(vocab.values())}. Expected {list(range(0,N))}."
	
	footer = f"{len(input_testcases)} testcases PASSED"

	print("-"*len(header))
	print(footer)
	print("-"*len(header))



def make_tests():
	return {
	
"make_vocabulary": run_make_vocabulary_test,

"multiply_by_three": [
	{'input': (1,), 'output': 3},
	{'input': (2,), 'output': 6},
	{'input': (3,), 'output': 9},
	{'input': (4,), 'output': 12},
	{'input': (5,), 'output': 15},
],

"make_onehot_dense": [
	{"input": (["text", "university", "good", "good"], {"text": 0, "python": 1, "city": 2, "good": 3, "university": 4}), "output": [1, 0, 0, 1, 1]},
	{"input": (["coffee", "university", "culture", "coffee"], {"coffee": 0, "university": 1, "culture": 2, "city": 3}), "output": [1, 1, 1, 0]},
	{"input": (["university", "good", "city", "university"], {"university": 0, "city": 1, "good": 2, "python": 3}), "output": [1, 1, 1, 0]},
	{"input": (["university", "shop", "coffee", "shop"], {"glasgow": 0, "text": 1, "coffee": 2, "shop": 3, "irn": 4, "university": 5}), "output": [0, 0, 1, 1, 0, 1]},
	{"input": (["culture", "city", "culture", "good", "shop"], {"city": 0, "good": 1, "culture": 2, "shop": 3}), "output": [1, 1, 1, 1]},

],

"make_onehot_sparse": [
	{"input": (["bad", "irn", "glasgow", "glasgow", "bad", "bad"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5}), "output": {3: 1, 2: 1, 1: 1}},
	{"input": (["kelvin", "kelvin", "irn", "irn"], {"coffee": 0, "shop": 1, "irn": 2, "kelvin": 3}), "output": {2: 1, 3: 1}},
	{"input": (["culture", "good", "city", "culture"], {"irn": 0, "good": 1, "culture": 2, "city": 3, "glasgow": 4}), "output": {3: 1, 2: 1, 1: 1}},
	{"input": (["city", "university", "city", "glasgow", "shop", "university"], {"city": 0, "shop": 1, "glasgow": 2, "irn": 3, "university": 4}), "output": {0: 1, 2: 1, 1: 1, 4: 1}},
	{"input": (["shop", "shop", "shop", "bru", "irn"], {"shop": 0, "bad": 1, "bru": 2, "irn": 3, "python": 4}), "output": {2: 1, 3: 1, 0: 1}},
],

"make_tf_sparse": [
	{"input": (["bad", "irn", "glasgow", "glasgow", "bad", "bad"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5}), "output": {3: 3, 1: 1, 2: 2}},
	{"input": (["kelvin", "kelvin", "irn", "irn"], {"coffee": 0, "shop": 1, "irn": 2, "kelvin": 3}), "output": {3: 2, 2: 2}},
	{"input": (["culture", "good", "city", "culture"], {"irn": 0, "good": 1, "culture": 2, "city": 3, "glasgow": 4}), "output": {2: 2, 1: 1, 3: 1}},
	{"input": (["city", "university", "city", "glasgow", "shop", "university"], {"city": 0, "shop": 1, "glasgow": 2, "irn": 3, "university": 4}), "output": {0: 2, 4: 2, 2: 1, 1: 1}},
	{"input": (["shop", "shop", "shop", "bru", "irn"], {"shop": 0, "bad": 1, "bru": 2, "irn": 3, "python": 4}), "output": {0: 3, 2: 1, 3: 1}},
],

"doc_frequency": [
	{"input": ([["irn", "kelvin"], ["glasgow", "bad"], ["bru", "glasgow"], ["glasgow", "irn"]],), "output": {"kelvin": 1, "irn": 2, "bad": 1, "glasgow": 3, "bru": 1}},
	{"input": ([["python", "culture", "bad"], ["bad", "culture", "culture", "culture"]],), "output": {"python": 1, "bad": 2, "culture": 2}},
	{"input": ([["university", "irn", "university", "culture"], ["bru", "coffee"]],), "output": {"culture": 1, "irn": 1, "university": 1, "coffee": 1, "bru": 1}},
	{"input": ([["bad", "bru", "glasgow", "glasgow"], ["glasgow", "bad"], ["bad", "bru", "kelvin"]],), "output": {"bad": 3, "glasgow": 2, "bru": 2, "kelvin": 1}},
	{"input": ([["city", "bad", "kelvin", "coffee"], ["bru", "city", "kelvin", "coffee"]],), "output": {"kelvin": 2, "bad": 1, "coffee": 2, "city": 2, "bru": 1}},

],

"make_tfidf_sparse": [
	{"input": (["irn", "kelvin"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5}, {"kelvin": 4, "irn": 5, "bad": 5, "glasgow": 6, "bru": 4, "coffee": 3}, 10), "output": {1: 0.6931471805599453, 5: 0.9162907318741551}},
	{"input": (["bad", "bru", "glasgow", "glasgow"], {"bru": 0, "bad": 1, "kelvin": 2, "culture": 3, "glasgow": 4}, {"bad": 3, "glasgow": 4, "bru": 5, "kelvin": 5, "culture": 3}, 8), "output": {1: 0.9808292530117262, 0: 0.47000362924573563, 4: 1.1736001944781467}},
	{"input": (["kelvin", "city", "city"], {"kelvin": 0, "shop": 1, "culture": 2, "python": 3, "city": 4}, {"kelvin": 2, "city": 4, "culture": 2, "python": 2, "shop": 1}, 6), "output": {0: 1.0986122886681098, 4: 0.686512104608772}},
	{"input": (["bru", "good", "glasgow"], {"coffee": 0, "good": 1, "kelvin": 2, "bru": 3, "glasgow": 4}, {"good": 5, "glasgow": 6, "bru": 5, "kelvin": 5, "coffee": 4}, 10), "output": {3: 0.6931471805599453, 1: 0.6931471805599453, 4: 0.5108256237659907}},
	{"input": (["coffee", "bru", "bru", "irn"], {"irn": 0, "city": 1, "bru": 2, "coffee": 3}, {"irn": 2, "coffee": 4, "bru": 5, "city": 3}, 6), "output": {3: 0.4054651081081644, 2: 0.3086972298409842, 0: 1.0986122886681098}},
],

"tfidf_vectorize_with_sklearn": [
	{"input": (["Glasgow smiles better", "He smiles a lot"],), "output": [[0.6316672017376245, 0.6316672017376245, 0.0, 0.0, 0.4494364165239821], [0.0, 0.0, 0.6316672017376245, 0.6316672017376245, 0.4494364165239821]]},
	{"input": (["Irn Bru is good", "Irn Bru is my favourite", "I hate Irn Bru"],), "output": [[0.39148397136265967, 0.0, 0.6628399823470976, 0.0, 0.39148397136265967, 0.5041068915759233, 0.0], [0.3263095219528963, 0.55249004708441, 0.0, 0.0, 0.3263095219528963, 0.42018292148905534, 0.55249004708441], [0.4532946552278861, 0.0, 0.0, 0.7674945674619879, 0.4532946552278861, 0.0, 0.0]]},
	{"input": (["This to shall pass", "You shall not pass", "You did not pass the ball"],), "output": [[0.0, 0.0, 0.0, 0.34520501686496574, 0.444514311537431, 0.0, 0.5844829010200651, 0.5844829010200651, 0.0], [0.0, 0.0, 0.5268201732399633, 0.40912286076708654, 0.5268201732399633, 0.0, 0.0, 0.0, 0.5268201732399633], [0.4711101009983051, 0.4711101009983051, 0.35829137488557944, 0.2782452148327134, 0.0, 0.4711101009983051, 0.0, 0.0, 0.35829137488557944]]},
	{"input": (["Yesterday I went for a walk", "I am so tired I could not walk any further"],), "output": [[0.0, 0.0, 0.0, 0.534046329052269, 0.0, 0.0, 0.0, 0.0, 0.37997836159100784, 0.534046329052269, 0.534046329052269], [0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.0, 0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.25969799324016246, 0.0, 0.0]]},
	{"input": (["I ate too much", "I eat therefore I am", "I ate all of the chocolate"],), "output": [[0.0, 0.0, 0.4736296010332684, 0.0, 0.0, 0.6227660078332259, 0.0, 0.0, 0.0, 0.6227660078332259], [0.0, 0.5773502691896257, 0.0, 0.0, 0.5773502691896257, 0.0, 0.0, 0.0, 0.5773502691896257, 0.0], [0.4673509818107163, 0.0, 0.35543246785041743, 0.4673509818107163, 0.0, 0.0, 0.4673509818107163, 0.4673509818107163, 0.0, 0.0]]},

],

"tfidf_vectorize_with_sklearn_and_spacy": [
	{"input": (["Glasgow smiles better", "He smiles a lot"],), "output": [[0.6316672017376245, 0.0, 0.4494364165239821, 0.6316672017376245], [0.0, 0.8148024746671689, 0.5797386715376657, 0.0]]},
	{"input": (["Irn Bru is good", "Irn Bru is my favourite", "I hate Irn Bru"],), "output": [[0.4532946552278861, 0.0, 0.7674945674619879, 0.0, 0.4532946552278861], [0.4532946552278861, 0.7674945674619879, 0.0, 0.0, 0.4532946552278861], [0.4532946552278861, 0.0, 0.0, 0.7674945674619879, 0.4532946552278861]]},
	{"input": (["This to shall pass", "You shall not pass", "You did not pass the ball"],), "output": [[0.0, 0.6133555370249717, 0.7898069290660905], [0.0, 0.6133555370249717, 0.7898069290660905], [0.8610369959439764, 0.5085423203783267, 0.0]]},
	{"input": (["Yesterday I went for a walk", "I am so tired I could not walk any further"],), "output": [[0.6316672017376245, 0.0, 0.4494364165239821, 0.6316672017376245], [0.0, 0.8148024746671689, 0.5797386715376657, 0.0]]},
	{"input": (["I ate too much", "I eat therefore I am", "I ate all of the chocolate"],), "output": [[0.0, 1.0], [0.0, 1.0], [0.8610369959439764, 0.5085423203783267]]},

],

}
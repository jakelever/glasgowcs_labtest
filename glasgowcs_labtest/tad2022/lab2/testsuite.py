import copy

def run_make_vocabulary_test(make_vocabulary,with_unk):
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
		
		unique_tokens = sorted(set(sum(input_testcase, [])))
		if with_unk:
			unique_tokens.append('<UNK>')
		
		N = len(unique_tokens)
		
		usecase_txt = "make_vocabulary({input_testcase})"
		
		original_testcase = copy.deepcopy(input_testcase)
		vocab = make_vocabulary(input_testcase)
		
		assert original_testcase == input_testcase, f"ERROR: The input data to the function has been changed inside the make_vocabulary function.\n\nThe original input data: {original_testcase}.\n\nThe input data after the function is called: {input_testcase}.\n\nSee https://bit.ly/glasgowcs_objinput_explainer for more information."
		assert isinstance(vocab, dict), f"ERROR: make_vocabulary MUST return a dictionary. Got a {type(vocab)}"
		assert all( isinstance(k,str) for k in vocab.keys() ), f"ERROR: Returned dictionary keys should all be text values. Got {vocab.keys()}." 
		assert all( isinstance(v,int) for v in vocab.values() ), f"ERROR: Returned dictionary values should all be text values. Got {vocab.values()}." 
		
		if with_unk:
			assert sorted(vocab.keys()) == sorted(unique_tokens), f"ERROR: Returned dictionary keys should match the unique tokens plus <UNK> (order doesn't matter). Got {sorted(vocab.keys())}. Expected {sorted(unique_tokens)}."
		else:
			assert sorted(vocab.keys()) == sorted(unique_tokens), f"ERROR: Returned dictionary keys should match the unique tokens (order doesn't matter). Got {sorted(vocab.keys())}. Expected {sorted(unique_tokens)}."
		assert sorted(vocab.values()) == list(range(0,N)), f"ERROR: Returned dictionary values should start from 0 and go up to the number of tokens minus 1. Which token is given which number does not matter. Got {sorted(vocab.values())}. Expected {list(range(0,N))}."
	
	footer = f"{len(input_testcases)} testcases PASSED"

	print("-"*len(header))
	print(footer)
	print("-"*len(header))
	

def make_tests():
	return {
	
"make_vocabulary": lambda func : run_make_vocabulary_test(func,with_unk=False),

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

"sparse_to_dense": [
	{"input":({2: 1, 1: 4}, 4), "output":[0, 4, 1, 0]},
	{"input":({4: 2}, 5), "output":[0, 0, 0, 0, 2]},
	{"input":({0: 1, 1: 2, 4: 4}, 7), "output":[1, 2, 0, 0, 4, 0, 0]},
	{"input":({1: 9, 3: 9}, 4), "output":[0, 9, 0, 9]},
	{"input":({4: 8, 0: 5}, 5), "output":[5, 0, 0, 0, 8]},
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
	{"input": (["irn", "kelvin"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5}, {"kelvin": 4, "irn": 5, "bad": 5, "glasgow": 6, "bru": 4, "coffee": 3}, 10), "output":{1: 0.3010299956639812, 5: 0.3979400086720376}},
	{"input": (["bad", "bru", "glasgow", "glasgow"], {"bru": 0, "bad": 1, "kelvin": 2, "culture": 3, "glasgow": 4}, {"bad": 3, "glasgow": 4, "bru": 5, "kelvin": 5, "culture": 3}, 8), "output": {1: 0.4259687322722811, 0: 0.20411998265592482, 4: 0.39164905395343774}},
	{"input": (["kelvin", "city", "city"], {"kelvin": 0, "shop": 1, "culture": 2, "python": 3, "city": 4}, {"kelvin": 2, "city": 4, "culture": 2, "python": 2, "shop": 1}, 6), "output": {0: 0.47712125471966244, 4: 0.22910001000567795}},
	{"input": (["bru", "good", "glasgow"], {"coffee": 0, "good": 1, "kelvin": 2, "bru": 3, "glasgow": 4}, {"good": 5, "glasgow": 6, "bru": 5, "kelvin": 5, "coffee": 4}, 10), "output": {3: 0.3010299956639812, 1: 0.3010299956639812, 4: 0.22184874961635637}},
	{"input": (["coffee", "bru", "bru", "irn"], {"irn": 0, "city": 1, "bru": 2, "coffee": 3}, {"irn": 2, "coffee": 4, "bru": 5, "city": 3}, 6), "output": {3: 0.17609125905568124, 2: 0.10301717620200995, 0: 0.47712125471966244}},
],

"make_onehot_ignorenewtokens": [
	{"input": (["bad", "irn", "glasgow", "edinburgh", "glasgow", "bad", "bad"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5}), "output": {3: 1, 2: 1, 1: 1}},
	{"input": (["thames", "kelvin", "kelvin", "irn", "clyde", "irn"], {"coffee": 0, "shop": 1, "irn": 2, "kelvin": 3}), "output": {2: 1, 3: 1}},
	{"input": (["culture", "good", "city", "culture", "books"], {"irn": 0, "good": 1, "culture": 2, "city": 3, "glasgow": 4}), "output": {3: 1, 2: 1, 1: 1}},
	{"input": (["city", "university", "edinburgh", "city", "glasgow", "shop", "university", "library"], {"city": 0, "shop": 1, "glasgow": 2, "irn": 3, "university": 4}), "output": {0: 1, 2: 1, 1: 1, 4: 1}},
	{"input": (["shop", "shop", "shop", "bru", "irn", "vimto"], {"shop": 0, "bad": 1, "bru": 2, "irn": 3, "python": 4}), "output": {2: 1, 3: 1, 0: 1}},
],

"make_vocabulary_with_unk": lambda func : run_make_vocabulary_test(func,with_unk=True),

"make_onehot_unk": [
	{"input": (["bad", "irn", "glasgow", "edinburgh", "glasgow", "bad", "bad"], {"bru": 0, "irn": 1, "glasgow": 2, "bad": 3, "coffee": 4, "kelvin": 5, "<UNK>": 6}), "output": {3: 1, 2: 1, 1: 1, 6: 1}},
	{"input": (["thames", "kelvin", "kelvin", "irn", "clyde", "irn"], {"coffee": 0, "shop": 1, "irn": 2, "kelvin": 3, "<UNK>": 4}), "output": {2: 1, 3: 1, 4: 1}},
	{"input": (["culture", "good", "city", "culture", "books"], {"irn": 0, "good": 1, "culture": 2, "city": 3, "glasgow": 4, "<UNK>": 5}), "output": {3: 1, 2: 1, 1: 1, 5: 1}},
	{"input": (["city", "university", "edinburgh", "city", "glasgow", "shop", "university", "library"], {"city": 0, "shop": 1, "glasgow": 2, "irn": 3, "university": 4, "<UNK>": 5}), "output": {0: 1, 2: 1, 1: 1, 4: 1, 5: 1}},
	{"input": (["shop", "shop", "shop", "bru", "irn"], {"shop": 0, "bad": 1, "bru": 2, "irn": 3, "python": 4}), "output": {2: 1, 3: 1, 0: 1}},
],

"sparse_eucledean_distance": [
	{"input": ({2: 1}, {0: 3}), "output": 3.1622776601683795},
	{"input": ({1: 2, 0: 1}, {0: 4, 2: 1}), "output": 3.7416573867739413},
	{"input": ({0: 2, 4: 2}, {4: 5, 0: 2}), "output": 3.0},
	{"input": ({5: 2, 4: 4, 3: 5}, {2: 4, 0: 3, 1: 3}), "output": 8.888194417315589},
	{"input": ({1: 1, 6: 1, 2: 4}, {0: 5, 2: 3, 5: 1}), "output": 5.385164807134504},
],


"normalize_sparse_vector": [
	{"input": ({0: 3, 3: 2},), "output": {0: 0.8320502943378437, 3: 0.5547001962252291}},
	{"input": ({0: 5, 4: 4},), "output": {0: 0.7808688094430304, 4: 0.6246950475544243}},
	{"input": ({1: 5, 4: 2, 0: 5},), "output": {1: 0.6804138174397717, 4: 0.2721655269759087, 0: 0.6804138174397717}},
	{"input": ({2: 4, 0: 3, 1: 3},), "output": {2: 0.6859943405700353, 0: 0.5144957554275265, 1: 0.5144957554275265}},
	{"input": ({1: 3, 2: 1, 6: 4, 4: 5},), "output": {1: 0.42008402520840293, 2: 0.14002800840280097, 6: 0.5601120336112039, 4: 0.7001400420140048}},
],

"sparse_dot_prod": [
	{"input": ({0: 0.8320502943378437, 3: 0.5547001962252291}, {0: 1.0}), "output": 0.8320502943378437},
	{"input": ({0: 0.7808688094430304, 4: 0.6246950475544243}, {0: 0.4472135954999579, 3: 0.8944271909999159}), "output": 0.34921514788478913},
	{"input": ({1: 0.6804138174397717, 4: 0.2721655269759087, 0: 0.6804138174397717}, {3: 0.6246950475544243, 1: 0.7808688094430304}), "output": 0.531313927552782},
	{"input": ({2: 0.6859943405700353, 0: 0.5144957554275265, 1: 0.5144957554275265}, {1: 0.23570226039551587, 5: 0.23570226039551587, 2: 0.9428090415820635}), "output": 0.768029479281721},
	{"input": ({1: 0.42008402520840293, 2: 0.14002800840280097, 6: 0.5601120336112039, 4: 0.7001400420140048}, {0: 0.6509445549041194, 3: 0.39056673294247163, 6: 0.6509445549041194}), "output": 0.36460187841548625},

],

"sparse_cosine_similarity": [
	{'input': ({0: 3, 1: 4}, {1: 4, 3: 4}), 'output': 0.565685424949238},
	{'input': ({3: 5, 1: 5}, {2: 2, 3: 1}), 'output': 0.3162277660168379},
	{'input': ({3: 1, 2: 3}, {1: 1, 0: 5}), 'output': 0.0},
	{'input': ({0: 1, 1: 1}, {1: 5, 3: 4}), 'output': 0.5521576303742327},
	{'input': ({0: 2, 2: 2}, {3: 4, 0: 3}), 'output': 0.4242640687119285},
],


"tfidf_vectorize_with_sklearn": [
	{"input": (["Irn Bru is good", "Irn Bru is my favourite", "I hate Irn Bru"],), "output": [[0.39148397136265967, 0.0, 0.6628399823470976, 0.0, 0.39148397136265967, 0.5041068915759233, 0.0], [0.3263095219528963, 0.55249004708441, 0.0, 0.0, 0.3263095219528963, 0.42018292148905534, 0.55249004708441], [0.4532946552278861, 0.0, 0.0, 0.7674945674619879, 0.4532946552278861, 0.0, 0.0]]},
	{"input": (["This to shall pass", "You shall not pass", "You did not pass the ball"],), "output": [[0.0, 0.0, 0.0, 0.34520501686496574, 0.444514311537431, 0.0, 0.5844829010200651, 0.5844829010200651, 0.0], [0.0, 0.0, 0.5268201732399633, 0.40912286076708654, 0.5268201732399633, 0.0, 0.0, 0.0, 0.5268201732399633], [0.4711101009983051, 0.4711101009983051, 0.35829137488557944, 0.2782452148327134, 0.0, 0.4711101009983051, 0.0, 0.0, 0.35829137488557944]]},
	{"input": (["Yesterday I went for a walk", "I am so tired I could not walk any further"],), "output": [[0.0, 0.0, 0.0, 0.534046329052269, 0.0, 0.0, 0.0, 0.0, 0.37997836159100784, 0.534046329052269, 0.534046329052269], [0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.0, 0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.3649964681447582, 0.25969799324016246, 0.0, 0.0]]},
	{"input": (["I ate too much", "I eat therefore I am", "I ate all of the chocolate"],), "output": [[0.0, 0.0, 0.4736296010332684, 0.0, 0.0, 0.6227660078332259, 0.0, 0.0, 0.0, 0.6227660078332259], [0.0, 0.5773502691896257, 0.0, 0.0, 0.5773502691896257, 0.0, 0.0, 0.0, 0.5773502691896257, 0.0], [0.4673509818107163, 0.0, 0.35543246785041743, 0.4673509818107163, 0.0, 0.0, 0.4673509818107163, 0.4673509818107163, 0.0, 0.0]]},

],

"tfidf_vectorize_with_sklearn_and_spacy": [
	{"input": (["Irn Bru is good", "Irn Bru is my favourite", "I hate Irn Bru"],), "output": [[0.4532946552278861, 0.0, 0.7674945674619879, 0.0, 0.4532946552278861], [0.4532946552278861, 0.7674945674619879, 0.0, 0.0, 0.4532946552278861], [0.4532946552278861, 0.0, 0.0, 0.7674945674619879, 0.4532946552278861]]},
	{"input": (["This to shall pass", "You shall not pass", "You did not pass the ball"],), "output": [[0.0, 0.6133555370249717, 0.7898069290660905], [0.0, 0.6133555370249717, 0.7898069290660905], [0.8610369959439764, 0.5085423203783267, 0.0]]},
	{"input": (["Yesterday I went for a walk", "I am so tired I could not walk any further"],), "output": [[0.6316672017376245, 0.0, 0.4494364165239821, 0.6316672017376245], [0.0, 0.8148024746671689, 0.5797386715376657, 0.0]]},
	{"input": (["I ate too much", "I eat therefore I am", "I ate all of the chocolate"],), "output": [[0.0, 1.0], [0.0, 1.0], [0.8610369959439764, 0.5085423203783267]]},

],

"assign_clusters": [
	{"input": ([{0: 1, 2: 0.5}, {0: 1, 1: 0.5}, {0:1, 2:1, 5:1}], [{0: 1, 1: 0.5}, {0: 1, 2: 0.5}, {0: 1, 3: 1.}]), "output": [1, 0, 1]}
],

"compute_centroids": [
	{"input": ([{0: 1, 2: 0.5}, {0: 1, 1: 0.5}, {0:1, 2:1, 5:1}], [0, 1, 0]), "output": [{0:1., 2:0.75, 5:0.5}, {0: 1, 1: 0.5}]}
],
}

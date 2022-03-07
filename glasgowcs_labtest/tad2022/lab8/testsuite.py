
from collections import Counter

def featurizer_that_return_only_token(sentence, index):
  return [ sentence['tokens'][index] ]

def make_tests():
	return {

"train_pos_tagger": [
	{"input": ({"ner_tags": [0, 7, 0, 0, 0], "pos_tags": [40, 16, 21, 40, 7], "tokens": ["Famous", "Chinese", "panda", "recaptured", "."]}, 0), "output": ["[START]", "famous"]},
	{"input": ({"ner_tags": [0, 7, 0, 0, 0], "pos_tags": [40, 16, 21, 40, 7], "tokens": ["Famous", "Chinese", "panda", "recaptured", "."]}, 1), "output": ["O", "chinese"]},
	{"input": ({"ner_tags": [0, 7, 0, 0, 0], "pos_tags": [40, 16, 21, 40, 7], "tokens": ["Famous", "Chinese", "panda", "recaptured", "."]}, 2), "output": ["B-MISC", "panda"]},
	{"input": ({"ner_tags": [0, 7, 0, 0, 0], "pos_tags": [40, 16, 21, 40, 7], "tokens": ["Famous", "Chinese", "panda", "recaptured", "."]}, 3), "output": ["O", "recaptured"]},
	{"input": ({"ner_tags": [0, 7, 0, 0, 0], "pos_tags": [40, 16, 21, 40, 7], "tokens": ["Famous", "Chinese", "panda", "recaptured", "."]}, 4), "output": ["O", "."]},
],

"": [
	{
		'input': ([{'ner_tags': [0, 7, 0, 0, 0],
				'pos_tags': [40, 16, 21, 40, 7],
				'tokens': ['Famous', 'Chinese', 'panda', 'recaptured', '.']},
				{'ner_tags': [0, 7, 0, 0, 0],
				'pos_tags': [40, 16, 21, 40, 7],
				'tokens': ['Underwhelming', 'British', 'novel', 'published', '.']}],
				featurizer_that_return_only_token),
		'output': ([['Famous'],
				['Chinese'],
				['panda'],
				['recaptured'],
				['.'],
				['Underwhelming'],
				['British'],
				['novel'],
				['published'],
				['.']],
				['O', 'B-MISC', 'O', 'O', 'O', 'O', 'B-MISC', 'O', 'O', 'O'])
	}
	]

}

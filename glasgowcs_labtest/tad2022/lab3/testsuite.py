
def make_tests():
	return {

"unigram_token_prob": [
	{'input': ('cup', {'cup': 2, 'spoon': 2, 'glass': 6, 'fork': 1}, 11), 'output': 0.18181818181818182},
	{'input': ('plate', {'plate': 2, 'cup': 2, 'fork': 5, 'spoon': 5}, 14), 'output': 0.14285714285714285},
	{'input': ('fork', {'bowl': 4, 'fork': 5, 'plate': 3, 'cup': 1}, 13), 'output': 0.38461538461538464},
	{'input': ('cup', {'plate': 2, 'glass': 3, 'fork': 1, 'cup': 1}, 7), 'output': 0.14285714285714285},
	{'input': ('glass', {'glass': 5, 'spoon': 3}, 8), 'output': 0.625}
],


"unigram_sequence_prob": [
	{'input': (['glass', 'glass', 'glass', 'cup', 'cup'], {'cup': 2, 'spoon': 2, 'glass': 6, 'fork': 1}, 11), 'output': 0.005364760231231099},
	{'input': (['spoon', 'spoon', 'fork'], {'fork': 1, 'spoon': 5}, 6), 'output': 0.11574074074074076},
	{'input': (['fork', 'fork', 'cup', 'fork'], {'fork': 2, 'glass': 6, 'cup': 4}, 12), 'output': 0.0015432098765432098},
	{'input': (['glass', 'cup', 'fork', 'cup', 'cup'], {'cup': 5, 'glass': 3, 'fork': 1}, 9), 'output': 0.006350657928161358},
	{'input': (['spoon', 'spoon', 'spoon', 'glass'], {'fork': 1, 'glass': 1, 'bowl': 6, 'spoon': 2}, 10), 'output': 0.0008000000000000003},

],

"unigram_sequence_logprob": [
	{'input': (['glass', 'glass', 'glass', 'cup', 'cup'], {'cup': 2, 'spoon': 2, 'glass': 6, 'fork': 1}, 11), 'output': -7.542270591023018},
	{'input': (['spoon', 'spoon', 'fork'], {'fork': 1, 'spoon': 5}, 6), 'output': -3.111031312388744},
	{'input': (['fork', 'fork', 'cup', 'fork'], {'fork': 2, 'glass': 6, 'cup': 4}, 12), 'output': -9.339850002884624},
	{'input': (['glass', 'cup', 'fork', 'cup', 'cup'], {'cup': 5, 'glass': 3, 'fork': 1}, 9), 'output': -7.2988782218283195},
	{'input': (['spoon', 'spoon', 'spoon', 'glass'], {'fork': 1, 'glass': 1, 'bowl': 6, 'spoon': 2}, 10), 'output': -10.287712379549449},

],

"get_candidate_tokens": [
	{'input': ('tey', {'me': 1, 'sun': 3, 'heavy': 1, 'sea': 2, 'her': 1}), 'output': {'her', 'me', 'sea'}},
	{'input': ('cofee', {'typical': 2, 'will': 2, 'come': 3, 'codes': 1}), 'output': {'codes', 'come'}},
	{'input': ('coffee', {'spent': 3, 'coffee': 1, 'offer': 1, 'coffees': 2, 'color': 2}), 'output': ['coffee']},
	{'input': ('spda', {'pc': 2, 'spin': 1, 'pad': 1}), 'output': {'pad', 'spin'}},
	{'input': ('brw', {'arm': 1, 'mystery': 2, 'dew': 3, 'filled': 2}), 'output': {'arm', 'dew'}},

],
"blah": [


],

}

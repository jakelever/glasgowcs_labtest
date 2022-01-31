
def make_tests():
	return {

"unigram_prob": [
	{'input': ('cup', {'cup': 2, 'spoon': 2, 'glass': 6, 'fork': 1}, 11), 'output': 0.18181818181818182},
	{'input': ('plate', {'plate': 2, 'cup': 2, 'fork': 5, 'spoon': 5}, 14), 'output': 0.14285714285714285},
	{'input': ('fork', {'bowl': 4, 'fork': 5, 'plate': 3, 'cup': 1}, 13), 'output': 0.38461538461538464},
	{'input': ('cup', {'plate': 2, 'glass': 3, 'fork': 1, 'cup': 1}, 7), 'output': 0.14285714285714285},
	{'input': ('glass', {'glass': 5, 'spoon': 3}, 8), 'output': 0.625}
],

}

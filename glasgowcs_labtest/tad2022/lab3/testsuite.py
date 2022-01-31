
from collections import Counter

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
	{'input': ('coffee', {'spent': 3, 'coffee': 1, 'offer': 1, 'coffees': 2, 'color': 2}), 'output': {'coffee'}},
	{'input': ('spda', {'pc': 2, 'spin': 1, 'pad': 1}), 'output': {'pad', 'spin'}},
	{'input': ('brw', {'arm': 1, 'mystery': 2, 'dew': 3, 'filled': 2}), 'output': {'arm', 'dew'}},

],


"unigram_spelling_correct": [
	{'input': ('tey', {'heavy': 1, 'sun': 3, 'her': 1, 'sea': 2, 'me': 1}, 8), 'output': 'sea'},
	{'input': ('cofee', {'will': 2, 'codes': 2, 'come': 3, 'typical': 1}, 8), 'output': 'come'},
	{'input': ('coffee', {'offer': 3, 'coffee': 1, 'coffees': 1, 'spent': 2, 'color': 2}, 9), 'output': 'coffee'},
	{'input': ('spda', {'spin': 2, 'pad': 1, 'pc': 1}, 4), 'output': 'spin'},
	{'input': ('brw', {'mystery': 1, 'filled': 2, 'dew': 3, 'arm': 2}, 8), 'output': 'dew'},
],


"count_bigrams": [
	{'input': (['accidentally', 'halo', 'halo', 'halo'],), 'output': Counter({('halo', 'halo'): 2, ('accidentally', 'halo'): 1})},
	{'input': (['teavana', 'teavana', 'order'],), 'output': Counter({('teavana', 'teavana'): 1, ('teavana', 'order'): 1})},
	{'input': (['started', 'enough', 'enough', 'started', 'enough', 'enough'],), 'output': Counter({('started', 'enough'): 2, ('enough', 'enough'): 2, ('enough', 'started'): 1})},
	{'input': (['hario', 'hario', 'lead'],), 'output': Counter({('hario', 'hario'): 1, ('hario', 'lead'): 1})},
	{'input': (['similar', 'college', 'similar'],), 'output': Counter({('similar', 'college'): 1, ('college', 'similar'): 1})},
],

"count_trigrams": [
	{'input': (['accidentally', 'halo', 'halo', 'halo'],), 'output': Counter({('accidentally', 'halo', 'halo'): 1, ('halo', 'halo', 'halo'): 1})},
	{'input': (['teavana', 'teavana', 'order'],), 'output': Counter({('teavana', 'teavana', 'order'): 1})},
	{'input': (['started', 'enough', 'enough', 'started', 'enough', 'enough'],), 'output': Counter({('started', 'enough', 'enough'): 2, ('enough', 'enough', 'started'): 1, ('enough', 'started', 'enough'): 1})},
	{'input': (['hario', 'hario', 'lead'],), 'output': Counter({('hario', 'hario', 'lead'): 1})},
	{'input': (['similar', 'college', 'similar'],), 'output': Counter({('similar', 'college', 'similar'): 1})},
],

"bigram_token_prob": [
	{'input': ('a', 'b', {'a': 8, 'b': 7}, {('a', 'a'): 2, ('a', 'b'): 2, ('b', 'a'): 4, ('b', 'b'): 3}), 'output': 0.25},
	{'input': ('b', 'b', {'a': 8, 'b': 9}, {('a', 'a'): 1, ('a', 'b'): 2, ('b', 'a'): 1, ('b', 'b'): 4}), 'output': 0.4444444444444444},
	{'input': ('a', 'b', {'a': 7, 'b': 6}, {('a', 'a'): 3, ('a', 'b'): 1, ('b', 'a'): 1, ('b', 'b'): 1}), 'output': 0.14285714285714285},
	{'input': ('a', 'b', {'a': 7, 'b': 6}, {('a', 'a'): 1, ('a', 'b'): 3, ('b', 'a'): 4, ('b', 'b'): 2}), 'output': 0.42857142857142855},
	{'input': ('a', 'b', {'a': 5, 'b': 5}, {('a', 'a'): 1, ('a', 'b'): 2, ('b', 'a'): 2, ('b', 'b'): 1}), 'output': 0.4},
],

"bigram_spelling_correct": [
	{'input': ('i', 'hcacn', Counter({'where': 7, 'i': 6, 'can': 6}), Counter({('i', 'can'): 4, ('where', 'i'): 3})), 'output': 'can'},
	{'input': ('the', 'owvnyr', Counter({'the': 9, 'and': 8, 'owner': 5}), Counter({('and', 'the'): 2, ('the', 'owner'): 1})), 'output': 'owner'},
	{'input': ('life', 'gtze', Counter({'life': 7, 'her': 6, 'the': 6}), Counter({('her', 'life'): 3, ('life', 'the'): 1})), 'output': 'the'},
	{'input': ('it', 's', Counter({'it': 8, "'s": 7, 'says': 5}), Counter({('it', "'s"): 2, ('says', 'it'): 1})), 'output': 'it'},
	{'input': ('as', 'hmcin', Counter({'main': 9, 'linked': 8, 'as': 6}), Counter({('as', 'main'): 1, ('linked', 'as'): 1})), 'output': 'main'},
],

"trigram_token_prob": [
	{'input': ('c', 'a', 'a', Counter({('a', 'a'): 5, ('c', 'a'): 3, ('c', 'c'): 3}), Counter({('c', 'a', 'a'): 1, ('c', 'c', 'a'): 1})), 'output': 0.3333333333333333},
	{'input': ('a', 'c', 'a', Counter({('a', 'a'): 4, ('a', 'c'): 4, ('c', 'a'): 4}), Counter({('a', 'a', 'c'): 1, ('a', 'c', 'a'): 1})), 'output': 0.25},
	{'input': ('a', 'b', 'c', Counter({('a', 'a'): 5, ('a', 'b'): 4, ('b', 'c'): 4, ('c', 'a'): 4}), Counter({('a', 'b', 'c'): 2, ('c', 'a', 'a'): 2, ('a', 'a', 'b'): 1})), 'output': 0.5},
	{'input': ('c', 'b', 'b', Counter({('a', 'a'): 5, ('a', 'c'): 4, ('c', 'b'): 4, ('b', 'b'): 3}), Counter({('a', 'c', 'b'): 2, ('c', 'b', 'b'): 2, ('a', 'a', 'c'): 1})), 'output': 0.5},
	{'input': ('a', 'b', 'b', Counter({('a', 'b'): 5, ('b', 'b'): 3}), Counter({('a', 'b', 'b'): 2})), 'output': 0.4},
],


"hallucinate_text": [
	{'input': (['i', 'like'], 3, Counter({'potatoes': 5, 'like': 4, 'i': 3}), Counter({('i', 'like'): 5}), Counter({('i', 'like', 'potatoes'): 5})), 'output': ['i', 'like', 'potatoes']},
],

"unigram_token_prob_ksmooth": [
	{'input': ('cup', {'cup': 2, 'spoon': 2, 'glass': 6, 'fork': 1}, 11, 0.1), 'output': 0.18421052631578946},
	{'input': ('plate', {'plate': 2, 'cup': 2, 'fork': 5, 'spoon': 5}, 14, 0.1), 'output': 0.14583333333333334},
	{'input': ('fork', {'bowl': 4, 'fork': 5, 'plate': 3, 'cup': 1}, 13, 0.1), 'output': 0.3805970149253731},
	{'input': ('cup', {'plate': 2, 'glass': 3, 'fork': 1, 'cup': 1}, 7, 0.1), 'output': 0.14864864864864866},
	{'input': ('glass', {'glass': 5, 'spoon': 3}, 8, 0.1), 'output': 0.6219512195121951},
],

"blah": [

],

"blah": [

],


}


from collections import Counter

def make_tests():
	return {

"shift": [
	{'input': ([(0, 'ROOT')], [(1, 'Water')]), 'output': ([(0, 'ROOT'), (1, 'Water')], [])},
	{'input': ([(0, 'ROOT'), (1, 'The')], [(2, 'small'), (3, 'apple')]), 'output': ([(0, 'ROOT'), (1, 'The'), (2, 'small')], [(3, 'apple')])},
	{'input': ([(0, 'ROOT'), (1, 'Two'), (2, 'giant')], [(3, 'elephants')]), 'output': ([(0, 'ROOT'), (1, 'Two'), (2, 'giant'), (3, 'elephants')], [])}
,
	{'input': ([(0, 'ROOT')], [(1, 'Five'), (2, 'round'), (3, 'coins')]), 'output': ([(0, 'ROOT'), (1, 'Five')], [(2, 'round'), (3, 'coins')])}

,
],

"left_arc": [
	{'input': ([(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles'), (3, 'better')], [(1, 2)]), 'output': ([(0, 'ROOT'), (1, 'glasgow'), (3, 'better')], [(1, 2), (3, 2)])},
	{'input': ([(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae'), (3, 'that')], []), 'output': ([(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (3, 'that')], [(3, 2)])},
	{'input': ([(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic'), (4, '!')], [(1, 2), (2, 3)]), 'output': ([(0, 'ROOT'), (1, 'it'), (2, 'is'), (4, '!')], [(1, 2), (2, 3), (4, 3)])},
],

"right_arc": [
	{'input': ([(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles'), (3, 'better')], [(1, 2)]), 'output': ([(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles')], [(1, 2), (2, 3)])},
	{'input': ([(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae'), (3, 'that')], []), 'output': ([(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae')], [(2, 3)])},
	{'input': ([(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic'), (4, '!')], [(1, 2), (2, 3)]), 'output': ([(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic')], [(1, 2), (2, 3), (3, 4)])}
],

"run_action": [
	{'input': ('s', [(0, 'ROOT')], [(1, 'Water')], []), 'output': ('s', [(0, 'ROOT'), (1, 'Water')], [], [])},
	{'input': ('s', [(0, 'ROOT'), (1, 'The')], [(2, 'small'), (3, 'apple')], []), 'output': ('s', [(0, 'ROOT'), (1, 'The'), (2, 'small')], [(3, 'apple')], [])},
	{'input': ('s', [(0, 'ROOT'), (1, 'Two'), (2, 'giant')], [(3, 'elephants')], []), 'output': ('s', [(0, 'ROOT'), (1, 'Two'), (2, 'giant'), (3, 'elephants')], [], [])},
	{'input': ('s', [(0, 'ROOT')], [(1, 'Five'), (2, 'round'), (3, 'coins')], []), 'output': ('s', [(0, 'ROOT'), (1, 'Five')], [(2, 'round'), (3, 'coins')], [])},

	{'input': ('l', [(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles'), (3, 'better')], [], [(1, 2)]), 'output': ('l', [(0, 'ROOT'), (1, 'glasgow'), (3, 'better')], [], [(1, 2), (3, 2)])},
	{'input': ('l', [(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae'), (3, 'that')], [], []), 'output': ('l', [(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (3, 'that')], [], [(3, 2)])},
	{'input': ('l', [(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic'), (4, '!')], [], [(1, 2), (2, 3)]), 'output': ('l', [(0, 'ROOT'), (1, 'it'), (2, 'is'), (4, '!')], [], [(1, 2), (2, 3), (4, 3)])},
	
	{'input': ('r', [(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles'), (3, 'better')], [], [(1, 2)]), 'output': ('r', [(0, 'ROOT'), (1, 'glasgow'), (2, 'smiles')], [], [(1, 2), (2, 3)])},
	{'input': ('r', [(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae'), (3, 'that')], [], []), 'output': ('r', [(0, 'ROOT'), (1, 'gonnae'), (2, 'no'), (2, 'dae')], [], [(2, 3)])},
	{'input': ('r', [(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic'), (4, '!')], [], [(1, 2), (2, 3)]), 'output': ('r', [(0, 'ROOT'), (1, 'it'), (2, 'is'), (3, 'baltic')], [], [(1, 2), (2, 3), (3, 4)])}
	
],

}


import copy
import numpy as np
from collections import Counter, defaultdict

def round_data(x, places):
	"""
	Takes a data structure (potentially of nested data) and rounds all the
	floating point values into to the given number of decimal places. It works
	with nested structures (e.g. list of lists, etc).

	Data structures can contain any of dict, list, float, int, string
	Counter or defaultdict.

	Args:
		x: The data structure to round any floats within
		places: Number of decimal places to round to

	Returns:
	A copy of the data structure with any floating point
	values rounded and everything else kept the same

	"""

	if isinstance(x, dict):
		return {key:round_data(val,places) for key,val in x.items() }
	elif isinstance(x, list):
		return [round_data(val,places) for val in x ]
	elif isinstance(x, set):
		return set(round_data(val,places) for val in x)
	elif isinstance(x, Counter) or isinstance(x, defaultdict):
		copied = copy.copy(x)
		for k in copied:
			copied[k] = round_data(copied[k],places)
		return copied
	elif isinstance(x, float):
		return round(x, places)
	elif isinstance(x, int) or isinstance(x, str):
		return x
	else:
		raise RuntimeError("ERROR: Data structure contains an element that is not a dict, list, float, int, string, Counter or defaultdict")

def round_sparse_matrix(m, places):
	"""
	Rounds a scipy sparse matrix (e.g. csr_matrix) to
	the given number of decimal places.

	Args:
		m: The sparse matrix
		places: Number of decimal places to round to

	Returns:
	A copy of the sparse matrix with all values rounded

	"""
	
	m_copy = copy.deepcopy(m)
	m_copy.data = np.round(m_copy.data, 2)
	return m_copy
	
	
def to_type(x):
	"""
	Converts a variable into its type for comparison and works recursively for lists and dictionaries
	
	Args:
		x: A variable of any time
		
	Returns:
	A representation of the type of the variable (either just the type, a list of types, dictionary of types, etc)
	"""
	
	if isinstance(x, list):
		return [ to_type(j) for j in x ]
	elif isinstance(x, set):
		return set( to_type(j) for j in x )
	elif isinstance(x, dict) or isinstance(x, Counter) or isinstance(x, defaultdict):
		return { k:to_type(v) for k,v in x.items() }
	else:
		return type(x)
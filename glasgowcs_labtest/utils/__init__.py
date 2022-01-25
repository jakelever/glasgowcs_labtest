
import copy
import numpy as np

def round_data(x, places):
	"""
	Takes a data structure (potentially of nested data) and rounds all the
	floating point values into to the given number of decimal places. It works
	with nested structures (e.g. list of lists, etc).

	Data structures can contain any of dict, list, float, int or string

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
	elif isinstance(x, float):
		return round(x, places)
	elif isinstance(x, int) or isinstance(x, str):
		return x
	else:
		raise RuntimeError("ERROR: Data structure contains an element that is not a dict, list, float, int or string")

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
"""Utilities for Various Tasks"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

def format_arrays(*args):
	"""
	Format all arrays given into numpy ndarrays
	such that the last axis denotes the features.

	Parameters
	----------
	*args : tuple, default=()
		Tuple of array-like objects to convert into ndarrays.

	Returns
	-------
	arrays : list
		List of formatted ndarrays where the last axis denotes the features.
	"""
	pass

def check_dimensionality(*args):
	"""
	Check that all arguments have the same dimensionality.
	Return that dimensionality.

	Parameters
	----------
	*args : tuple, default=()
		Tuple of array-like objects or scalars to evaluate.

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	pass

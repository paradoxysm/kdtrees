# coding=utf-8

"""Utilities for Various Tasks"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

def format_array(arr, list=False):
	"""
	Format all arrays given into numpy ndarrays
	such that the last axis denotes the features.
	If the argument given is a scalar, wrap into a list first.

	Parameters
	----------
	arr : array-like
		array-like object to convert into ndarray.

	Returns
	-------
	ndarr : ndarray
		Formatted ndarrays where the last axis denotes the features.
	"""
	if np.isscalar(arr):
		return np.asarray([arr])
	np_arr = np.asarray(arr)
	if list:
		if np_arr.ndim != np_arr.shape[-1]:
			return np_arr[:, np.new_axis]
		else:
			return np_arr
	else:
		return np.squeeze(np_arr)


def check_dimensionality(*args):
	"""
	Check that all arguments have the same dimensionality.
	Return that dimensionality.

	Parameters
	----------
	*args : tuple, default=()
		Tuple of ndarrays where the last axis denotes the features.

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	if len(args) == 0:
		raise ValueError("Must contain at least one argument")
	if np.any(args == None):
		raise ValueError("Must contain non-None arguments")
	if np.any(not isinstance(args, np.ndarray)):
		raise ValueError("Must contain ndarray arguments")
	dim = None
	for arg in args:
		if dim is None:
			dim = arg.shape[-1]
		elif dim != arg.shape[-1]:
			raise ValueError("Arguments must be the same dimensions")
	return dim

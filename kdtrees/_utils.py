# coding=utf-8

"""Utilities for Various Tasks"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

def _is_builtin(obj):
	"""
	Check if the type of `obj` is a builtin type.

	Parameters
	----------
	obj : object
		Object in question.

	Returns
	-------
	builtin : bool
		True if `obj` is a builtin type
	"""
	return obj.__class__.__module__ == 'builtins'

def format_array(arr, l=False):
	"""
	Format the given array or scalar into a numpy ndarray
	such that the last axis denotes the features.
	If the argument given is a scalar, wrap into a list first.

	Parameters
	----------
	arr : array-like or scalar
		Array-like object or scalar to convert into ndarray.

	l : bool
		`l` should be set to True if `arr` is a list of items.

	Returns
	-------
	ndarr : ndarray
		Formatted ndarray where the last axis denotes the features.
	"""
	if not isinstance(arr, (np.ndarray, np.generic)) and \
			not _is_builtin(arr):
		raise ValueError("Must be an array-like or scalar built from standard types")
	if np.isscalar(arr):
		return np.asarray([arr])
	np_arr = np.asarray(arr)
	if list:
		if np_arr.shape != () and np_arr.ndim != np_arr.shape[-1]:
			return np_arr[:, np.newaxis]
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

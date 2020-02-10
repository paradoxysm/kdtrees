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


def format_array(arr, l=False, accept=None):
	"""
	Format the given array or scalar into a numpy ndarray
	such that the last axis denotes the features.
	If the argument given is a scalar, wrap into a list first.

	Parameters
	----------
	arr : array-like or scalar
		Array-like object or scalar to convert into ndarray.

	l : bool
		`l` should be set to True if `arr` is semantically a list of items.

	Returns
	-------
	ndarr : ndarray
		Formatted ndarray where the last axis denotes the features.
	"""
	accept_types = (np.ndarray, np.generic)
	if accept:
		accept_types += accept
	if not isinstance(arr, accept_types) and \
			not _is_builtin(arr):
		raise ValueError("Must be an array-like or scalar built from standard types")
	if np.isscalar(arr):
		return np.asarray([arr])
	np_arr = np.asarray(arr)
	if l:
		if np_arr.shape != () and (np_arr.ndim != np_arr.shape[-1] or \
				(np_arr.shape[0] == 1 and np_arr.ndim <= 1)):
			return np_arr[:, np.newaxis]
		return np_arr
	else:
		if np_arr.shape != () and np_arr.size != 1:
			return np.squeeze(np_arr)
		np_arr = np.squeeze(np_arr)
		np_arr.shape = (1,)
		return np_arr


def check_dimensionality(*args, l=False, accept=None):
	"""
	Check that all arguments have the same dimensionality.
	Return that dimensionality.

	Parameters
	----------
	*args : tuple, default=()
		Tuple of array-like objects where the last axis denotes the features.

	l : bool
		`l` should be set to True if `args` is a tuple where every
		item is semantically a list of items.

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	if len(args) == 0:
		raise ValueError("Must contain at least one argument")
	np_args = []
	for a in args:
		np_args.append(format_array(a, l=l, accept=accept))
	dim = None
	for arg in np_args:
		if dim is None:
			dim = arg.shape[-1]
		elif dim != arg.shape[-1]:
			raise ValueError("Arguments must be the same dimensions")
	return dim

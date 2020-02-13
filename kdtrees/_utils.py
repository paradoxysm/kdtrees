# coding=utf-8

"""Utilities for Various Tasks"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

def _is_acceptable_type(obj, builtin=True, accept=None):
	"""
	Check if the type of `obj` is a builtin type or an `accept` type.

	Parameters
	----------
	obj : object
		Object in question.

	builtin : bool, default=True
		Also check if `obj` is a builtin type.

	accept : None or array-like, default=None
		List of accept override types. Allow `obj` to be this type.

	Returns
	-------
	acceptable : bool
		True if `obj` is an acceptable type
	"""
	acceptable = False
	if accept:
		acceptable = isinstance(obj, tuple(accept))
	if builtin:
		return obj.__class__.__module__ == 'builtins' or acceptable
	return acceptable

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

	accept : None or object, default=None
		Accept override type. Allow `arr` to be this type.

	Returns
	-------
	ndarr : ndarray
		Formatted ndarray where the last axis denotes the features.
	"""
	accept_types = [np.ndarray, np.generic]
	if accept:
		accept_types.append(accept)
	if not _is_acceptable_type(arr, builtin=True, accept=accept_types):
		raise ValueError("Must be an array-like or scalar built from acceptable types")
	if np.isscalar(arr) or (accept and isinstance(arr, accept)):
		return np.asarray([arr])
	np_arr = np.asarray(arr)
	if accept:
		return np_arr
	if l:
		if np_arr.shape != () and np_arr.ndim <= 1:
			return np_arr[:, np.newaxis]
		elif len(np_arr) <= 1 or np_arr.shape[-1] == 1:
			return np_arr
		return np.squeeze(np_arr)
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

	If `accept` is an object that contains a `dim`
	attribute, use that instead.

	Parameters
	----------
	*args : tuple, default=()
		Tuple of ndarray objects where the last axis denotes the features.
		If `accept` is an object, it can be this type.

	l : bool
		`l` should be set to True if `args` is a tuple where every
		item is semantically a list of items.

	accept : None or object, default=None
		Accept override type. Check the `dim` attribute of this object

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	if len(args) == 0:
		raise ValueError("Must contain at least one argument")
	if accept:
		try:
			dim = args[0].dim
			for a in args[1:]:
				if a.dim != dim:
					raise ValueError()
			return dim
		except AttributeError:
			raise AttributeError("Arguments must contain attribute `dim`")
		except ValueError:
			raise ValueError("Arguments must be the same dimensions")
	else:
		np_args = []
		for a in args:
			np_args.append(format_array(a, l=l))
		dim = np_args[0].shape[-1]
		for arg in np_args[1:]:
			if dim != arg.shape[-1]:
				raise ValueError("Arguments must be the same dimensions")
		return dim

def distance(obj1, obj2, accept=None):
	"""
	Calculate the distance between `obj1` and `obj2`,
	using norm.

	If `accept` is an object that contains a `distance`
	function, use that instead. Uses `obj1.distance(obj2)`.

	Parameters
	----------
	obj1 : array-like or object, default=()
		Tuple of array-like objects where the last axis denotes the features.

	l : bool
		`l` should be set to True if `args` is a tuple where every
		item is semantically a list of items.

	accept : None or object, default=None
		Accept override type. Check the dimensionality attribute of this object

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	if accept:
		if isinstance(obj1, accept) and isinstance(obj2, accept):
			return obj1.distance(obj2)
		raise ValueError("`obj1` and `obj2` must be the same type as `accept`")
	else:
		try:
			return np.linalg.norm(obj1 - obj2)
		except:
			raise ValueError("`obj1` and `obj2` must be vectors or scalars")

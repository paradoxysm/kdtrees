# coding=utf-8

"""Utilities for Various Tasks"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

def check_dimensionality(*args, accept=None):
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

	accept : None or object, default=None
		Accept override type. Check the `dim` attribute of this object.

	Returns
	-------
	dim : int
		The dimensionality of all given arguments.
	"""
	if len(args) == 0:
		raise ValueError("Must contain at least one argument")
	try:
		if accept:
			dims = [a.dim for a in args]
		else:
			dims = [np.asarray(a).shape[-1] for a in args]
		dim = dims[0]
		for d in dims[1:]:
			if d != dim:
				raise ValueError("Arguments must be the same dimensions")
		return dim
	except AttributeError:
		print(args)
		raise AttributeError("Arguments must contain attribute `dim`")

def distance(obj1, obj2, accept=None):
	"""
	Calculate the distance between `obj1` and `obj2`,
	using norm.

	If `accept` is an object that contains a `distance`
	function, use that instead. Uses `obj1.distance(obj2)`.

	Parameters
	----------
	obj1 : ndarray or scalar or object
		ndarray or scalar where the last axis denotes the features.
		If `accept` is an object, it can be this type.

	obj2 : ndarray or scalar or object
		ndarray or scalar where the last axis denotes the features.
		If `accept` is an object, it can be this type.

	accept : None or object, default=None
		Accept override type. Use the `distance` function of this type.

	Returns
	-------
	distance : int
		The distance between `obj1` and `obj2`.
	"""
	if accept:
		if isinstance(obj1, accept) and isinstance(obj2, accept):
			return obj1.distance(obj2)
		raise ValueError("`obj1` and `obj2` must be the same type as `accept`")
	else:
		return np.linalg.norm(obj1 - obj2)

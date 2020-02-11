# coding=utf-8

"""Abstract base super class for acceptable type overrides"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

from abc import ABC, abstractmethod

class KDTreeType(ABC, list):
	"""
	An abstract base super class (interface) for creating custom
	types that kdtrees can accept. Any custom type must extend
	KDTreeType to be acceptable. Based on the purpose of a K-D Tree,
	KDTreeTypes must be comparable, indexable, and iterable.
	"""
	def __init__(self):
		pass

	def __eq__(self, other):
		"""
		Determine if `other` is equivalent to this `KDTreeType`.

		Parameters
		----------
		other : object
			The object in question.

		Returns : bool
			True if `other` is equivalent to this `KDTreeType`
		"""
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		"""
		Determine if `other` is not equivalent to this `KDTreeType`.

		Parameters
		----------
		other : object
			The object in question.

		Returns : bool
			True if `other` is not equivalent to this `KDTreeType`
		"""
		return not self.__eq__(other)

	@abstractmethod
	def __len__(self):
		"""
		Return the 'length' of the KDTreeType. This needs to be
		defined based on the custom implementation.

		Returns : int
			The 'length' of this `KDTreeType`.
		"""
		raise NotImplementedError("__len__ not implemented")

	@abstractmethod
	def __getitem__(self, key):
		"""
		Return the 'item' and the 'index', `key`, of the KDTreeType.
		This needs to be defined based on the custom implementation.

		Returns : object
			The 'item' and the 'index', `key`, of the KDTreeType.
		"""
		raise NotImplementedError("__getitem__ not implemented")

	@abstractmethod
	def __iter__(self):
		"""
		Return the next 'item' of the KDTreeType.
		This needs to be defined based on the custom implementation.

		Yields : object
			The next 'item' of the KDTreeType.
		"""
		raise NotImplementedError("__iter__ not implemented")

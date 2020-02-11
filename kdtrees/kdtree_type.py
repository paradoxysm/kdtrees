from abc import ABC, abstractmethod

class KDTreeType(ABC, list):

	def __init__(self):
		pass

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	@abstractmethod
	def __len__(self):
		raise NotImplementedError("__len__ not implemented")

	@abstractmethod
	def __getitem__(self, key):
		raise NotImplementedError("__getitem__ not implemented")

	@abstractmethod
	def __iter__(self):
		raise NotImplementedError("__iter__ not implemented")

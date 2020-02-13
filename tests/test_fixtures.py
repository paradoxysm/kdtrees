import pytest
import numpy as np

from kdtrees import KDTreeType

class KDSubType(KDTreeType):
	def __init__(self, dim, a):
		super().__init__(dim)
		self.a = a
	def distance(self, other):
		return np.abs(self.a - other.a)
	def __lt__(self, other):
		if isinstance(other, KDSubType):
			return self.a < other.a
		else:
			return self.a < other
	def __getitem__(self, i):
		return self.a

class KDBadType(KDTreeType):
	def __init__(self, dim, a):
		super().__init__(dim)
		self.a = a

class BadType:
	def __init__(self):
		self.bad = True

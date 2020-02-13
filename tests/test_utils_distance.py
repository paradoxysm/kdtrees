import pytest
import numpy as np

from kdtrees import _utils as utils
from kdtrees import KDTreeType

@pytest.fixture
def kd_subtype():
	class KDSubType(KDTreeType):
		def __init__(self, dim, a):
			super().__init__(dim)
			self.a = a
		def distance(self, other):
			return 1
	return KDSubType

@pytest.fixture
def bad_type():
	class BadType:
		def __init__(self):
			self.bad = True
	return BadType

def test_distance():
	assert utils.distance(1,0) == 1

def test_distance_mismatch(kd_subtype):
	with pytest.raises(ValueError):
		utils.distance(kd_subtype(1,1), 1)

def test_distance_accept(kd_subtype):
	assert utils.distance(kd_subtype(1,1), kd_subtype(1,1), accept=kd_subtype) == 1

def test_distance_accept_mismatch(kd_subtype):
	with pytest.raises(ValueError):
		utils.distance(kd_subtype(1,1), 0, accept=kd_subtype)

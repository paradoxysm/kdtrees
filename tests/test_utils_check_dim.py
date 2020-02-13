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

@pytest.mark.parametrize("args,dim_l,dim_exp", [
	([0,1], False, 1),
	([0], False, 1),
	([0,1,2], True, 1),
	([[0]], False, 1),
	([[0]], True, 1),
	([[0,1]], False, 2),
	([[0,1]], True, 1),
	([[[0,1]]], False, 2),
	([[[0,1]]], True, 2),
	([[[0,1],[2,3]]], True, 2),
	(np.asarray([0,1]), True, 1),
	(utils.format_array([0,1], l=True), True, 1)
])

def test_check_dimensionality(args, dim_l, dim_exp):
	if len(args) > 1:
		assert utils.check_dimensionality(*args, l=dim_l) == dim_exp
	else:
		assert utils.check_dimensionality(args[0], l=dim_l) == dim_exp

def test_check_dimensionality_accept(kd_subtype):
	assert utils.check_dimensionality(kd_subtype(1,1), accept=kd_subtype) == 1

def test_check_dimensionality_no_args():
	with pytest.raises(ValueError):
		utils.check_dimensionality()

def test_check_dimensionality_mismatch():
	with pytest.raises(ValueError):
		utils.check_dimensionality(0, [0,1])

def test_check_dimensionality_no_dim(bad_type):
	with pytest.raises(AttributeError):
		utils.check_dimensionality(bad_type(), accept=bad_type)

def test_check_dimensionality_no_shape():
	with pytest.raises(AttributeError):
		utils.check_dimensionality(0, accept=bad_type)

def test_check_dimensionality_mismatch_accept(kd_subtype):
	with pytest.raises(ValueError):
		utils.check_dimensionality(kd_subtype(1,1), kd_subtype(2,1), accept=kd_subtype)

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

@pytest.mark.parametrize("obj,builtin_exp", [
	(0, True),
	([], True),
	("abc", True),
	(np.int32(2), False)
])

def test_is_acceptable_type(obj, builtin_exp):
	assert utils._is_acceptable_type(obj) == builtin_exp

def test_is_acceptable_type_accept(kd_subtype):
	assert utils._is_acceptable_type(kd_subtype(1,1), builtin=False, accept=[kd_subtype])

@pytest.mark.parametrize("arr,format_l,format_exp", [
	(0, False, np.asarray([0])),
	(0, True, np.asarray([0])),
	([0], False, np.asarray([0])),
	([[0],[1]], True, np.asarray([[0],[1]])),
	([[0]], False, np.asarray([0])),
	([0], True, np.asarray([[0]])),
	([0,1], False, np.asarray([0,1])),
	([0,1], True, np.asarray([[0],[1]])),
	([[0,1]], False, np.asarray([0,1])),
	([[0,1]], True, np.asarray([[0,1]])),
	([[0,1],[2,3]], True, np.asarray([[0,1],[2,3]])),
	(np.asarray([0,1]), True, np.asarray([[0],[1]])),
	([[0,1,2],[2,3,4]], True, np.asarray([[0,1,2],[2,3,4]])),
])

def test_format_array(arr, format_l, format_exp):
	assert np.array_equal(utils.format_array(arr, l=format_l), format_exp)

def test_format_array_wrong_type(bad_type):
	with pytest.raises(ValueError):
		utils.format_array(bad_type())

def test_format_array_override_type(kd_subtype):
	assert utils.format_array(kd_subtype(1,1), accept=kd_subtype) == np.asarray([kd_subtype(1,1)])
	assert utils.format_array([kd_subtype(1,1)], accept=kd_subtype) == np.asarray([kd_subtype(1,1)])

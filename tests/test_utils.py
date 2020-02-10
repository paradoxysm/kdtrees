import pytest
import numpy as np

from kdtrees import _utils as utils

@pytest.mark.parametrize("obj,builtin_exp", [
	(0, True),
	([], True),
	("abc", True),
	(np.int32(2), False)
])

def test_is_builtin(obj, builtin_exp):
	assert utils._is_builtin(obj) == builtin_exp

@pytest.mark.parametrize("arr,format_l,format_exp", [
	(0, False, np.asarray([0])),
	(0, True, np.asarray([0])),
	([0], False, np.asarray([0])),
	([[0]], False, np.asarray([0])),
	([0], True, np.asarray([[0]])),
	([0,1], False, np.asarray([0,1])),
	([0,1], True, np.asarray([[0],[1]])),
	([[0,1]], False, np.asarray([0,1])),
	([[0,1]], True, np.asarray([[0,1]])),
	([[0,1],[2,3]], True, np.asarray([[0,1],[2,3]])),
	(np.asarray([0,1]), True, np.asarray([[0],[1]]))
])

def test_format_array(arr, format_l, format_exp):
	assert np.array_equal(utils.format_array(arr, l=format_l), format_exp)

def test_format_array_wrong_type():
	with pytest.raises(ValueError):
		class BadType:
			def __init__(self):
				self.bad = True
		assert utils.format_array(BadType())

@pytest.mark.parametrize("args,dim_l,dim_exp", [
	([0,1], False, 1),
	([0], False, 1),
	([[0]], False, 1),
	([[0]], True, 1),
	([[0,1]], False, 2),
	([[0,1]], True, 1),
	([[[0,1]]], False, 2),
	([[[0,1]]], True, 2),
	([[[0,1],[2,3]]], True, 2),
	(np.asarray([0,1]), True, 1)
])

def test_check_dimensionality(args, dim_l, dim_exp):
	if len(args) > 1:
		assert utils.check_dimensionality(*args, l=dim_l) == dim_exp
	else:
		assert utils.check_dimensionality(args[0], l=dim_l) == dim_exp

def test_check_dimensionality_no_args():
	with pytest.raises(ValueError):
		utils.check_dimensionality()

def test_check_dimensionality_mismatch():
	with pytest.raises(ValueError):
		utils.check_dimensionality(0, [0,1])

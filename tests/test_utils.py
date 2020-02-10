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

@pytest.mark.parametrize("arr,l,format_exp", [
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

def test_format_array(arr, l, format_exp):
	assert np.array_equal(utils.format_array(arr, l=l), format_exp)

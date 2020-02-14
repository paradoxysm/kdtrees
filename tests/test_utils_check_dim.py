import pytest
import numpy as np

from kdtrees import _utils as utils
from .test_fixtures import KDSubType, BadType

@pytest.mark.parametrize("args,dim_exp", [
	([[0],[1]], 1),
	([[0]], 1),
	([[0],[1],[2]], 1),
	([[0]], 1),
	([[0,1]], 2),
	([[[0],[1]]], 1),
	([[[0,1]]], 2),
	([[[0,1]]], 2),
	([[[0,1],[2,3]]], 2),
	([np.asarray([0,1])], 2),
])

def test_check_dimensionality(args, dim_exp):
	if len(args) > 1:
		assert utils.check_dimensionality(*args) == dim_exp
	else:
		assert utils.check_dimensionality(args[0]) == dim_exp

def test_check_dimensionality_accept():
	assert utils.check_dimensionality(KDSubType(1,1), accept=KDSubType) == 1

def test_check_dimensionality_no_args():
	with pytest.raises(ValueError):
		utils.check_dimensionality()

def test_check_dimensionality_mismatch():
	with pytest.raises(ValueError):
		utils.check_dimensionality([0], [0,1])

def test_check_dimensionality_no_dim():
	with pytest.raises(AttributeError):
		utils.check_dimensionality(BadType(), accept=BadType)

def test_check_dimensionality_no_shape():
	with pytest.raises(AttributeError):
		utils.check_dimensionality([0], accept=BadType)

def test_check_dimensionality_mismatch_accept():
	with pytest.raises(ValueError):
		utils.check_dimensionality(KDSubType(1,1), KDSubType(2,1), accept=KDSubType)

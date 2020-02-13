import pytest
import numpy as np

from kdtrees import _utils as utils
from .test_fixtures import KDSubType, BadType

def test_distance_1D():
	assert utils.distance(1,0) == 1

def test_distance_2D():
	assert utils.distance(np.asarray([1,1]),np.asarray([0,0])) == np.sqrt(2)

def test_distance_mismatch():
	with pytest.raises(ValueError):
		utils.distance(KDSubType(1,1), 1, accept=KDSubType)

def test_distance_accept():
	assert utils.distance(KDSubType(1,1), KDSubType(1,1), accept=KDSubType) == 0

def test_distance_accept_mismatch():
	with pytest.raises(ValueError):
		utils.distance(KDSubType(1,1), 0, accept=KDSubType)

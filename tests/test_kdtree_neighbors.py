import pytest
import numpy as np

from kdtrees import KDTree

def test_1NN():
	tree = KDTree.initialize([1,4])
	assert np.all(tree.nearest_neighbor(3) == np.asarray([[4,1]]))

def test_2NN():
	tree = KDTree.initialize([1,5,6])
	assert np.all(tree.nearest_neighbor(4, n=2) == np.asarray([[5,1],[6,2]]))

def test_KNN_mismatch():
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		tree.nearest_neighbor([0,0])

def test_d0PN():
	tree = KDTree.initialize([1,4])
	assert np.all(tree.proximal_neighbor(3) == np.asarray([]))

def test_d1PN():
	tree = KDTree.initialize([1,4])
	assert np.all(tree.proximal_neighbor(3, d=1) == np.asarray([[4,1]]))

def test_d2PN():
	tree = KDTree.initialize([1,5,6])
	assert np.all(tree.proximal_neighbor(4, d=2) == np.asarray([[5,1],[6,2]]))

def test_dPN_mismatch():
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		assert tree.proximal_neighbor([0,0])

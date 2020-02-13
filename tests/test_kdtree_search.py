import pytest
import numpy as np

from kdtrees import KDTree

def test_search_1D():
	tree = KDTree([1])
	right = KDTree([2])
	left = KDTree([0])
	tree.right = right
	tree.left = left
	assert tree.search(2) == right
	assert tree.search(0) == left
	assert tree.search(3) is None
	assert tree.search(-1) is None

def test_search_mismatch():
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		tree.search([0,0])

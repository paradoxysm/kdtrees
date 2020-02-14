import pytest
import numpy as np

from kdtrees import KDTree
from .test_fixtures import KDSubType, BadType

def test_search_1D():
	tree = KDTree([1])
	right = KDTree([2])
	left = KDTree([0])
	tree.right = right
	tree.left = left
	assert tree.search([2]) == right
	assert tree.search([0]) == left
	assert tree.search([3]) is None
	assert tree.search([-1]) is None

def test_search_2D():
	tree = KDTree([1,1], k=2)
	right = KDTree([1,2], k=2, axis=1)
	tree.right = right
	assert tree.search([1,2]) == right
	assert tree.search([1,0]) is None

def test_search_accept():
	tree = KDTree(KDSubType(1,1), accept=KDSubType)
	left = KDTree(KDSubType(1,0), accept=KDSubType)
	tree.left = left
	assert tree.search(KDSubType(1,0)) == left
	assert tree.search(KDSubType(1,3)) is None

def test_search_mismatch():
	tree = KDTree.initialize([[1],[2]])
	with pytest.raises(ValueError):
		tree.search([0,0])

def test_search_mismatch_accept():
	tree = KDTree.initialize([KDSubType(1,0), KDSubType(1,1)], accept=KDSubType)
	with pytest.raises(ValueError):
		tree.search(KDSubType(2,0))
	with pytest.raises(AttributeError):
		tree.search(0)

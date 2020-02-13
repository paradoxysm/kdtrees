import pytest
import numpy as np

from kdtrees import KDTree

@pytest.mark.parametrize("points_1d_delete,delete_1d, delete_1d_exp", [
	([4,2,5,3,7,1,9], 3, "[4], axis: 0, nodes: 6\n" + \
							"\t[7], axis: 0, nodes: 3\n" + \
							"\t\t[9], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n" + \
							"\t\t[5], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n" + \
							"\t[2], axis: 0, nodes: 2\n" + \
							"\t\tNone\n"
							"\t\t[1], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n"
							),
	([1,2,3], 3, "[2], axis: 0, nodes: 2\n" + \
					"\tNone\n" + \
					"\t[1], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					),
	([1,2], 1, "[2], axis: 0, nodes: 1\n" + \
					"\tNone\n" + "\tNone\n"
					),
	([1,2], 2, "[1], axis: 0, nodes: 1\n" + \
					"\tNone\n" + "\tNone\n"
					),
	([1,2], 3, "[2], axis: 0, nodes: 2\n" + \
					"\tNone\n" + \
					"\t[1], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					),
	([1,2], 0, "[2], axis: 0, nodes: 2\n" + \
					"\tNone\n" + \
					"\t[1], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					),
	([1,2,3,4], 4, "[2], axis: 0, nodes: 3\n" + \
					"\t[3], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					"\t[1], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					),
])

def test_delete_1D(points_1d_delete, delete_1d, delete_1d_exp, capsys):
	tree = KDTree.initialize(points_1d_delete)
	tree = tree.delete(delete_1d)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == delete_1d_exp

@pytest.mark.parametrize("points_2d_delete,delete_2d,delete_2d_exp", [
	([[0,0],[1,1],[1,0]], [1,0], "[1 1], axis: 0, nodes: 2\n" + \
									"\tNone\n" + \
									"\t[0 0], axis: 1, nodes: 1\n" + \
									"\t\tNone\n\t\tNone\n"
									),
	([[0,0],[1,1],[1,0]], [2,0], "[1 1], axis: 0, nodes: 3\n" + \
									"\t[1 0], axis: 1, nodes: 1\n" + \
									"\t\tNone\n\t\tNone\n" + \
									"\t[0 0], axis: 1, nodes: 1\n" + \
									"\t\tNone\n\t\tNone\n"
									),
])

def test_delete_2D(points_2d_delete, delete_2d, delete_2d_exp, capsys):
	tree = KDTree.initialize(points_2d_delete)
	tree = tree.delete(delete_2d)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == delete_2d_exp

def test_delete_mismatch():
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		tree.delete([0,0])

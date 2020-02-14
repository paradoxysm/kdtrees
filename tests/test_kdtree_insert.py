import pytest
import numpy as np

from kdtrees import KDTree

@pytest.mark.parametrize("points_1d_insert,insert_1d, insert_1d_exp", [
	([[4],[2],[5],[7],[1],[9]], np.array([3]), "[4], axis: 0, nodes: 7\n" + \
							"\t[7], axis: 0, nodes: 3\n" + \
							"\t\t[9], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n" + \
							"\t\t[5], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n" + \
							"\t[2], axis: 0, nodes: 3\n" + \
							"\t\t[3], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n"
							"\t\t[1], axis: 0, nodes: 1\n" + \
							"\t\t\tNone\n" + "\t\t\tNone\n"
							),
	([[1],[2]], np.array([3]), "[2], axis: 0, nodes: 3\n" + \
					"\t[3], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n" + \
					"\t[1], axis: 0, nodes: 1\n" + \
					"\t\tNone\n" + "\t\tNone\n"
					),
])

def test_insert_1D(points_1d_insert, insert_1d, insert_1d_exp, capsys):
	tree = KDTree.initialize(points_1d_insert)
	tree = tree.insert(insert_1d)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == insert_1d_exp

@pytest.mark.parametrize("points_2d_insert,insert_2d,insert_2d_exp", [
	([[0,0],[1,1]], np.array([1,0]), "[1 1], axis: 0, nodes: 3\n" + \
							"\t[1 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n" + \
							"\t[0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n"
							),
	([[0,0],[1,1],[1,0]], np.array([2,0]), "[1 1], axis: 0, nodes: 4\n" + \
									"\t[1 0], axis: 1, nodes: 2\n" + \
									"\t\t[2 0], axis: 0, nodes: 1\n" + \
									"\t\t\tNone\n\t\t\tNone\n" + \
									"\t\tNone\n" + \
									"\t[0 0], axis: 1, nodes: 1\n" + \
									"\t\tNone\n\t\tNone\n"
									),
	([[0,0],[1,1]], np.array([0,0]), "[1 1], axis: 0, nodes: 2\n" + \
							"\tNone\n" + \
							"\t[0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n"
							),
])

def test_insert_2D(points_2d_insert, insert_2d, insert_2d_exp, capsys):
	tree = KDTree.initialize(points_2d_insert)
	tree = tree.insert(insert_2d)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == insert_2d_exp

def test_insert_mismatch():
	tree = KDTree.initialize([[1],[2]])
	with pytest.raises(ValueError):
		tree.insert([0,0])

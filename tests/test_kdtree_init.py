import pytest
import numpy as np

from kdtrees import KDTree
from .test_fixtures import KDSubType

def test_init():
	tree = KDTree(0)
	assert tree.value == 0
	assert tree.k == 1
	assert tree.axis == 0
	assert tree.left == None
	assert tree.right == None
	assert tree.nodes == 1

def test_init_with_params():
	tree = KDTree([0,0], k=2, axis=1)
	assert tree.value == [0,0]
	assert tree.k == 2
	assert tree.axis == 1
	assert tree.left == None
	assert tree.right == None
	assert tree.nodes == 1

@pytest.mark.parametrize("points_1d,init_1d_exp", [
	([[4],[2],[5],[7],[1],[9]], np.asarray([5])),
	([[1],[2],[3],[4],[5],[6],[7]], np.asarray([4])),
	([[3],[2],[1]], np.asarray([2])),
])

def test_initialize_1D(points_1d, init_1d_exp):
	tree = KDTree.initialize(points_1d)
	assert np.all(tree.value == init_1d_exp)

@pytest.mark.parametrize("points_2d,init_2d_exp", [
	([[0,0],[1,1],[2,0]],  "[1 1], axis: 0, nodes: 3\n" + \
							"\t[2 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n" + \
							"\t[0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n"
							),
])

def test_initialize_2D(points_2d, init_2d_exp, capsys):
	tree = KDTree.initialize(points_2d)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == init_2d_exp

@pytest.mark.parametrize("points_3d,init_3d_exp", [
	([[0,0,0],[1,1,1],[0,2,0]], np.asarray([0,2,0])),
])

def test_initialize_3D(points_3d, init_3d_exp):
	tree = KDTree.initialize(points_3d)
	assert np.all(tree.value == init_3d_exp)

@pytest.mark.parametrize("points_type, init_type_exp", [
	([KDSubType(2,[-1,1]),KDSubType(2,[0,0]), KDSubType(2,[1,1]), KDSubType(2,[1,0])],
		KDSubType(2,[1,1])),
])

def test_initialize_accept(points_type, init_type_exp):
	tree = KDTree.initialize(points_type, accept=KDSubType)
	assert np.all(tree.value == init_type_exp)
	assert np.all(tree.right.value == KDSubType(2, [1,0]))
	assert np.all(tree.left.value == KDSubType(2, [-1,1]))
	assert np.all(tree.left.left.value == KDSubType(2, [0,0]))

@pytest.mark.parametrize("points_vis,vis_exp", [
	([[0,0,0],[1,1,1],[0,2,0]], "[0 2 0], axis: 0, nodes: 3\n" + \
							"\t[1 1 1], axis: 1, nodes: 1\n" + \
							"\t\tNone\n" + "\t\tNone\n" + \
							"\t[0 0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n" + "\t\tNone\n"
							),
	([[4],[2],[5],[7],[1],[9],[3]], "[4], axis: 0, nodes: 7\n" + \
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
	([[4],[2],[5],[7],[1],[9]], "[5], axis: 0, nodes: 6\n" + \
						"\t[9], axis: 0, nodes: 2\n" + \
						"\t\tNone\n" + \
						"\t\t[7], axis: 0, nodes: 1\n" + \
						"\t\t\tNone\n" + "\t\t\tNone\n" + \
						"\t[2], axis: 0, nodes: 3\n" + \
						"\t\t[4], axis: 0, nodes: 1\n" + \
						"\t\t\tNone\n" + "\t\t\tNone\n"
						"\t\t[1], axis: 0, nodes: 1\n" + \
						"\t\t\tNone\n" + "\t\t\tNone\n"
						),
])

def test_visualize(points_vis, vis_exp, capsys):
	tree = KDTree.initialize(points_vis)
	tree.visualize()
	captured = capsys.readouterr()
	assert captured.out == vis_exp

def test_initialize_error():
	with pytest.raises(ValueError):
		class BadType:
			def __init__(self):
				self.bad = True
		KDTree.initialize([[0,0,0],[1,1,1],[0,2,0]], accept=BadType)

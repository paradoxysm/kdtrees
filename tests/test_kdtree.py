import pytest
import numpy as np

from kdtrees import KDTree

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
	([4,2,5,7,1,9], np.asarray([5])),
	([1,2,3,4,5,6,7], np.asarray([4])),
	([3,2,1], np.asarray([2])),
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

@pytest.mark.parametrize("points_vis,vis_exp", [
	([[0,0,0],[1,1,1],[0,2,0]], "[0 2 0], axis: 0, nodes: 3\n" + \
							"\t[1 1 1], axis: 1, nodes: 1\n" + \
							"\t\tNone\n" + "\t\tNone\n" + \
							"\t[0 0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n" + "\t\tNone\n"
							),
	([4,2,5,7,1,9,3], "[4], axis: 0, nodes: 7\n" + \
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
	([4,2,5,7,1,9], "[5], axis: 0, nodes: 6\n" + \
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
		assert KDTree.initialize([[0,0,0],[1,1,1],[0,2,0]], accept=BadType)

@pytest.mark.parametrize("points_1d_insert,insert_1d, insert_1d_exp", [
	([4,2,5,7,1,9], 3, "[4], axis: 0, nodes: 7\n" + \
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
	([1,2], 3, "[2], axis: 0, nodes: 3\n" + \
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
	([[0,0],[1,1]], [1,0], "[1 1], axis: 0, nodes: 3\n" + \
							"\t[1 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n" + \
							"\t[0 0], axis: 1, nodes: 1\n" + \
							"\t\tNone\n\t\tNone\n"
							),
	([[0,0],[1,1],[1,0]], [2,0], "[1 1], axis: 0, nodes: 4\n" + \
									"\t[1 0], axis: 1, nodes: 2\n" + \
									"\t\t[2 0], axis: 0, nodes: 1\n" + \
									"\t\t\tNone\n\t\t\tNone\n" + \
									"\t\tNone\n" + \
									"\t[0 0], axis: 1, nodes: 1\n" + \
									"\t\tNone\n\t\tNone\n"
									),
	([[0,0],[1,1]], [0,0], "[1 1], axis: 0, nodes: 2\n" + \
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
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		assert tree.insert([0,0])

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
		assert tree.search([0,0])

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
		assert tree.delete([0,0])

def test_1NN():
	tree = KDTree.initialize([1,4])
	assert np.all(tree.nearest_neighbor(3) == np.asarray([[4,1]]))

def test_2NN():
	tree = KDTree.initialize([1,5,6])
	assert np.all(tree.nearest_neighbor(4, n=2) == np.asarray([[5,1],[6,2]]))

def test_KNN_mismatch():
	tree = KDTree.initialize([1,2])
	with pytest.raises(ValueError):
		assert tree.nearest_neighbor([0,0])

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

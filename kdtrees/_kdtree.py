"""K-D Tree"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

import ._utils as utils

class KDTree:
	"""
	A K-D Tree implemented as an AVL Tree.

	Parameters
	----------
	value : None or array-like, default=None
		Value at the KDTree node.

	k : int, default=0
		Dimensionality of the KDTree.

	axis : int, default=0
		Axis of discriminiation.

	Attributes
	----------
	left : KDTree
		Left child of the KDTree.

	right : KDTree
		Right child of the KDTree.

	height : int
		Height of the KDTree. Height is 0 if value is None.

	nodes : int
		Number of KDTree nodes, including itself if value is not None.
	"""
	def __init__(self, value=None, k=0, axis=0):
		self.value = value
		self.k = k
		self.axis = axis
		self.left = None
		self.right = None
		self.height = 0 if value is None else 1
		self.nodes = 0 if value is None else 1

	def visualize(self, depth=0):
		"""
		Prints a visual representation of the KDTree.

		Parameters
		----------
		depth : int, default=0
			Depth of the KDTree node. A depth of 0 implies the root.
		"""
		print('\t' * depth + str(self.value.mu) + ", axis: " + str(self.axis))
		if self.right:
			self.right.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")
		if self.left:
			self.left.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")

	@staticmethod
	def initialize(points, depth=0):
		"""
		Initialize a KDTree from a list of points.

		Parameters
		----------
		points : array-like
			List of points to build a KDTree where the last axis denotes the features

		depth : int, default=0
			Initial depth to generate the KDTree.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`
		"""
		points = np.asarray(points)
		if points.shape == () or points.shape[0] == 0:
			raise ValueError("Points needs to be a collection")
		axis = depth % (k + 1)
		points = sorted(points, key=lambda x: x[axis])
		median = len(points) // 2
		tree = KDTree(value=points[median], k=k, axis=axis, tol=tol)
		rh, rn, lh, ln = 0, 0, 0, 0
		if len(points[median+1:]) > 0:
			tree.right, rh, rn = KDTree.initialize(points[median+1:], depth=axis+1, tol=tol)
		if len(points[:median]) > 0:
			tree.left, lh, ln = KDTree.initialize(points[:median], depth=axis+1, tol=tol)
		tree.height += rh + lh
		tree.nodes += rn + ln
		return tree, tree.height, tree.nodes

	def insert(self, point):
		"""
		Insert a point into the KDTree.

		Parameters
		----------
		point : array-like or scalar
			The point to be inserted, where the last axis denotes the features.
		"""
		pass

	def search(self, point):
		"""
		Search the KDTree for a point.
		Returns the KDTree node if found, None otherwise.

		Parameters
		----------
		point : array-like or scalar
			The point being searched, where the last axis denotes the features.

		Returns
		-------
		tree : KDTree or None
			The KDTree node whose value matches the point.
			None if the point was not found in the tree.
		"""
		if self.k != utils.check_dimensionality(point):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if self.value is None:
			raise ValueError("KDTree is empty")
		elif self.value == point:
			return self
		elif point[self.axis] > self.value[self.axis]:
			if self.right is None:
				return None
			else:
				return self.right.search(point)
		else:
			if self.left is None:
				return None
			else:
				return self.left.search(point)

	def delete(self, point):
		"""
		Insert a point into the KDTree.

		Parameters
		----------
		point : array-like or scalar
			The point to be deleted, where the last axis denotes the features.
		"""
		pass

	def balance(self):
		"""
		Balance the KDTree.
		"""
		pass

	def nearest_neighbor(self, point, n=1, neighbors=None, distances=None):
		"""
		Determine the `n` nearest KDTree nodes to `point` and their distances.

		Parameters
		----------
		point : array-like or scalar
			The query point, where the last axis denotes the features.

		n : int, default=1
			The number of neighbors to search for.

		neighbors : list or None, default=None
			The list of `n` nearest neighbors.

		distances : list or None, default=None
			The list of distances corresponding to `neighbors`.

		Returns
		-------
		neighbors : list or None, default=None
			The list of `n` nearest neighbors, sorted based on proximity.

		distances : list or None, default=None
			The list of distances corresponding to `neighbors`.
		"""
		if self.k != utils.check_dimensionality(point):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if self.value is None:
			raise ValueError("KDTree is empty")
		if distances is None or neighbors is None:
			distances = [np.inf] * n
			neighbors = [None] * n
		distances, neighbors = np.asarray(distances), np.asarray(neighbors)
		dist = np.linalg.norm(point - self.value)
		idx = distances.searchsorted(dist)
		if idx < len(distances):
			distances = np.insert(distances, idx, dist)[:n]
			neighbors = np.insert(neighbors, idx, self.value)[:n]
		if point[self.axis] + distances[-1] >= self.value[self.axis]:
			neighbors, distances = self.right.nearest_neighbor(point, n=n, neighbors=neighbors, distances=distances)
		if point[self.axis] - distances[-1] < self.value[self.axis]:
			neighbors, distances = self.left.nearest_neighbor(point, n=n, neighbors=neighbors, distances=distances)
		return neighbours, distances

	def proximal_neighbor(self, point, d=0, neighbors=None, distances=None):
		"""
		Determine the KDTree nodes that are within `d` distance
		to `point` and their distances.

		Parameters
		----------
		point : array-like or scalar
			The query point, where the last axis denotes the features.

		d : int, default=0
			The maximum acceptable distance for neighbors.

		neighbors : list or None, default=None
			The list of `n` nearest neighbors.

		distances : list or None, default=None
			The list of distances corresponding to `neighbors`.

		Returns
		-------
		neighbors : list or None, default=None
			The list of `n` nearest neighbors, sorted based on proximity.

		distances : list or None, default=None
			The list of distances corresponding to `neighbors`.
		"""
		if self.k != utils.check_dimensionality(point):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if d == 0:
			return neighbors, distances
		if self.value is None:
			raise ValueError("KDTree is empty")
		if distances is None or neighbors is None:
			distances = []
			neighbors = []
		distances, neighbors = np.asarray(distances), np.asarray(neighbors, dtype=Core)
		dist = np.linalg.norm(point - self.value)
		if dist <= d and point != self.value:
			idx = distances.searchsorted(dist)
			distances = np.insert(distances, idx, dist)
			neighbors = np.insert(neighbors, idx, self.value)
		if self.right and point[self.axis] + d >= self.value[self.axis]:
			neighbors, distances = self.right.proximal_neighbor(point, d=d, neighbors=neighbors, distances=distances)
		if self.left and point[self.axis] - d < self.value[self.axis]:
			neighbors, distances = self.left.proximal_neighbor(point, d=d, neighbors=neighbors, distances=distances)
		return neighbors, distances

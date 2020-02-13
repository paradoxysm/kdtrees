# coding=utf-8

"""K-D Tree"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

from . import _utils as utils
from ._kdtree_type import KDTreeType

class KDTree:
	"""
	A K-D Tree in a pseudo-balanced Tree.
	In addition to the K-D Tree invariant, the KDTree maintains
	a secondary invariant such that any node is the
	median ± dimensionality of all nodes contained in the KDTree.

	Parameters
	----------
	value : array-like
		Value at the KDTree node.

	k : int, default=0
		Dimensionality of the KDTree.

	axis : int, default=0
		Axis of discriminiation.

	accept : KDTreeType or None
		Override and allow custom types to be accepted.

	Attributes
	----------
	left : KDTree
		Left child of the KDTree.

	right : KDTree
		Right child of the KDTree.

	nodes : int
		Number of nodes in the KDTree, including itself.

	accept : KDTreeType or None
		Override and allow a custom type to be accepted.
	"""
	def __init__(self, value, k=1, axis=0, accept=None):
		self.value = value
		self.k = k
		self.axis = axis
		self.left = None
		self.right = None
		self.nodes = 1
		self.accept = accept

	def visualize(self, depth=0):
		"""
		Prints a visual representation of the KDTree.

		Parameters
		----------
		depth : int, default=0
			Depth of the KDTree node. A depth of 0 implies the root.
		"""
		print('\t' * depth + str(self.value) + ", axis: " + str(self.axis) + ", nodes: " + str(self.nodes))
		if self.right:
			self.right.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")
		if self.left:
			self.left.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")

	@staticmethod
	def initialize(points, k=None, init_axis=0, accept=None):
		"""
		Initialize a KDTree from a list of points by presorting `points`
		by each of the axes of discrimination. Initialization attempts
		balancing by selecting the median along each axis of discrimination
		as the root.

		Parameters
		----------
		points : array-like, shape (n_points, *)
			List of points to build a KDTree where the last axis denotes the features.
			If `accept` is a KDTreeType, list can contain this type.

		k : int or None, default=None
			Dimensionality of the points. If None, `initialize` will self-detect.

		init_axis : int, default=0
			Initial axis to generate the KDTree.

		accept : KDTreeType or None
			Override and allow a custom type to be accepted.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`.
		"""
		if accept is not None and not issubclass(accept, KDTreeType):
			raise ValueError("Accept must be a subclass of KDTreeType")
		if k is None:
			k = utils.check_dimensionality(*points, accept=accept)
		sorted_points = []
		for axis in range(k):
			sorted_points.append(sorted(points, key=lambda x: x[axis]))
		sorted_points = np.asarray(sorted_points)
		return KDTree._initialize_recursive(sorted_points, k, init_axis, accept)

	@staticmethod
	def _initialize_recursive(sorted_points, k, axis, accept):
		"""
		Internal recursive initialization based on an array of points
		presorted in all axes.

		This function should not be called externally. Use `initialize`
		instead.

		Parameters
		----------
		sorted_points : list
			List of ndarrays of points (KDTreeType if `accept` is used),
			each sorted on each of the axes of discrimination.

		k : int
			Dimensionality of the points.

		axis : int
			Axis of discrimination.

		accept : KDTreeType or None
			Override and allow a custom type to be accepted.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`
		"""
		median = len(sorted_points[axis]) // 2
		tree = KDTree(sorted_points[axis][median], k=k, axis=axis, accept=accept)
		sorted_right_points = []
		sorted_left_points = []
		right_points = sorted_points[axis][median+1:]
		left_points = sorted_points[axis][:median]
		for points in sorted_points:
			if accept:
				right_mask = np.isin(points, right_points)
				left_mask = np.isin(points, left_points)
			else:
				right_dim_masks = [np.isin(points[:,x], right_points[:,x]) for x in range(k)]
				right_mask = np.all(np.stack(right_dim_masks, axis=-1), axis=-1)
				left_dim_masks = [np.isin(points[:,x], left_points[:,x]) for x in range(k)]
				left_mask = np.all(np.stack(left_dim_masks, axis=-1), axis=-1)
			sorted_right_points.append(points[right_mask])
			sorted_left_points.append(points[left_mask])
		sorted_right_points = np.asarray(sorted_right_points)
		sorted_left_points = np.asarray(sorted_left_points)
		axis = axis + 1 if axis + 1 < k else 0
		if len(sorted_points[axis][median+1:]) > 0:
			tree.right = KDTree._initialize_recursive(sorted_right_points, k, axis, accept)
		if len(sorted_points[axis][:median]) > 0:
			tree.left = KDTree._initialize_recursive(sorted_left_points, k, axis, accept)
		tree._recalculate_nodes()
		return tree

	def _recalculate_nodes(self):
		"""
		Recalculate the number of nodes of the KDTree,
		assuming that the KDTree's children are correctly
		calculated.
		"""
		nodes = 0
		if self.right:
			nodes += self.right.nodes
		if self.left:
			nodes += self.left.nodes
		self.nodes = nodes + 1

	def insert(self, point):
		"""
		Insert a point into the KDTree.

		Parameters
		----------
		point : array-like or object
			The point (KDTreeType if `accept` is used) to be inserted,
			where the last axis denotes the features.

		Returns
		-------
		tree : KDTree
			The root of the KDTree with `point` inserted.
		"""
		if self.accept is None:
			point = np.asarray(point)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		axis = self.axis + 1 if self.axis + 1 < self.k else 0
		if np.all(self.value == point):
			return self
		elif point[self.axis] >= self.value[self.axis]:
			if self.right is None:
				self.right = KDTree(value=point, k=self.k, axis=axis, accept=self.accept)
			else:
				self.right = self.right.insert(point)
		elif point[self.axis] < self.value[self.axis]:
			if self.left is None:
				self.left = KDTree(value=point, k=self.k, axis=axis, accept=self.accept)
			else:
				self.left = self.left.insert(point)
		self._recalculate_nodes()
		return self.balance()

	def search(self, point):
		"""
		Search the KDTree for a point.
		Returns the KDTree node if found, None otherwise.

		Parameters
		----------
		point : array-like or scalar
			The point (KDTreeType if `accept` is used) being searched,
			where the last axis denotes the features.

		Returns
		-------
		tree : KDTree or None
			The KDTree node whose value matches the point.
			None if the point was not found in the tree.
		"""
		if self.accept is None:
			point = np.asarray(point)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		elif np.all(self.value == point):
			return self
		elif point[self.axis] >= self.value[self.axis]:
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
		Delete a point from the KDTree and return the new
		KDTree. Returns the same tree if the point was not found.

		Parameters
		----------
		point : array-like or scalar
			The point to be deleted, where the last axis denotes the features.

		Returns
		-------
		tree : KDTree
			The root of the KDTree with `point` removed.
		"""
		if self.accept is None:
			point = np.asarray(point)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if np.all(self.value == point):
			values = self.collect()
			if len(values) > 1:
				values.remove(point)
				new_tree = KDTree.initialize(values, k=self.k, init_axis=self.axis, accept=self.accept)
				return new_tree
			return None
		elif point[self.axis] >= self.value[self.axis]:
			if self.right is None:
				return self
			else:
				new_tree = self.right.delete(point)
				self.right = new_tree
				self._recalculate_nodes()
				return self.balance()
		else:
			if self.left is None:
				return self
			else:
				new_tree = self.left.delete(point)
				self.left = new_tree
				self._recalculate_nodes()
				return self.balance()

	def collect(self):
		"""
		Collect all values in the KDTree as a list,
		ordered in a depth-first manner.

		Returns
		-------
		values : list
			A list of all the values in the KDTree.
		"""
		values = []
		values.append(self.value)
		if self.right is not None:
			values += self.right.collect()
		if self.left is not None:
			values += self.left.collect()
		return values

	def balance(self):
		"""
		Balance the KDTree if the secondary invariant is not satisfied.

		Returns
		-------
		tree : KDTree
			The root of the newly pseudo-balanced KDTree
		"""
		if not self.invariant():
			values = self.collect()
			return KDTree.initialize(values, k=self.k, init_axis=self.axis, accept=self.accept)
		return self

	def invariant(self):
		"""
		Verify that the KDTree satisfies the secondary invariant.

		Returns
		-------
		valid : bool
			True if the KDTree satisfies the secondary invariant.
		"""
		ln, rn = 0, 0
		if self.left:
			ln = self.left.nodes
		if self.right:
			rn = self.right.nodes
		return np.abs(ln - rn) <= self.k

	def nearest_neighbor(self, point, n=1, neighbors=[]):
		"""
		Determine the `n` nearest KDTree nodes to `point` and their distances.

		Parameters
		----------
		point : array-like or scalar
			The query point, where the last axis denotes the features.

		n : int, default=1
			The number of neighbors to search for.

		neighbors : list, default=[]
			The list of `n` tuples, referring to `n` nearest neighbors,
			sorted based on proximity. The first value in the tuple is the
			point, while the second is the distance to `point`.

		Returns
		-------
		neighbors : list, shape (n_neighbors, 2)
			The list of `n` tuples, referring to `n` nearest neighbors.
		"""
		if self.accept is None:
			point = np.asarray(point)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if len(neighbors) != n:
			neighbors = [(None, np.inf)] * n
		neighbors = np.asarray(neighbors)
		dist = utils.distance(point, self.value, accept=self.accept)
		idx = neighbors[:,1].searchsorted(dist)
		if idx < len(neighbors):
			neighbors = np.insert(neighbors, idx, np.asarray([self.value, dist]), axis=0)[:n]
		if point[self.axis] + neighbors[-1,1] >= self.value[self.axis] and self.right:
			neighbors = self.right.nearest_neighbor(point, n=n, neighbors=neighbors)
		if point[self.axis] - neighbors[-1,1] < self.value[self.axis] and self.left:
			neighbors = self.left.nearest_neighbor(point, n=n, neighbors=neighbors)
		return neighbors

	def proximal_neighbor(self, point, d=0, neighbors=[]):
		"""
		Determine the KDTree nodes that are within `d` distance
		to `point` and their distances.

		Parameters
		----------
		point : array-like or scalar
			The query point, where the last axis denotes the features.

		d : int, default=0
			The maximum acceptable distance for neighbors.

		neighbors : list, default=[]
			The list of `n` tuples, referring to proximal neighbors within
			`d` distance from `point`, sorted based on proximity.
			The first value in the tuple is the point, while the
			second is the distance to `point`.

		Returns
		-------
		neighbors : list, shape (n_neighbors, 2)
			The list of `n` tuples, referring to proximal neighbors within
			`d` distance from `point`.
		"""
		if self.accept is None:
			point = np.asarray(point)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if d == 0:
			exists = self.search(point)
			return [(exists, 0.0)] if exists else []
		neighbors = np.asarray(neighbors)
		dist = utils.distance(point, self.value, accept=self.accept)
		if dist <= d and point != self.value:
			if len(neighbors) > 0:
				idx = neighbors[:,1].searchsorted(dist)
				neighbors = np.insert(neighbors, idx, np.asarray([self.value, dist]), axis=0)
			else:
				neighbors = np.asarray([[self.value, dist]])
		if self.right and point[self.axis] + d >= self.value[self.axis]:
			neighbors = self.right.proximal_neighbor(point, d=d, neighbors=neighbors)
		if self.left and point[self.axis] - d < self.value[self.axis]:
			neighbors = self.left.proximal_neighbor(point, d=d, neighbors=neighbors)
		return neighbors

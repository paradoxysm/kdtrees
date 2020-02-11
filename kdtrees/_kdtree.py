# coding=utf-8

"""K-D Tree"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

from . import _utils as utils
from .kdtree_type import KDTreeType

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

	Attributes
	----------
	left : KDTree
		Left child of the KDTree.

	right : KDTree
		Right child of the KDTree.

	height : int
		Height of the KDTree.

	nodes : int
		Number of nodes in the KDTree, including itself.
	"""
	def __init__(self, value, k=1, axis=0, accept=None):
		self.value = value
		self.k = k
		self.axis = axis
		self.left = None
		self.right = None
		self.height = 1
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
		print('\t' * depth + str(self.value) + ", axis: " + str(self.axis) + ", height: " + str(self.height) + ", nodes: " + str(self.nodes))
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
			List of points to build a KDTree where the last axis denotes the features

		k : int or None, default=None
			Dimensionality of the points. If None, `initialize` will self-detect.

		init_axis : int, default=0
			Initial axis to generate the KDTree.

		accept : KDTreeType or None
			Override and allow custom types to be accepted.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`
		"""
		if accept is not None and not isinstance(accept, KDTreeType):
			raise ValueError("Accept must be a subclass of KDTreeType")
		points = utils.format_array(points, l=True, accept=accept)
		if k is None:
			k = utils.check_dimensionality(points, l=True, accept=accept)
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
			List of lists of points, each sorted on
			each of the axes of discrimination.

		k : int
			Dimensionality of the points.

		axis : int
			Axis of discrimination.

		accept : KDTreeType or None
			Override and allow custom types to be accepted.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`
		"""
		median = len(sorted_points[axis]) // 2
		tree = KDTree(sorted_points[axis][median], k=k, axis=axis, accept=accept)
		sorted_right_points = []
		sorted_left_points = []
		for points in sorted_points:
			right_mask = np.all(np.isin(points, sorted_points[axis][median+1:]), axis=-1)
			right_points = points[np.where(right_mask)]
			sorted_right_points.append(right_points)
			left_mask = np.all(np.isin(points, sorted_points[axis][:median]), axis=-1)
			left_points = points[np.where(left_mask)]
			sorted_right_points.append(left_points)
		sorted_right_points = np.asarray(sorted_right_points)
		sorted_left_points = np.asarray(sorted_left_points)
		axis = axis + 1 if axis + 1 < k else 0
		if len(sorted_points[axis][median+1:]) > 0:
			tree.right = KDTree._initialize_recursive(sorted_right_points, k, axis, accept)
		if len(sorted_points[axis][:median]) > 0:
			tree.left = KDTree._initialize_recursive(sorted_left_points, k, axis, accept)
		tree._recalculate_height_nodes()
		return tree

	def _recalculate_height_nodes(self):
		"""
		Recalculate the height and nodes of the KDTree,
		assuming that the KDTree's children are correctly
		calculated.
		"""
		heights = []
		nodes = 0
		if self.right:
			heights.append(self.right.height)
			nodes += self.right.nodes
		if self.left:
			heights.append(self.left.height)
			nodes += self.left.nodes
		if len(heights) > 0:
			self.height = np.max(heights) + 1
		self.nodes = nodes + 1

	def insert(self, point):
		"""
		Insert a point into the KDTree.

		Parameters
		----------
		point : array-like or scalar
			The point to be inserted, where the last axis denotes the features.

		Returns
		-------
		tree : KDTree
			The root of the KDTree with `point` inserted.
		"""
		point = utils.format_array(point, accept=self.accept)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		axis = self.axis + 1 if self.axis + 1 < self.k else 0
		if point[self.axis] > self.value[self.axis]:
			if self.right is None:
				self.right = KDTree(value=point, k=self.k, axis=axis, accept=self.accept)
			else:
				self.right.insert(point)
		elif point[self.axis] < self.value[self.axis]:
			if self.left is None:
				self.left = KDTree(value=point, k=self.k, axis=axis, accept=self.accept)
			else:
				self.left.insert(point)
		self._recalculate_height_nodes()
		return self.balance()

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
		point = utils.format_array(point, accept=self.accept)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
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
		point = utils.format_array(point, accept=self.accept)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDCoreTree")
		if self.value == point:
			values = self.collect()
			if len(values) > 1:
				values.remove(point)
				new_tree = KDTree.initialize(values, k=self.k, init_axis=self.axis, accept=self.accept)
				return new_tree
			return None
		elif point[self.axis] > self.value[self.axis]:
			if self.right is None:
				return self
			else:
				new_tree = self.right.delete(point)
				self.right = new_tree
				self.height = np.max([self.height, self.right.height + 1])
				ln = self.left.nodes if self.left else 0
				self.nodes = ln + self.right.nodes + 1
				self.balance()
				return self
		else:
			if self.left is None:
				return self
			else:
				new_tree = self.left.delete(point)
				self.left = new_tree
				self.height = np.max([self.height, self.left.height + 1])
				rn = self.right.nodes if self.right else 0
				self.nodes = rn + self.left.nodes + 1
				self.balance()
				return self

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
		if self.value is not None:
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
			KDTree.initialize(values, k=self.k, init_axis=self.axis, accept=self.accept)
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
		point = utils.format_array(point, accept=self.accept)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if len(neighbors) != n:
			neighbors = [(None, np.inf)] * n
		neighbors = np.asarray(neighbors)
		dist = np.linalg.norm(point - self.value)
		idx = neighbors[:][1].searchsorted(dist)
		if idx < len(distances):
			neighbors = np.insert(neighbors, idx, (self.value, dist))[:n]
		if point[self.axis] + distances[-1] >= self.value[self.axis]:
			neighbors = self.right.nearest_neighbor(point, n=n, neighbors=neighbors)
		if point[self.axis] - distances[-1] < self.value[self.axis]:
			neighbors = self.left.nearest_neighbor(point, n=n, neighbors=neighbors)
		return neighbours

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
		point = utils.format_array(point, accept=self.accept)
		if self.k != utils.check_dimensionality(point, accept=self.accept):
			raise ValueError("Point must be same dimensionality as the KDTree")
		if d == 0:
			exists = self.search(point)
			return [(exists, 0.0)] if exists else []
		neighbors = np.asarray(neighbors)
		dist = np.linalg.norm(point - self.value)
		if dist <= d and point != self.value:
			idx = neighbors[:][1].searchsorted(dist)
			neighbors = np.insert(neighbors, idx, (self.value, dist))
		if self.right and point[self.axis] + d >= self.value[self.axis]:
			neighbors = self.right.proximal_neighbor(point, d=d, neighbors=neighbors)
		if self.left and point[self.axis] - d < self.value[self.axis]:
			neighbors = self.left.proximal_neighbor(point, d=d, neighbors=neighbors)
		return neighbors

# coding=utf-8

"""K-D Tree"""

# Authors: Jeffrey Wang
# License: BSD 3 clause

import numpy as np

from . import _utils as utils

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
	def __init__(self, value, k=1, axis=0):
		self.value = value
		self.k = k
		self.axis = axis
		self.left = None
		self.right = None
		self.height = 1
		self.nodes = 1

	def visualize(self, depth=0):
		"""
		Prints a visual representation of the KDTree.

		Parameters
		----------
		depth : int, default=0
			Depth of the KDTree node. A depth of 0 implies the root.
		"""
		print('\t' * depth + str(self.value) + ", axis: " + str(self.axis))
		if self.right:
			self.right.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")
		if self.left:
			self.left.visualize(depth=depth+1)
		else:
			print('\t' * (depth+1) + "None")

	@staticmethod
	def initialize(points, k=1, init_axis=0):
		"""
		Initialize a KDTree from a list of points.

		Parameters
		----------
		points : array-like, shape (n_points, *)
			List of points to build a KDTree where the last axis denotes the features

		init_axis : int, default=0
			Initial axis to generate the KDTree.

		Returns
		-------
		tree : KDTree
			The root of the KDTree built from `points`
		"""
		points = utils.format_array(points, list=True)
		tree = KDTree(points[0], k=k, axis=init_axis)
		for p in points[1:]:
			tree.insert(p)
		return tree

	def insert(self, point):
		"""
		Insert a point into the KDTree.

		Parameters
		----------
		point : array-like or scalar
			The point to be inserted, where the last axis denotes the features.
		"""
		point = utils.format_array(point)
		if self.k != utils.check_dimensionality(point):
			raise ValueError("Point must be same dimensionality as the KDTree")
		axis = self.axis + 1 if self.axis < self.k else 0
		if point[self.axis] >= self.value[self.axis]:
			if self.right is None:
				self.right = KDTree(value=point, k=self.k, axis=axis)
			else:
				self.right.insert(point)
		else:
			if self.left is None:
				self.left = KDTree(value=point, k=self.k, axis=axis)
			else:
				self.left.insert(point)
		heights = []
		if self.right:
			heights.append(self.right.height)
		if self.left:
			heights.append(self.left.height)
		self.height = np.max(heights) + 1
		self.nodes += 1
		self.balance()

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
		point = utils.format_array(point)
		if self.k != utils.check_dimensionality(point):
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
		point = utils.format_array(point)
		if self.k != utils.checkDimensionality(point):
			raise ValueError("Point must be same dimensionality as the KDCoreTree")
		if self.value == point:
			values = self.collect()
			if len(values) > 1:
				values.remove(point)
				new_tree = KDTree.initialize(values, k=self.k, init_axis=self.axis)
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
		"""
		if not self.invariant():
			right_values = self.right.collect()
			left_values = self.left.collect()
			self.right = initialize(right_values, k=self.right.k, init_axis=self.right.axis)
			self.left = initialize(left_values, k=self.left.k, init_axis=self.left.axis)

	def invariant(self):
		"""
		Verify that the KDTree satisfies the secondary invariant.

		Returns
		-------
		valid : bool
			True if the KDTree satisfies the secondary invariant.
		"""
		return np.abs(self.left.nodes - self.right.nodes) <= self.k

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
		point = utils.format_array(point)
		if self.k != utils.check_dimensionality(point):
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
		point = utils.format_array(point)
		if self.k != utils.check_dimensionality(point):
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

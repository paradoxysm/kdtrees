# Documentation

All documentation for kdtrees is located here!

[**pydoc**](https://github.com/paradoxysm/kdtrees/tree/master/doc/pydoc) : Documentation regarding python classes and functions.

# KDTrees Overview

kdtrees implements a K-D Tree in a pseudo-balanced tree. A pseudo-balanced tree, in kdtrees, is defined by an invariant where all nodes must be the median ± dimensionality of subsidiary nodes along a specific axis.

kdtrees allows for construction, visualization, insertion, deletion, searching, aggregating, and balancing. In addition, k-nearest neighbors as well as neighbors-within-distance have been implemented. Insuring proper types and dimensionality is also integrated.

kdtrees supports all builtin types and numpy types. However, additional support may be added by the user with the `accept` clause. Additional types must have methods to compare and be iterable-like. An abstract base class, `kdtree_type` has been provided which you may extend to ensure compatibility with additional accept types.

**Construction**

kdtrees constructs a K-D Tree from a given list of points in a manner such that a pseudo-balanced tree is produced (i.e. A tree that satisfies the secondary invariant). It does this by presorting the list of points along each of the available axes. At each recursive entry, the median point along an alternating axis of discrimination is chosen as the root of the sub-tree. This produces a pseudo-balanced tree in *O(nlogn)*. For details see [`initialize`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#initialize).

**Visualization**

kdtrees can be visualized in a preorder traversal. This is one such example:

```python
[0 2 0], axis: 0, height: 2, nodes: 3
	[1 1 1], axis: 1, height: 1, nodes: 1
		None
		None
	[0 0 0], axis: 1, height: 1, nodes: 1
		None
		None
```
For details see [`visualize`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#visualize).

**Insertion and Deletion**

kdtrees supports insertion and deletion in preorder traversal. The tree automatically balances as needed. It runs in *O(n)*. For details see [`insert`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#insert) and [`delete`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#delete).

**Searching**

kdtrees supports searches in preorder traversal, running in *O(logn)*. kdtrees searches and produces the KDTree that holds the queried value. Finding none, it will return None. For details see [`search`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#search).

**Aggregating**

kdtrees can aggregate all subsidiary nodes, produced as a list in preorder, running in *O(logn)*. For details see [`collect`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#collect).

**Balancing**

kdtrees balances in a pseudo-balanced manner, satisfying the secondary invariant. If the KDTree does not satisfy this invariant, it is reconstructed anew and thus returned to pseudo-balance. For details see [`balance`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#balance).

**K-Nearest Neighbors**

kdtrees supports finding k-nearest neighbors, finding a specified number of (1 if not specified) of nodes that are closest to the query point. Ties are broken based on the preorder traversal (i.e. left-most nodes are prioritized). It produces a list of tuples, containing the value of the node and its corresponding distance to the query point. For details see [`nearest_neighbor`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#nearest_neighbor).

**Neighbors-within-Distance**

kdtrees is also able to find all neighbors within a specified distance (0 if not specified). This produces a list of tuples, containing the value of the node and its corresponding distance to the query point. For details see [`proximal_neighbor`](https://github.com/paradoxysm/kdtrees/blob/master/doc/pydoc/doc_kdtree.md#proximal_neighbor).

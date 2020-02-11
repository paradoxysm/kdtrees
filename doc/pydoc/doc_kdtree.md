# kdtrees._kdtree
K-D Tree
## KDTree
```python
KDTree(self, value, k=1, axis=0, accept=None)
```

A K-D Tree in a pseudo-balanced Tree.
In addition to the K-D Tree invariant, the KDTree maintains
a secondary invariant such that any node is the
median ± dimensionality of all nodes contained in the KDTree.

**Parameters**
```python
value : array-like
 Value at the KDTree node.

k : int, default=0
 Dimensionality of the KDTree.

axis : int, default=0
 Axis of discriminiation.
```

**Attributes**

In addition to all parameters:
```python
left : KDTree
 Left child of the KDTree.

right : KDTree
 Right child of the KDTree.

height : int
 Height of the KDTree.

nodes : int
 Number of nodes in the KDTree, including itself.
```

## initialize
```python
KDTree.initialize(points, k=None, init_axis=0, accept=None)
```

Initialize a KDTree from a list of points by presorting `points`
by each of the axes of discrimination. Initialization attempts
balancing by selecting the median along each axis of discrimination
as the root.

**Parameters**
```python
points : array-like, shape (n_points, *)
 List of points to build a KDTree where the last axis denotes the features

k : int or None, default=None
 Dimensionality of the points. If None, `initialize` will self-detect.

init_axis : int, default=0
 Initial axis to generate the KDTree.

accept : KDTreeType or None
 Override and allow custom types to be accepted.
```

**Returns**
```python
tree : KDTree
 The root of the KDTree built from `points`
```

## visualize
```python
KDTree.visualize(self, depth=0)
```

Prints a visual representation of the KDTree.

**Parameters**
```python
depth : int, default=0
 Depth of the KDTree node. A depth of 0 implies the root.
```

## insert
```python
KDTree.insert(self, point)
```

Insert a point into the KDTree.

**Parameters**
```python
point : array-like or scalar
 The point to be inserted, where the last axis denotes the features.
```

**Returns**
```python
tree : KDTree
 The root of the KDTree with `point` inserted.
```

## search
```python
KDTree.search(self, point)
```

Search the KDTree for a point.
Returns the KDTree node if found, None otherwise.

**Parameters**
```python
point : array-like or scalar
 The point being searched, where the last axis denotes the features.
```

**Returns**
```python
tree : KDTree or None
 The KDTree node whose value matches the point.
 None if the point was not found in the tree.
```

## delete
```python
KDTree.delete(self, point)
```

Delete a point from the KDTree and return the new
KDTree. Returns the same tree if the point was not found.

**Parameters**
```python
point : array-like or scalar
 The point to be deleted, where the last axis denotes the features.
```

**Returns**
```python
tree : KDTree
 The root of the KDTree with `point` removed.
```

## collect
```python
KDTree.collect(self)
```

Collect all values in the KDTree as a list,
ordered in a depth-first manner.

**Returns**
```python
values : list
 A list of all the values in the KDTree.
```

## balance
```python
KDTree.balance(self)
```

Balance the KDTree if the secondary invariant is not satisfied.

**Returns**
```python
tree : KDTree
 The root of the newly pseudo-balanced KDTree
```

## invariant
```python
KDTree.invariant(self)
```

Verify that the KDTree satisfies the secondary invariant.

**Returns**
```python
valid : bool
 True if the KDTree satisfies the secondary invariant.
```

## nearest_neighbor
```python
KDTree.nearest_neighbor(self, point, n=1, neighbors=[])
```

Determine the `n` nearest KDTree nodes to `point` and their distances.

**Parameters**
```python
point : array-like or scalar
 The query point, where the last axis denotes the features.

n : int, default=1
 The number of neighbors to search for.

neighbors : list, default=[]
 The list of `n` tuples, referring to `n` nearest neighbors,
 sorted based on proximity. The first value in the tuple is the
 point, while the second is the distance to `point`.
```

**Returns**
```python
neighbors : list, shape (n_neighbors, 2)
 The list of `n` tuples, referring to `n` nearest neighbors.
```

## proximal_neighbor
```python
KDTree.proximal_neighbor(self, point, d=0, neighbors=[])
```

Determine the KDTree nodes that are within `d` distance
to `point` and their distances.

**Parameters**
```python
point : array-like or scalar
 The query point, where the last axis denotes the features.

d : int, default=0
 The maximum acceptable distance for neighbors.

neighbors : list, default=[]
 The list of `n` tuples, referring to proximal neighbors within
 `d` distance from `point`, sorted based on proximity.
 The first value in the tuple is the point, while the
 second is the distance to `point`.
```

**Returns**
```python
neighbors : list, shape (n_neighbors, 2)
 The list of `n` tuples, referring to proximal neighbors within
 `d` distance from `point`.
```

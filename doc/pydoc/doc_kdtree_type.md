# kdtrees._kdtree_type
Abstract base super class for acceptable type overrides
## KDTreeType
```python
KDTreeType(self, dim)
```

An abstract base super class (interface) for creating custom
types that kdtrees can accept. Any custom type must extend
KDTreeType to be acceptable. Based on the purpose of a K-D Tree,
KDTreeTypes must be comparable, indexable, and iterable.

**Parameters**
```
dim : int
	Dimensionality of this `KDTreeType`.
```

## __eq__
```python
KDTreeType == other
KDTreeType.__eq__(other)
```

Determine if `other` is equivalent to this `KDTreeType`.

**Parameters**
```
other : object
	The object in question.
```

**Returns**
```
eq : bool
	True if `other` is equivalent to this `KDTreeType`
```

## __ne__
```python
KDTreeType != other
KDTreeType.__ne__(other)
```

Determine if `other` is not equivalent to this `KDTreeType`.

**Parameters**
```
other : object
	The object in question.
```

**Returns**
```
ne : bool
	True if `other` is not equivalent to this `KDTreeType`
```

## __lt__
```python
KDTreeType < KDTreeType
KDTreeType.__lt__(other)
```
Return if this `KDTreeType` is 'less' than `other`.

**Parameters**
```
other : object
	The object in question.
```

**Returns**
```
lt : bool
	True if this `KDTreeType` is 'less' than `other`.
```

## __getitem__
```python
KDTreeType[i]
KDTreeType.__getitem__(i)
```
Return the 'item' and the 'index', `key`, of the KDTreeType.
This needs to be defined based on the custom implementation.

**Returns**
```
item : object
	The 'item' and the 'index', `key`, of the KDTreeType.
```

## distance
```python
KDTreeType.distance(KDTreeType)
```
Calculate the 'distance' between this `KDTreeType` and `other`.

**Parameters**
```
other : object
	The object in question.
```

**Returns**
```
dist : float
	'Distance' between this `KDTreeType` and `other`.
```

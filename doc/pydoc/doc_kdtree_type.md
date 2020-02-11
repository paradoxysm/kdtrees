# kdtree_type
Abstract base super class for acceptable type overrides
## KDTreeType
```python
KDTreeType(self)
```

An abstract base super class (interface) for creating custom
types that kdtrees can accept. Any custom type must extend
KDTreeType to be acceptable. Based on the purpose of a K-D Tree,
KDTreeTypes must be comparable, indexable, and iterable.

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

## __len__
```python
len(KDTreeType)
KDTreeType.__len__()
```
Return the 'length' of the KDTreeType. This needs to be
defined based on the custom implementation.

**Returns**
```
length : int
	The 'length' of this `KDTreeType`.
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

## __iter__
```python
for item in KDTreeType:
	print(item)
```
Return the next 'item' of the KDTreeType.
This needs to be defined based on the custom implementation.

**Yields**
```
item : object
	The next 'item' of the KDTreeType.
```

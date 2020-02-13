# kdtrees._utils
Utilities for Various Tasks

## check_dimensionality
```python
check_dimensionality(*args, accept=None)
```

Check that all arguments have the same dimensionality.
Return that dimensionality.

If `accept` is an object that contains a `dim`
attribute, use that instead.

**Parameters**
```
*args : tuple, default=()
	Tuple of ndarray objects where the last axis denotes the features.
	If `accept` is an object, it can be this type.

accept : None or object, default=None
	Accept override type. Check the `dim` attribute of this object.
```

**Returns**
```
dim : int
 The dimensionality of all given arguments.
```

## distance
```python
distance(obj1, obj2, accept=None)
```
Calculate the distance between `obj1` and `obj2`,
using norm.

If `accept` is an object that contains a `distance`
function, use that instead. Uses `obj1.distance(obj2)`.

**Parameters**
```
obj1 : array-like or scalar or object
	array-like or scalar where the last axis denotes the features.
	If `accept` is an object, it can be this type.

obj2 : array-like or scalar or object
	array-like or scalar where the last axis denotes the features.
	If `accept` is an object, it can be this type.

accept : None or object, default=None
	Accept override type. Use the `distance` function of this type.
```

**Returns**
```
distance : int
	The distance between `obj1` and `obj2`.
```

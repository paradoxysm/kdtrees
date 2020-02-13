# kdtrees._utils
Utilities for Various Tasks
## format_array
```python
format_array(arr, l=False, accept=None)
```

Format the given array or scalar into a numpy ndarray
such that the last axis denotes the features.
If the argument given is a scalar, wrap into a list first.

**Parameters**
```
arr : array-like or scalar
 Array-like object or scalar to convert into ndarray.

l : bool
 `l` should be set to True if `arr` is semantically a list of items.

accept : None or object, default=None
  Accept override type. Allow `arr` to be this type
```

**Returns**
```
ndarr : ndarray
 Formatted ndarray where the last axis denotes the features.
```

## check_dimensionality
```python
check_dimensionality(*args, l=False, accept=None)
```

Check that all arguments have the same dimensionality.
Return that dimensionality.

If `accept` is an object that contains a `dim`
attribute, use that instead.

**Parameters**
```
*args : tuple, default=()
 Tuple of array-like objects where the last axis denotes the features.

l : bool
 `l` should be set to True if `args` is a tuple where every
 item is semantically a list of items.

accept : None or object, default=None
  Accept override type. Check the `dim` attribute of this object
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
obj1 : array-like or object, default=()
	Tuple of array-like objects where the last axis denotes the features.

l : bool
	`l` should be set to True if `args` is a tuple where every
	item is semantically a list of items.

accept : None or object, default=None
	Accept override type. Check the dimensionality attribute of this object
```

**Returns**
```
dim : int
	The dimensionality of all given arguments.
```

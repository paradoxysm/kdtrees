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

**Parameters**
```
*args : tuple, default=()
 Tuple of array-like objects where the last axis denotes the features.

l : bool
 `l` should be set to True if `args` is a tuple where every
 item is semantically a list of items.
```

**Returns**
```
dim : int
 The dimensionality of all given arguments.
```

# kdtrees
**Python implementation of a K-D Tree as a pseudo-balanced Tree**

## Overview

K-Dimensional Tree is a space-partitioning data structure, efficiently organizing points in k-dimensional space.

This K-D Tree implementation allows for construction, modification and searching of a K-D Tree. It also maintains the tree in a pseudo-balanced manner through a secondary invariant where every node is the median ± dimensionality of subsidiary nodes along a specific axis.

More details regarding this implementation can be found [here](docs)

## Installation

### Dependencies

kdtrees requires:
- numpy >= 1.18.0
 
kdtrees is tested and supported on Python 3.5 and Python 3.6. Usage on other versions of Python is not guaranteed to work as intended.
 
### User Installation
 
kdtrees can be easily installed using ```pip```
 
```
pip install kdtrees
```
 
## Changelog
 
See the [changelog](CHANGES.md) for a history of notable changes to kdtrees.

## Development

kdtrees is fully implemented for basic functionality. However, it may not have every utility function or have the most optimized algorithms. We welcome new contributors of all experience lelevels to help grow and improve kdtrees. Guides on development, testing, and contribution are in the works!

## Help and Support

### Documentation

Documentation for kdtrees can be found [here](docs)

### Issues and Questions

Issues and Questions should be posed to the issue tracker [here](https://github.com/paradoxysm/kdtrees/issues)

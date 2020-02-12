# kdtrees
**Python implementation of a K-D Tree as a pseudo-balanced Tree**

[![Build Status](https://travis-ci.com/paradoxysm/kdtrees.svg?branch=master)](https://travis-ci.com/paradoxysm/kdtrees)
[![codecov](https://codecov.io/gh/paradoxysm/kdtrees/branch/master/graph/badge.svg)](https://codecov.io/gh/paradoxysm/kdtrees)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kdtrees)
[![PyPI](https://img.shields.io/pypi/v/kdtrees)](https://pypi.org/project/kdtrees/)
[![GitHub](https://img.shields.io/github/license/paradoxysm/kdtrees?color=blue)](https://github.com/paradoxysm/kdtrees/blob/master/LICENSE)

[![Maintainability](https://api.codeclimate.com/v1/badges/34ab5f0112f08e766e09/maintainability)](https://codeclimate.com/github/paradoxysm/kdtrees/maintainability)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fparadoxysm%2Fkdtrees.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fparadoxysm%2Fkdtrees?)

## Overview

A K-Dimensional Tree, or K-D Tree, is a space-partitioning data structure which efficiently organizing points in k-dimensional space. For further details regarding K-D Trees, please see a detailed description on [Wikipedia](https://en.wikipedia.org/wiki/K-d_tree).

kdtrees implementation of a K-D Tree allows for construction, modification, searching, and other helpful functions such as k-nearest neighbors. It also maintains the tree in a pseudo-balanced manner through a secondary invariant where every node is the median ± dimensionality of subsidiary nodes along a specific axis.

More details regarding this implementation can be found in the documentation [here](https://github.com/paradoxysm/kdtrees/tree/master/doc)

## Installation

### Dependencies

kdtrees requires:
- numpy

kdtrees is tested and supported on Python 3.4+ up to Python 3.7. Usage on other versions of Python is not guaranteed to work as intended.

### User Installation

kdtrees can be easily installed using ```pip```

```
pip install kdtrees
```

## Changelog

See the [changelog](https://github.com/paradoxysm/kdtrees/tree/master/CHANGES.md) for a history of notable changes to kdtrees.

## Development

kdtrees is fully implemented for basic functionality. However, it may not have every utility function or have the most optimized algorithms. We welcome contributors of all experience levels to help grow and improve kdtrees. Guides on development, testing, and contribution are in the works!

Currently, particular contributions regarding pytests and documentation would be greatly appreciated. Guides and examples of usage are warmly welcomed.

## Help and Support

### Documentation

Documentation for kdtrees can be found [here](https://github.com/paradoxysm/kdtrees/tree/master/doc)

### Issues and Questions

Issues and Questions should be posed to the issue tracker [here](https://github.com/paradoxysm/kdtrees/issues)

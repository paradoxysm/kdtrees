# Changelog

### Legend

- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : Something that you couldn’t do before.
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : A miscellaneous minor improvement.
- ![Efficiency](https://img.shields.io/badge/-Efficiency-indigo) : An existing feature now may not require as much computation or memory.
- ![Fix](https://img.shields.io/badge/-Fix-red) : Something that previously didn’t work as documentated or as expected should now work.
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : An update to the documentation.
- ![Other](https://img.shields.io/badge/-Other-lightgrey) : Miscellaneous updates such as package structure or GitHub quality of life updates.


### Version 0.1.7

- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : [`_utils.format_array`](https://github.com/paradoxysm/kdtrees/blob/0.1.7/kdtrees/_utils.py) is now removed and all code is changed to reflect. **This is a major feature. `kdtrees 0.1.7` is not backwards-compatible.**
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : `__len__` no longer a required function in [`KDTreeType`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree_type.py) as per [ISS #9](https://github.com/paradoxysm/kdtrees/issues/9).
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`_utils.check_dimensionality`](https://github.com/paradoxysm/kdtrees/blob/0.1.7/kdtrees/_utils.py) now properly checks `accept` overridden types without unexepected errors.
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`KDTreeType`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree_type.py) now implements `__lt__` for proper sorting.
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`KDTreeType`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree_type.py) no longer extends `list` so that it can be properly wrapped into a list.
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`_kdtrees.nearest_neighbor`](https://github.com/paradoxysm/kdtrees/blob/0.1.7/kdtrees/_kdtrees.py) and [`_kdtrees.proximal_neighbor`](https://github.com/paradoxysm/kdtrees/blob/0.1.7/kdtrees/_kdtrees.py) now properly call [`_utils.distance`](https://github.com/paradoxysm/kdtrees/blob/0.1.7/kdtrees/_utils.py) with `accept` override applied as per [ISS #7](https://github.com/paradoxysm/kdtrees/issues/7).
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : Updated documentation to reflect changes.
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : Implemented a number of new tests in [`tests`](https://github.com/paradoxysm/kdtrees/tree/0.1.7/tests/)

### Version 0.1.6

- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : `__iter__` no longer required for [`KDTreeType`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree_type.py) as per [ISS #2](https://github.com/paradoxysm/kdtrees/issues/2).
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : `height` no longer an attribute in [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree.py) as per [ISS #6](https://github.com/paradoxysm/kdtrees/issues/6).
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`setup.py`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/setup.py) fixed with updates to metadata.
- ![Fix](https://img.shields.io/badge/-Fix-red) : Fixed equality and comparison checks in [`_kdtrees.insert`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtrees.py), [`_kdtrees.search`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtrees.py), and [`_kdtrees.delete`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtrees.py) as per [ISS #3](https://github.com/paradoxysm/kdtrees/issues/3).
- ![Fix](https://img.shields.io/badge/-Fix-red) : [`_utils.distance`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_utils.py) now implemented as per [ISS #4](https://github.com/paradoxysm/kdtrees/issues/4). Allows accept overriding to properly use `nearest_neighbor` and `proximal_neighbor`.
- ![Fix](https://img.shields.io/badge/-Fix-red) : Accept overriding is now properly implemented without fatal errors. This affected [`_utils.format_array`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_utils.py) and [`_utils.check_dimensionality`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_utils.py) as per [ISS #5](https://github.com/paradoxysm/kdtrees/issues/5).
- ![Fix](https://img.shields.io/badge/-Fix-red) : Fixed mask extractions on presorted arrays in [`_kdtrees._initialize_recursive`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtrees.py).
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : [Overview](https://github.com/paradoxysm/kdtrees/blob/0.1.6/README.md#Overview) description of [README](https://github.com/paradoxysm/kdtrees/blob/0.1.6/README.md) is now expanded slightly and includes a link to [Wikipedia](https://en.wikipedia.org/wiki/K-d_tree) for further reading.
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : Updates to [doc_kdtree.md](https://github.com/paradoxysm/kdtrees/blob/0.1.6/doc/pydoc/doc_kdtree.md) to fix the [`initialize`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/doc/pydoc/doc_kdtree.md#initialize) header.
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : Added documentation for [`KDTreeType`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/doc/pydoc/doc_kdtree_type.md).
- ![Other](https://img.shields.io/badge/-Other-lightgrey) : Created a variety of issues and pull request templates.
- ![Other](https://img.shields.io/badge/-Other-lightgrey) : Addition of CodeClimate and FOSSAS license scanning.
- ![Other](https://img.shields.io/badge/-Other-lightgrey) : `KDTreeType` is now in [`kdtrees._kdtree_type`](https://github.com/paradoxysm/kdtrees/blob/0.1.6/kdtrees/_kdtree_type.py)

### Version 0.1.5

- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : [`kdtrees`](https://github.com/paradoxysm/kdtrees/tree/0.1.5) is now implemented. We're live!
- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_kdtree.py) can now be modified by insertion and deletion.
- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_kdtree.py) now maintains itself as a pseudo-balanced tree.
- ![Feature](https://img.shields.io/badge/-Feature-blueviolet) : [`kdtrees._utils`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_utils.py) now implements `format_array` and `check_dimensionality`.
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_kdtree.py) now supports k-nearest neighbors through `nearest_neighbor`.
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_kdtree.py) now supports finding neighbors within a specified distance through `proximal_neighbor`.
- ![Enhancement](https://img.shields.io/badge/-Enhancement-purple) : [`KDTree`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/_kdtree.py) now supports custom types through the use of an `accept` clause. See [`kdtrees.kdtree_type`](https://github.com/paradoxysm/kdtrees/blob/0.1.5/kdtrees/kdtree_type.py) for implementation of required abstract base superclass.
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : Updates made to the [README](https://github.com/paradoxysm/kdtrees/blob/0.1.5/README.md) and [CHANGES](https://github.com/paradoxysm/kdtrees/blob/0.1.5/CHANGES.md).
- ![Documentation](https://img.shields.io/badge/-Documentation-blue) : [Documentation](https://github.com/paradoxysm/kdtrees/tree/0.1.5/doc) initialized and [pydoc](https://github.com/paradoxysm/kdtrees/tree/0.1.5/doc/pydoc) created.

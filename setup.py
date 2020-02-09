import os
from setuptools import setup, find_packages

def read(*paths):
    """
	Build a file path from *paths* and return the contents.
	"""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
	name='kdtrees',
	version='0.1.0',
    description='Python implementation of a K-D Tree as an AVL Tree',
    long_description=(read('README.md') + '\n\n'),
	url='http://github.com/paradoxysm/kdtrees',
    author='paradoxysm',
    license='BSD-3-Clause',
    packages=find_packages(),
    install_requires=[
		'numpy'
    ],
	python_requires='>=2.7, >=3.4, <4',
	classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
	keywords='kdtree'
    zip_safe=False)

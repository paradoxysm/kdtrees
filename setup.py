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
	version='0.1.5',
    description='Python implementation of a K-D Tree as a pseudo-balanced Tree',
    long_description=(read('README.md') + '\n\n'),
	long_description_content_type="text/markdown",
	url='http://github.com/paradoxysm/kdtrees',
	download_url = 'https://github.com/paradoxysm/kdtrees/archive/v0.1.5.tar.gz',
    author='paradoxysm',
	author_email='paradoxysm.dev@gmail.com',
    license='BSD-3-Clause',
    packages=find_packages(),
    install_requires=[
		'numpy'
    ],
	extras_require={
        'test': ['pytest', 'coverage', 'pytest-cov']
    },
	python_requires='>=3.4, <4',
	classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
	keywords=['kdtree'],
    zip_safe=True)

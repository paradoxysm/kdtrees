import pytest

from kdtrees import KDTreeType
from .test_fixtures import KDSubType, BadType, KDBadType

def test_init():
	kdtype = KDSubType(1,1)
	assert isinstance(kdtype, KDTreeType)

def test_bad_subtype():
	with pytest.raises(ValueError):
		KDSubType('a', 1)

def test_equals():
	kdtype1 = KDSubType(1, 1)
	kdtype2 = KDSubType(1, 1)
	assert kdtype1 == kdtype2

def test_not_equals():
	kdtype1 = KDSubType(1, 1)
	kdtype2 = KDSubType(1, 2)
	assert kdtype1 != kdtype2
	assert kdtype1 != 2

def test_abstract():
	with pytest.raises(TypeError):
		KDBadType(1, 1)

def test_get():
	assert KDSubType(1, 1)[0] == 1

def test_dist():
	assert KDSubType(1, 1).distance(KDSubType(1, 2)) == 1

def test_dist_mismatch():
	with pytest.raises(AttributeError):
		KDSubType(1, 1).distance(3)

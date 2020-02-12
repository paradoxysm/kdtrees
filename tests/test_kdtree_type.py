import pytest

from kdtrees import KDTreeType

def test_init():
	kdtype = KDTreeType(1)
	assert kdtype.__class__ == KDTreeType

@pytest.fixture
def kd_subtype():
	class KDSubType(KDTreeType):
		def __init__(self, dim, a):
			super().__init__(dim)
			self.a = a
	return KDSubType

def test_bad_subtype(kd_subtype):
	with pytest.raises(ValueError):
		assert kd_subtype('a', 1)

def test_equals(kd_subtype):
	kdtype1 = kd_subtype(1, 1)
	kdtype2 = kd_subtype(1, 1)
	assert kdtype1 == kdtype2

def test_not_equals(kd_subtype):
	kdtype1 = kd_subtype(1, 1)
	kdtype2 = kd_subtype(1, 2)
	assert kdtype1 != kdtype2
	assert kdtype1 != 2

def test_abstract_len(kd_subtype):
	with pytest.raises(NotImplementedError):
		assert len(kd_subtype(1, 1))

def test_abstract_get(kd_subtype):
	with pytest.raises(NotImplementedError):
		assert kd_subtype(1, 1)[0]

def test_abstract_dist(kd_subtype):
	with pytest.raises(NotImplementedError):
		assert kd_subtype(1, 1).distance(3)

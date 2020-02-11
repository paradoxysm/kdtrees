import pytest

from kdtrees import KDTreeType

def test_init():
	kdtype = KDTreeType()
	assert kdtype.__class__ == KDTreeType

@pytest.fixture
def kd_subtype():
	class KDSubType(KDTreeType):
		def __init__(self, a):
			self.a = a
	return KDSubType

def test_equals(kd_subtype):
	kdtype1 = kd_subtype(1)
	kdtype2 = kd_subtype(1)
	assert kdtype1 == kdtype2

def test_not_equals(kd_subtype):
	kdtype1 = kd_subtype(1)
	kdtype2 = kd_subtype(2)
	assert kdtype1 != kdtype2
	assert kdtype1 != 2

def test_abstract_len(kd_subtype):
	with pytest.raises(NotImplementedError):
		assert len(kd_subtype(1))

def test_abstract_get(kd_subtype):
	with pytest.raises(NotImplementedError):
		assert kd_subtype(1)[0]

def test_abstract_iter(kd_subtype):
	with pytest.raises(NotImplementedError):
		for i in kd_subtype(1):
			break

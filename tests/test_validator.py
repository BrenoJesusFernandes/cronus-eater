from cronus_eater import _validator


def test_is_magic():
    assert _validator.is_magic(1)
    assert not _validator.is_magic(0)
    assert not _validator.is_magic(-1)

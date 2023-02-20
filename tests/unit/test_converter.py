from cronus_eater import _converter


def test_blank_to_zero():
    assert _converter.blank_to_zero('- ') == 0
    assert _converter.blank_to_zero(None) == 0
    assert _converter.blank_to_zero(0.0) == 0

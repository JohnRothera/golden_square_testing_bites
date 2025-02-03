import pytest
from lib.present import *


def test_add_contents():
    johns_pressies = Present()
    johns_pressies.wrap("PS5")
    result = johns_pressies.unwrap()
    assert result == "You get a PS5!"


def test_unwrapping_without_wrapping():
    johns_pressies = Present()
    with pytest.raises(Exception) as e:
        johns_pressies.unwrap()
    error_message = str(e.value)
    assert error_message == "Pressies have been unwrapped already!"


def test_add_more_contents():
    johns_pressies = Present()
    johns_pressies.wrap("PS5")
    with pytest.raises(Exception) as e:
        johns_pressies.wrap("PS5")
    error_message = str(e.value)
    assert error_message == "Contents have already been wrapped!"

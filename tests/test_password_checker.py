import pytest
from lib.password_checker import *


def test_entered_valid_password():
    password = PasswordChecker()
    result = password.check("123456Jr00")
    assert result == True


def test_entered_password_is_invalid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid!! Password must be longer than 8 characters!"

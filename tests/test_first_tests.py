from lib.add_five import *
from lib.greet import *
from lib.check_codeword import *
from lib.report_length import *


def test_add_five_return_12_for_7():
    result = add_five(7)
    assert result == 12


def test_add_5_will_return_15_for_10():
    result = add_five(10)
    assert result == 15


def test_adding_name_returns_hello():
    result = greet("John")
    assert result == "Hello, John"


def test_codeword_is_horse():
    correct_codeword = check_codeword("Horse")
    assert correct_codeword == "Correct, come in!"


def test_codeword_starts_with_h_ends_with_e():
    close_codeword = check_codeword("House")
    assert close_codeword == "close, but nope."


def test_codeword_is_wrong():
    wrong_codeword = check_codeword("Goblin")
    assert wrong_codeword == "WRONG!"


def test_string_len_is_8():
    string_len_8 = report_length("Platform")
    assert string_len_8 == "This string is 8 characters long."

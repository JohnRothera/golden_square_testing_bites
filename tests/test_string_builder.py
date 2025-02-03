from lib.string_builder import *


def test_string_len_and_output():
    string_example = StringBuilder()
    string_example.add("Rhino")
    string_size = string_example.size()
    string_output = string_example.output()
    string_example.add(" Horn")
    string_size_2 = string_example.size()
    string_output2 = string_example.output()
    assert string_size == 5
    assert string_output == "Rhino"
    assert string_output2 == "Rhino Horn"
    assert string_size_2 == 10

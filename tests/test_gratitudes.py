from lib.gratitudes import *


def test_format_of_gratitude():
    grateful_guy = Gratitudes()
    grateful_guy.add("Love")
    grateful_guy.add("life")
    grateful_guy.add("laughing")
    assert grateful_guy.format() == "Be grateful for: Love, life, laughing"

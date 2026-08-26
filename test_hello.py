from hello import add
from hello import random_hash


def test_add():
    assert add(1, 1) == 2


def test_random_hash():
    result = random_hash()

    assert isinstance(result, str)
    assert len(result) == 64

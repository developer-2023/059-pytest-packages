from hello import hello
import sys

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

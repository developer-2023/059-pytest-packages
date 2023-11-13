from hello import hello
import sys

# 7:00:05 Harvard CS50’s Introduction to Programming with Python – Full University Course

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

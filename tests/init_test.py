"""Test the romanlander __init__ module."""

from romanlander import __version__


def test_version() -> None:
    assert isinstance(__version__, str)

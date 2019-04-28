import pytest


def test_empty_db(flask_app):
    """Start with a blank database."""

    assert 1 + 1 == 2

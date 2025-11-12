import pytest

from note import rate_note

@pytest.mark.parametrize("note", [8,7,9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"

def test_rate_10_returns_acceptable():
    assert rate_note(10) == "acceptable"

def test_rate_12_returns_good():
     assert rate_note(12) == "good"

def test_rate_13_returns_good():
    assert rate_note(13) == "good"

def test_rate_11_returns_acceptable():
    assert rate_note(11) == "acceptable"

def test_rate_14_returns_verygood():
    assert rate_note(14) == "verygood"
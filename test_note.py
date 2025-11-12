import pytest

from note import rate_note

import pytest
from note import rate_note

@pytest.mark.parametrize(
    "note, expected",
    [
        (0, "unsuccessful"),
        (1, "unsuccessful"),
        (2, "unsuccessful"),
        (3, "unsuccessful"),
        (4, "unsuccessful"),
        (5, "unsuccessful"),
        (6, "unsuccessful"),
        (7, "unsuccessful"),
        (8, "unsuccessful"),
        (9, "unsuccessful"),
        (10, "acceptable"),
        (11, "acceptable"),
        (12, "good"),
        (13, "good"),
        (14, "verygood"),
        (15, "verygood"),
        (17, "excellent"),
        (20, "excellent"),
    ],
)
def test_rate_note(note, expected):
    assert rate_note(note) == expected
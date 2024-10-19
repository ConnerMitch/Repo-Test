import pytest
from our_add import our_add


def test_trivial_add():
    assert our_add(2, 3 ) == 5, "Should be 5"

def test_for_negatives():
    assert our_add(-2, -3) == -5, "Should be -5"

def test_for_mixed():
    assert our_add(-2, 3) == 1, "Should be 1 (error)"

@pytest.mark.parametrize("a, b, result",[(1,2,3),(2,4,6),(3,7,10),(4,8,12)])
def test_multiples(a, b, result):
   assert result == our_add(a, b)


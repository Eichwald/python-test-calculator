import pytest

from src.calculator import add

@pytest.mark.c0001
def test_add():
    result = add(3, 4)
    assert result == 7

@pytest.mark.c0002
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)

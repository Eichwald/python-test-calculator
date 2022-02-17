import pytest
import os

from src.calculator import add

def test_add():
    result = add(3, 4)
    assert result == 7

def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)

def test_exe():
    os.startfile("ADD_CLI.exe")
from src.calculator import multiply
import pytest



def test_multiply():
    result = multiply(3, 4)
    assert result == 12
<<<<<<< HEAD

=======
>>>>>>> 1cbd41d3c8f1a53080735cb9fe68485f51fe4968


def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)

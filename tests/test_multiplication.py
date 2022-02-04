from src.calculator import multiply
import pytest
from src.testrail import *

client = APIClient('https://testautomationtest.testrail.io/')
client.user = 'jonas.eichwald@velux.com'
client.password = '6/FeVpnvRjU3TjdRFnkT'


def test_multiply():
    result = multiply(3, 4)
    assert result == 12
    # res = client.send_post(
    #     'add_result_for_case/20/2374',
    #     {'status_id': 1, 'comment': 'This test did not work fine!'}
    # )

    # print(res)


def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)

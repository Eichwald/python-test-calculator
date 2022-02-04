import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.calculator import add
from src.testrail import *

client = APIClient('https://testautomationtest.testrail.io/')
client.user = 'jonas.eichwald@velux.com'
client.password = '6/FeVpnvRjU3TjdRFnkT'


def test_add():
    result = add(3, 4)
    assert result == 7
    # res = client.send_post(
    #    'add_result_for_case/20/2373',
    #    {'status_id': 2, 'comment': 'This test worked fine!'}
    #)

    #print(res)


def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)

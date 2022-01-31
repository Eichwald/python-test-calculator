import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.calculator import add
from src.testrail import *

client = APIClient('https://testautomationtest.testrail.io/')
client.user = 'jonas.eichwald@velux.com'
client.password = '6/FeVpnvRjU3TjdRFnkT'

chrome_options = Options()
chrome_options.binary_location = r"C:\Users\45232\Desktop\Codeing\python-test-calculator\src/chromedriver.exe"
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')


def test_sele():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    driver.close()
    driver.quit()


def test_add():
    result = add(3, 4)
    assert result == 7
    res = client.send_post(
        'add_result_for_case/20/2373',
        {'status_id': 2, 'comment': 'This test worked fine!'}
    )

    print(res)


def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)

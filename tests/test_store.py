import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config.settings import DRIVER_PATH, BASE_DIR


@pytest.fixture
def root_url():
    return f'file:///{BASE_DIR / "store-template" / "index.html"}'


def test_titles_are_correct(root_url):
    service = Service(executable_path=DRIVER_PATH)
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()

    time.sleep(2)
    browser.get(root_url)

    time.sleep(2)
    main_title = browser.find_element(By.CLASS_NAME, 'navbar-brand')
    assert main_title.text == 'Store'

    time.sleep(2)
    purchase_link = browser.find_element(By.ID, 'start-purchase-link')
    purchase_link.click()

    time.sleep(2)
    product_title = browser.find_element(By.ID, 'product-title')
    assert product_title.text == 'Store'

    time.sleep(2)
    browser.quit()

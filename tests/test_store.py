from selenium import webdriver

DRIVER_PATH = '/Users/vokler/projects/WebDriver/chromedriver'


def test_browser():
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.maximize_window()
    browser.get("https://www.google.com")
    browser.quit()

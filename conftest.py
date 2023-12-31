import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_debug():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("\nLaunch test. . . ")
    yield driver
    driver.close()
    driver.quit()
    print("\nFinish test...")

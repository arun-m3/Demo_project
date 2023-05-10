import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.provet.cloud/request-demo?hsCtaTracking=a3ea9906-246e-43f6-8ae9-d4aec8d67b08%7C5fc25f4f-8d28-4224-8de3-66ec41604683")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

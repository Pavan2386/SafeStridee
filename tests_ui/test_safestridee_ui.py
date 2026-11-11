
import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = os.getenv(
    "SAFESTRIDE_BASE_URL",
    "http://127.0.0.1:59985"
)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Edge(options=options)
    browser.implicitly_wait(5)

    yield browser

    browser.quit()


def test_home_page_title(driver):
    driver.get(BASE_URL)

    assert driver.title == "SafeStride Pro with Jenkins CI/CD"


def test_login_screen_elements(driver):
    driver.get(BASE_URL)

    assert driver.find_element(By.ID, "s-login").is_displayed()
    assert driver.find_element(By.ID, "l-user").is_displayed()
    assert driver.find_element(By.ID, "l-pass").is_displayed()


def test_registration_navigation(driver):
    driver.get(BASE_URL)

    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Create New Account')]"
    ).click()

    registration_screen = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "s-register"))
    )

    assert registration_screen.is_displayed()
    assert driver.find_element(By.ID, "r-user").is_displayed()
    assert driver.find_element(By.ID, "r-pass").is_displayed()
    assert driver.find_element(By.ID, "r-ec").is_displayed()

def test_caregiver_portal(driver):
    driver.get(BASE_URL + "/portal")

    assert driver.title == "SafeStride Caregiver Portal"
    assert driver.find_element(By.ID, "uid").is_displayed()
    assert driver.find_element(
        By.XPATH, "//button[contains(text(), 'TRACK')]"
    ).is_displayed()
    assert driver.find_element(
        By.XPATH, "//button[contains(text(), 'AUTO REFRESH')]"
    ).is_displayed()

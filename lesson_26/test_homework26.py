"""Тест перевірки верифікації у двох фреймах."""

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


@pytest.fixture
def setup_driver():
    """Ініціалізація драйвера."""
    driver = Chrome()
    driver.get('http://localhost:8000/dz.html')
    yield driver  # Повертає драйвер для використання у тесті
    driver.quit()  # Закриття драйвера після завершення тесту


def test_frame_verification(setup_driver):
    """Тест верифікації у двох фреймах."""
    driver = setup_driver

    # фрейм 1
    driver.switch_to.frame(driver.find_element(By.ID, 'frame1'))
    frame1_field = driver.find_element(By.ID, 'input1')
    frame1_field.send_keys('Frame1_Secret')
    check_button1 = driver.find_element(
        By.CSS_SELECTOR,
        'button[onclick="verifyInput(\'input1\')"]',
    )
    check_button1.click()

    # alert
    alert = Alert(driver)
    assert (
        alert.text == 'Верифікація пройшла успішно!'
    ), 'Frame 1 verification failed'
    alert.accept()

    # Повернення до основного контенту
    driver.switch_to.default_content()

    # фрейм 2
    driver.switch_to.frame(driver.find_element(By.ID, 'frame2'))
    frame2_field = driver.find_element(By.ID, 'input2')
    frame2_field.send_keys('Frame2_Secret')
    check_button2 = driver.find_element(
        By.CSS_SELECTOR,
        'button[onclick="verifyInput(\'input2\')"]',
    )
    check_button2.click()

    # alert
    alert = Alert(driver)
    assert (
        alert.text == 'Верифікація пройшла успішно!'
    ), 'Frame 2 verification failed'
    alert.accept()

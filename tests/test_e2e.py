import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Test login through browser
def test_login_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    assert 'login' not in driver.current_url.lower()


# Test task creation through browser
def test_create_task_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    driver.get('http://localhost:5000/add')
    driver.find_element(By.NAME, 'title').send_keys('UI Test')
    driver.find_element(By.NAME, 'description').send_keys('Test')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    assert 'UI Test' in driver.page_source


# Test task list viewing
def test_view_tasks_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    driver.get('http://localhost:5000/')
    time.sleep(1)
    assert 'task' in driver.page_source.lower()

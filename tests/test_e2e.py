import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--remote-debugging-port=9222')
    
    # Essayer de détecter Chromium snap si disponible
    if os.path.exists('/snap/bin/chromium'):
        options.binary_location = '/snap/bin/chromium'
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
    finally:
        try:
            driver.quit()
        except:
            pass


# Test 1: Login page -> login -> verify redirect
def test_login_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    assert 'login' not in driver.current_url.lower()


# Test 2: Create task through UI -> verify it appears
def test_create_task_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    
    driver.get('http://localhost:5000/tasks/new')
    driver.find_element(By.NAME, 'title').send_keys('UI Test Task')
    driver.find_element(By.NAME, 'description').send_keys('Testing UI')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    assert 'UI Test Task' in driver.page_source


# Test 3: View task list through UI
def test_view_tasks_ui(driver):
    driver.get('http://localhost:5000/login')
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    assert 'Task Manager' in driver.page_source or 'task' in driver.page_source.lower()

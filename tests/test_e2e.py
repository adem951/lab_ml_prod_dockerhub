import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope='module')
def driver(live_server):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    # Détecter le binaire Chrome/Chromium
    if os.path.exists('/snap/bin/chromium'):
        options.binary_location = '/snap/bin/chromium'
    elif os.path.exists('/usr/bin/chromium'):
        options.binary_location = '/usr/bin/chromium'
    elif os.path.exists('/usr/bin/chromium-browser'):
        options.binary_location = '/usr/bin/chromium-browser'
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    driver.quit()


# Test 1: Login page -> login -> verify redirect
def test_login_ui(driver):
    """Visit login page, login, verify redirect"""
    driver.get('http://localhost:5000/login')
    
    # Attendre le chargement de la page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    
    # Remplir le formulaire
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Vérifier la redirection (vers la page d'accueil)
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != 'http://localhost:5000/login'
    )
    
    # Vérifier qu'on n'est plus sur la page de login
    assert 'login' not in driver.current_url.lower() or driver.current_url == 'http://localhost:5000/'


# Test 2: Create task through UI -> verify it appears
def test_create_task_ui(driver):
    """Create task through UI and verify it appears"""
    # Login d'abord
    driver.get('http://localhost:5000/login')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Attendre la redirection
    time.sleep(2)
    
    # Aller à la page de création de tâche
    driver.get('http://localhost:5000/tasks/new')
    
    # Attendre le formulaire
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'title'))
    )
    
    # Créer une tâche
    driver.find_element(By.NAME, 'title').send_keys('E2E Test Task')
    driver.find_element(By.NAME, 'description').send_keys('Created via Selenium')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Attendre et vérifier que la tâche apparaît
    time.sleep(2)
    assert 'E2E Test Task' in driver.page_source or 'Created via Selenium' in driver.page_source


# Test 3: View task list through UI
def test_view_tasks_ui(driver):
    """View task list through UI"""
    # Login
    driver.get('http://localhost:5000/login')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Attendre d'être redirigé vers la page d'accueil
    time.sleep(2)
    
    # Vérifier qu'on voit la liste des tâches ou le titre de la page
    page_content = driver.page_source.lower()
    assert 'task' in page_content or 'tâche' in page_content or driver.current_url == 'http://localhost:5000/'

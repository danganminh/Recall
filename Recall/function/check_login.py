import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def check_captcha(driver):
    try:
        WebDriverWait(driver, 5).until( 
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div[2]'))
        )
        return True
    except TimeoutException:
        print("Not captcha")
        return False


def login(driver):
	
    #phone_number = "your_phone_number"
    #pass_word = "your_pass"

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input').send_keys(phone_number)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input').send_keys(pass_word)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button').click()
    time.sleep(1)


def check_login(driver, login_auto=True):
    try:
        # Check login
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/header/div[1]/nav/ul/li[3]/div/div/div/div[2]'))
        )
        return True
    except TimeoutException:
        try:
            # Wait Login Box
            WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]'))
            )
            print("Login page")
            if login_auto:    
                login(driver)
            return True
        except TimeoutException:
            print("Not login page")
            return False

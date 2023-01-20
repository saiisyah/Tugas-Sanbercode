import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from doc import data

class TestLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_LogIn_Negatif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID,"user-name").send_keys(data.nama)
        time.sleep(4)
        driver.find_element(By.ID,"password").send_keys(data.passowrd)
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        response_message = driver.find_element(By.CSS_SELECTOR,"error").text
        time.sleep(3)
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')
        time.sleep(2)

    def test_LogIn_Positif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID,"user-name").send_keys("problem_user")
        time.sleep(4)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        
    def test_Name_AtoZ(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window
        time.sleep(3)
        driver.find_element(By.ID,"product_sort_container").is_selected("Name (A to Z)").click()
        time.sleep(3)



unittest.main()

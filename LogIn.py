import unittest
import time
from selenium import webdriver
from selenium.webdriver.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from page import locator

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Negatif(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("yahuud123@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("straykids") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()

        response_message = driver.find_element(By.CSS_SELECTOR,"<div id="swal2-content" class="swal2-html-container" style="display: block;">Email atau Password Anda Salah</div>").text
        self.assertEqual(response_message,'Email atau Password Anda Salah')

    def tearDown(self):
        self.browser.close()

unittest.main

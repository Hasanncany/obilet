from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest


class Test_O_Bilett():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.obilet.com/")

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(locator))

    #Başarılı giriş
    @pytest.mark.parametrize("mail,password",[("hassncan.yildirim21@gmail.com","123456789")])
    def test_unsuccess_register(self,mail,password):
        self.wait_for_element_visible((By.CLASS_NAME, "login"))
        loginBtn = self.driver.find_element(By.CLASS_NAME, "login")
        loginBtn.click()

        self.wait_for_element_visible((By.XPATH, "//*[@id='login-form']/div[5]/a"))
        register_page = self.driver.find_element(By.XPATH, "//*[@id='login-form']/div[5]/a")
        register_page.click()

        self.wait_for_element_visible((By.NAME, "email"))
        mail_input = self.driver.find_element(By.NAME, "email")

        self.wait_for_element_visible((By.NAME, "password"))
        password_input = self.driver.find_element(By.NAME, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(mail_input,mail)
        action.send_keys_to_element(password_input,password)
        action.perform()

        box = self.driver.find_element(By.XPATH, "//*[@id='can-use-contract-information']/div")
        box.click()

        registerBtn = self.driver.find_element(By.XPATH, "//*[@id='register-form']/div[6]/button")
        registerBtn.click()
        sleep(5)
        
        self.wait_for_element_visible((By.XPATH, "//*[@id='header']/div[1]/div/ul/li[2]/a"))
        accountBtn = self.driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div/ul/li[2]/a")
        accountBtn.click()
        sleep(15)

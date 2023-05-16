from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest

class Test_O_Bilet():

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.obilet.com/")

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(locator))

    #Mail ve şifre boş deneme
    @pytest.mark.parametrize("mail,password",[("","")])
    def test_empty_mail_and_password_register(self,mail,password):
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

        mail_error_message = self.driver.find_element(By.ID, "email-error")
        assert mail_error_message.text == "E-mail adresi boş bırakılamaz"
        
        password_error_message = self.driver.find_element(By.ID, "password-error")
        assert password_error_message.text == "Şifre boş bırakılamaz"

    #Boş mail
    @pytest.mark.parametrize("mail,password",[("","123456789")])
    def test_empty_mail_register(self,mail,password):
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

        mail_error_message = self.driver.find_element(By.ID, "email-error")
        assert mail_error_message.text == "E-mail adresi boş bırakılamaz"

    #Boş şifre
    @pytest.mark.parametrize("mail,password",[("hasancan.yildirim21@hotmail.com","")])
    def test_empty_password_register(self,mail,password):
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
        
        password_error_message = self.driver.find_element(By.ID, "password-error")
        assert password_error_message.text == "Şifre boş bırakılamaz"

    #5 Haneli parola girişi
    @pytest.mark.parametrize("mail,password",[("hasancan.yildirim21@hotmail.com","12345")])
    def test_missing_password(self,mail,password):
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
        
        password_error_message = self.driver.find_element(By.ID, "password-error")
        assert password_error_message.text == "Şifreniz en az 6 karakter olmalıdır"

    
    #Daha önce kayıt olan kullanıcı girişi
    @pytest.mark.parametrize("mail,password",[("hasancan.yildirim21@hotmail.com","Hasancan..11")])
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

        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='register-form']/div[6]/div[1]/label")
        assert errorMessage.text == "Bu kullanıcı sisteme daha önceden kayıt olmuştur."

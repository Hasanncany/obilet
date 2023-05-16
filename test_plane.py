from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from pathlib import Path
from datetime import date


class Test_Plane():

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        self.driver.maximize_window()
        self.driver.get("https://www.obilet.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def wait_for_element_visible(self,locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(locator))
    
    def test_buy_plane_ticket(self):
        #Uçak Bileti Sayfasına Gitme
        self.wait_for_element_visible((By.XPATH,"//*[@id='header']/div[2]/div/ul/li[2]/a"))
        plainBtn = self.driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/ul/li[2]/a")
        plainBtn.click()
        sleep(3)
        self.driver.save_screenshot(f"{self.folderPath}/Uçak bileti satın alma sayfası açıldı.png")

        #Kalkış Yeri locator
        self.wait_for_element_visible((By.ID, "origin-input"))
        departure = self.driver.find_element(By.ID, "origin-input")
        
        #Gidilecek Yer locator
        self.wait_for_element_visible((By.ID, "destination-input"))
        arrival = self.driver.find_element(By.ID, "destination-input")
        sleep(3)

        #Kalkış Yeri seçme
        departure.send_keys("istanbul")
        sleep(2)        

        #Kalkış Havalimanı Seçme
        self.wait_for_element_visible((By.XPATH, "//li[contains(span[@class='location'], 'Sabiha')]"))
        istanbulSaw = self.driver.find_element(By.XPATH, "//li[contains(span[@class='location'], 'Sabiha')]") 
        istanbulSaw.click()
        self.driver.save_screenshot(f"{self.folderPath}/Nereden.png")
        
        #Gidiş Tarihi Seçme -> 16 Ağustos 2023
        self.wait_for_element_visible((By.ID, "departure"))
        departureDate = self.driver.find_element(By.ID, "departure-input")
        departureDate.click()
        sleep(2)

        #Takvimde İleri Gitme
        self.wait_for_element_visible((By.XPATH, "//*[@id='departure']/div/div/div[2]/div/table/thead/tr[1]/th[3]"))
        departureDateNext = self.driver.find_element(By.XPATH, "//*[@id='departure']/div/div/div[2]/div/table/thead/tr[1]/th[3]")
        departureDateNext.click()
        sleep(2)
        departureDateNext = self.driver.find_element(By.XPATH, "//*[@id='departure']/div/div/div[2]/div/table/thead/tr[1]/th[3]")
        departureDateNext.click()
        sleep(2)
        departureDateNext = self.driver.find_element(By.XPATH, "//*[@id='departure']/div/div/div[2]/div/table/thead/tr[1]/th[3]")                   
        departureDateNext.click()
        sleep(2)
        
        #16 Ağustos'u seçme
        self.wait_for_element_visible((By.XPATH, "//*[@id='departure']/div/div/div[1]/div/table/tbody/tr[3]/td[3]/button"))
        date = self.driver.find_element(By.XPATH, "//*[@id='departure']/div/div/div[1]/div/table/tbody/tr[3]/td[3]/button")
        date.click()
        self.driver.save_screenshot(f"{self.folderPath}/Gidiş tarihi seçildi..png")
    
        #Gidilecek Havalimanı seçme
        arrival.send_keys("batman")
        sleep(3)
        self.wait_for_element_visible((By.XPATH, "//li[contains(span[@class='location'], 'Batman')]"))
        batman = self.driver.find_element(By.XPATH, "//li[contains(span[@class='location'], 'Batman')]")
        batman.click()
        self.driver.save_screenshot(f"{self.folderPath}/Nereye.png")


        #Dönüş Tarihi Seçme -> 29 Ekim
        self.wait_for_element_visible((By.ID, "return-input-placeholder"))
        returnDate = self.driver.find_element(By.ID, "return-input-placeholder")
        returnDate.click()                              
        sleep(2)
        
        #Takvimde ileri gitme
        self.wait_for_element_visible((By.XPATH, "//*[@id='return']/div/div[1]/div[2]/div/table/thead/tr[1]/th[3]"))
        returnNext = self.driver.find_element(By.XPATH, "//*[@id='return']/div/div[1]/div[2]/div/table/thead/tr[1]/th[3]")
        returnNext.click()
        sleep(2)

        #29 Ekim'i seçme
        self.wait_for_element_visible((By.XPATH, "//*[@id='return']/div/div[1]/div[2]/div/table/tbody/tr[5]/td[7]/button/span"))
        date2 = self.driver.find_element(By.XPATH, "//*[@id='return']/div/div[1]/div[2]/div/table/tbody/tr[5]/td[7]/button/span")
        date2.click()
        self.driver.save_screenshot(f"{self.folderPath}/Gidiş tarihi seçildi.png")
        sleep(2)


        #Bilet Arama
        self.wait_for_element_visible((By.ID, "search-button"))
        searchBtn = self.driver.find_element(By.ID, "search-button")
        searchBtn.click()
        
        #Gidiş Bileti - Pegasus 10:50
        self.wait_for_element_visible((By.ID, "journey-SAW-BAL-20230816--1006PC--1006PC-2370-1"))
        pgs_gidis = self.driver.find_element(By.ID, "journey-SAW-BAL-20230816--1006PC--1006PC-2370-1")
        self.driver.save_screenshot(f"{self.folderPath}/Gidiş biletleri.png")
        pgs_gidis.click()

        #Dönüş Bileti - Anadolu Jet 15:40
        self.wait_for_element_visible((By.ID, "journey-BAL-SAW-20231029--1000AN--1000AN-TK7371-1"))
        ajet_donus = self.driver.find_element(By.ID, "journey-BAL-SAW-20231029--1000AN--1000AN-TK7371-1")
        self.driver.save_screenshot(f"{self.folderPath}/Dönüş biletleri.png")
        ajet_donus.click()
        sleep(3)

        #Eco Seçme
        self.wait_for_element_visible((By.CLASS_NAME, "fly-content-container.EF"))
        eco = self.driver.find_element(By.CLASS_NAME, "fly-content-container.EF")
        self.driver.save_screenshot(f"{self.folderPath}/Sınıflar.png")
        eco.click()
        sleep(5)
        self.driver.save_screenshot(f"{self.folderPath}/Bilet kontrolü.png")

from user_info import eposta,username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = webdriver.Firefox()

class Instagram :
    def __init__(self,eposta,username,password):
        self.username=username
        self.password=password
        self.eposta=eposta
    
    def sign(self):
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput= driver.find_element(By.NAME,'username')
        passwordInput=driver.find_element(By.NAME,'password')
        login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        time.sleep(1)
        usernameInput.send_keys(self.eposta)
        passwordInput.send_keys(self.password)
        time.sleep(1)
        login.click()
        time.sleep(5)
    
    def get_profil(self):
        driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(7)
    
    def get_follower(self,otherUsername=username):
        driver.get(f"https://www.instagram.com/{otherUsername}")
        time.sleep(2)
        t=driver.find_elements(By.CLASS_NAME,'_ac2a')[1]
        takipci=t.text
        t.click()
        time.sleep(1)
        s=0
        tikla=driver.find_element(By.CLASS_NAME,'_aano')
        tikla.click()
        takipci_listesi=[]
        time.sleep(1)
        while True:
            takiciler=driver.find_elements(By.CSS_SELECTOR,'._aacl._aaco._aacw._aacx._aad7._aade')
            if len(takiciler) >= int(takipci):
                for i in takiciler:
                    ad=i.text
                    print(ad)
                    takipci_listesi.append(ad)
                break
            tikla.send_keys(Keys.SPACE)
            print(f"yüklenen takipçi :{len(takiciler)}")
        #burada takipçi listesi geliyor istediğin gibi kullanabilirsin
        print(f"takipçi sayısı:{len(takipci_listesi)}")
        

    
        
#kendi hesabınız ise user_info.py dosyasındaki 
#eposta , username ve password alanlarını doldurabilirsiniz 
instagram=Instagram(eposta,username,password)
instagram.sign()
instagram.get_follower()

driver.quit()
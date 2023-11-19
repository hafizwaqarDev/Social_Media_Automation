import traceback
from selenium.webdriver.chrome.options import Options
import threading
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
import time
import psutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from collections import defaultdict
import pandas as pd
import time,csv


class faceBook_Posts():
    def __init__(self,inputText):
       # enter you login info here
        self.userEmail = '_-------'
        self.userPassword = '_------_'
         # enter a correct path here....
        self.inputText = inputText
        self.mainFolderPath = r'C:\Users\New folder (2)\images_for_posts'

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument("--disable-gpu")

    def startChrome(self):
        return os.system('"C:\Program Files\chrome.exe" --remote-debugging-port=9222')

    def closeBrowser(self):
        try:
            PROCNAME = "chromedriver.exe"
            userName = os.getlogin()
            for proc in psutil.process_iter():
                print(str(proc.name()))
                print(proc.username())
                proc.kill()
        except Exception as ex:
            print(str(ex))
    

    def startScraping(self):
        path = chromedriver_autoinstaller.install(cwd=True)
        print(path)
        time.sleep(2)
        self.closeBrowser()
        time.sleep(2)
        th = threading.Thread(target=self.startChrome, args=())
        th.daemon = True
        th.start()
        time.sleep(3)
        driver = webdriver.Chrome(options=self.chrome_options)
        return driver

    def loginProcess(self,driver):
        print('[INFO] Please wait facebook is logging now..........')
        Inputemail = driver.find_element(By.XPATH,'//input[@id="email"]')
        Inputemail.send_keys(self.userEmail)
        time.sleep(3)
        Inputpassword = driver.find_element(By.XPATH,'//input[@type="password"]')
        Inputpassword.click()
        time.sleep(1)
        checkLogin = driver.find_element(By.XPATH,'//button[@name="login"]')
        checkLogin.click()
        time.sleep(2)
        driver.get('https://www.facebook.com/profile')
        time.sleep(3)
    
    def post_process(self,driver,imagefile):
        try: 
            postoptionbtn = driver.find_element(By.XPATH,'//span[text()="Photo/video"]')
            postoptionbtn.click()
        except:
            pass
            
        try: 
            checkPostreq = driver.find_element(By.XPATH,'//span[text()="Default audience"]')
            if checkPostreq: resultReq = True
        except:
            resultReq = False
        if resultReq == True: 
            try: 
                sowPublic = driver.find_element(By.XPATH,'//span[text()="Public"]')
                sowPublic.click()
            except: pass
            try: 
                doneBtn = driver.find_element(By.XPATH,'//span[text()="Done"]')
                doneBtn.click()
            except: pass
        time.sleep(2)
        try: 
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/*f,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
            time.sleep(3)
            postImage.send_keys(imagefile)
        except:
            time.sleep(2)
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
            time.sleep(3)
            postImage.send_keys(imagefile)
        time.sleep(2)
        try: 
            postBtn = driver.find_element(By.XPATH,'//span[text()="Post"]')
            postBtn.click()
        except:
            time.sleep(2)
            postBtn = driver.find_element(By.XPATH,'//span[text()="Post"]')
            postBtn.click()
        time.sleep(12)
        print(f'[INFO] {imagefile} Posted Successfully')

    
    def run(self):
        folderPath = self.mainFolderPath
        driver = self.startScraping()
        driver.get('https://www.facebook.com/profile')
        try: 
            checkLogin = driver.find_element(By.XPATH,'//button[@name="login"]')
            if checkLogin: resultLogin = True
        except: resultLogin = False
        # login process
        if resultLogin == True: self.loginProcess(driver)
        time.sleep(3)
        print()
        file_list = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
        if file_list:
            for file in file_list:
                time.sleep(5)
                filePath = os.path.join(folderPath,file)
                self.post_process(driver,filePath)
        else:
            print('[INFO] Please add some photos in the select folder.Now the folder is empty........')


if __name__ == '__main__':
    inputText = input('\n[INFO] Please enter your text for post:-')
    beenVerified = faceBook_Posts(inputText)
    driver = beenVerified.run()

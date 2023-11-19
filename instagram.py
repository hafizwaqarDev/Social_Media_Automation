from selenium.webdriver.chrome.options import Options
import time, os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Instagram_Auto_Posts():
    def __init__(self,args):
        self.userName = args.username
        self.userPassword = args.password
        self.inputText = args.text
        self.image = args.image


    def openBrowser(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        return driver
    
    def loginProcess(self,driver):
        time.sleep(4)
        print('\n[INFO] Please wait Instagram is logging now..........')
        userName = self.userName
        userPassword = self.userPassword
        try:
            userEmailTag = driver.find_element(By.XPATH,'//input[@aria-label="Phone number, username, or email"]')
            time.sleep(2)
            time.sleep(2)
            userEmailTag.clear()
            userEmailTag.send_keys(userName)
            time.sleep(4)
        except:
            userEmailTag = driver.find_element(By.XPATH,'//input[@aria-label="Phone number, username, or email"]')
            time.sleep(2)
            userEmailTag.clear()
            userEmailTag.click()
            time.sleep(1)
            userEmailTag.clear()
            userEmailTag.send_keys(userName)
            time.sleep(4)
        try:
            userPasswordTag = driver.find_element(By.XPATH,'//input[@aria-label="Password"]')
            time.sleep(2)
            userPasswordTag.click()
            userPasswordTag.send_keys(userPassword)
            time.sleep(3)
        except:
            userPasswordTag = driver.find_element(By.XPATH,'//input[@aria-label="Password"]')
            userPasswordTag.click()
            time.sleep(2)
            userPasswordTag.clear()
            userPasswordTag.send_keys(userPassword)
            time.sleep(3)
        
        submitLogin = driver.find_element(By.XPATH,'//button[@type="submit"]')
        time.sleep(2)
        submitLogin.click()
        time.sleep(8)
        try:
            notnowbutton= driver.find_element(By.XPATH,"//div[text()='Not Now']")
            time.sleep(5)
        except:
            pass
        try:
            notNowButton = driver.find_element(By.XPATH,'//button[text()="Not Now"]')
            time.sleep(2)
            notNowButton.click()
            time.sleep(1)
        except: pass

    def post_process(self,driver):
        # image = r'{self.image}'
        image = image
        title_text = self.inputText
        try:
            creatbtn = driver.find_element(By.XPATH,'//div[@class="x1iyjqo2 xh8yej3"]/div[7]')
            time.sleep(3)
            creatbtn.click()
            time.sleep(4)
        except:
            creatbtn = driver.find_element(By.XPATH,'//div[@class="x1iyjqo2 xh8yej3"]/div[7]')
            time.sleep(3)
            creatbtn.click()
            time.sleep(4)
        try:
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime"]')
            time.sleep(2)
            postImage.send_keys(image)
            time.sleep(3)
        except:
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime"]')
            time.sleep(3)
            postImage.send_keys(image)
            time.sleep(3)
        try:
            nextbutton = driver.find_element(By.XPATH,'//div[text()="Next"]')
            time.sleep(2)
            nextbutton.click()
            time.sleep(4)
        except:
            nextbutton = driver.find_element(By.XPATH,'//div[text()="Next"]')
            time.sleep(2)
            nextbutton.click()
            time.sleep(4)
        try:
            nextbutton = driver.find_element(By.XPATH,'//div[text()="Next"]')
            time.sleep(2)
            nextbutton.click()
            time.sleep(3)
        except:
            nextbutton = driver.find_element(By.XPATH,'//div[text()="Next"]')
            time.sleep(2)
            nextbutton.click()
            time.sleep(3)
            
        time.sleep(2)
        print(f'[INFO] {image} Posted Successfully')
        time.sleep(3)
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        
    def run(self):
        driver = self.openBrowser()
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        # login process
        self.loginProcess(driver)
        time.sleep(3)
        print()
        self.post_process(driver)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description")
    parser.add_argument('-u', '--username', required=True, help='Username')
    parser.add_argument('-p', '--password', required=True, help='Password')
    parser.add_argument('-t', '--text', required=True, help='Text')
    parser.add_argument('-i', '--image', required=True, help='Image file')
    args = parser.parse_args()

    beenVerified = Instagram_Auto_Posts(args)
    driver = beenVerified.run()

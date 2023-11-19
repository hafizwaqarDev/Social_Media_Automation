from selenium.webdriver.chrome.options import Options
from optparse import OptionParser
import time, os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Twitter_Auto_Posts():
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
        driver.get('https://twitter.com/i/flow/login')
        time.sleep(4)
        print('\n[INFO] Please wait Twitter is logging now..........')
        userName = self.userName
        userPassword = self.userPassword
        try: 
            userNameButton = driver.find_element(By.XPATH,'//input[@autocomplete="username"]')
            userNameButton.click()
            userNameButton.clear()
            time.sleep(1)
            userNameButton.send_keys(userName)
        except:
            userNameButton = driver.find_element(By.XPATH,'//input[@autocomplete="username"]')
            userNameButton.click()
            userNameButton.clear()
            time.sleep(1)
            userNameButton.send_keys(userName)
        time.sleep(2)
        try:
            clickOnNext = driver.find_element(By.XPATH,'//span[text()="Next"]')
            clickOnNext.click()
            time.sleep(2)
        except:
            clickOnNext = driver.find_element(By.XPATH,'//span[text()="Next"]')
            clickOnNext.click()
            time.sleep(2)
        time.sleep(2)
        try:
            loginButton = driver.find_element(By.XPATH,'//div[@data-testid="LoginForm_Login_Button"]')
            loginButton.click()
            time.sleep(2)
        except:
            loginButton = driver.find_element(By.XPATH,'//div[@data-testid="LoginForm_Login_Button"]')
            loginButton.click()
            time.sleep(2)

    def post_process(self,driver):
        # image = r'{self.image}'
        imagefile = self.image
        title_text = self.inputText
        try:
            InputtextTag = driver.find_element(By.XPATH,'//div[@data-contents="true"]')
            time.sleep(2)
            InputtextTag.send_keys(title_text)
            time.sleep(2)
        except:
            InputtextTag = driver.find_element(By.XPATH,'//div[@data-contents="true"]')
            time.sleep(2)
            InputtextTag.send_keys(title_text)
            time.sleep(2)
        try:
            closeSuggestion = driver.find_element(By.XPATH,'//div[@data-testid="app-bar-close"]')
            closeSuggestion.click()
            time.sleep(2)
        except: pass
        time.sleep(2)
        print(f'[INFO] {imagefile} Posted Successfully')

    def run(self):
        driver = self.openBrowser()
        driver.get('https://twitter.com/')
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
    
    beenVerified = Twitter_Auto_Posts(args)
    driver = beenVerified.run()

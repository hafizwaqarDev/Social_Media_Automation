from selenium.webdriver.chrome.options import Options
import time, os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Pinterest_Auto_Posts():
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
        print('\n[INFO] Please wait Pinterest is logging now..........')
        userEmail = self.userName
        userPassword = self.userPassword
        try:
            login = driver.find_element(By.XPATH,'//div[text()="Log in"]')
            login.click()
            time.sleep(4)
        except:
            login = driver.find_element(By.XPATH,'//div[text()="Log in"]')
            login.click()
            time.sleep(4)
        try:
            userEmailTag = driver.find_element(By.XPATH,'//input[@autocomplete="email"]')
            userEmailTag.clear()
            userEmailTag.click()
            time.sleep(2)
            userEmailTag.clear()
            userEmailTag.send_keys(userEmail)
            time.sleep(4)
        except:
            userEmailTag = driver.find_element(By.XPATH,'//input[@autocomplete="email"]')
            userEmailTag.clear()
            userEmailTag.click()
            time.sleep(2)
            userEmailTag.clear()
            userEmailTag.send_keys(userEmail)
        try:
            submitLogin = driver.find_element(By.XPATH,'//div[@data-test-id="registerFormSubmitButton"]/button[@type="submit"]')
            submitLogin.click()
            time.sleep(2)
        except:
            submitLogin = driver.find_element(By.XPATH,'//div[@data-test-id="registerFormSubmitButton"]/button[@type="submit"]')
            submitLogin.click()
            time.sleep(2)

    def post_process(self,driver):
        image = self.image
        title_text = self.inputText
        try:
            creatbtn = driver.find_element(By.XPATH,'//div[@data-test-id="addPinButton"]')
            time.sleep(2)
            creatbtn.click()
            time.sleep(3)
        except:
            creatbtn = driver.find_element(By.XPATH,'//div[@data-test-id="addPinButton"]')
            time.sleep(2)
            creatbtn.click()
            time.sleep(3)
        time.sleep(8)
        try:
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/bmp,image/jpeg,image/png,image/tiff,image/webp,video/mp4,video/x-m4v,video/quicktime"]')
            time.sleep(3)
            postImage.send_keys(image)
            time.sleep(3)
        except:
            postImage = driver.find_element(By.XPATH,'//input[@accept="image/bmp,image/jpeg,image/png,image/tiff,image/webp,video/mp4,video/x-m4v,video/quicktime"]')
            time.sleep(2)
            time.sleep(2)
            postImage.send_keys(image)
            time.sleep(3)
        try:
            publish_button = driver.find_element(By.XPATH,'//div[text()="Publish"]')
            time.sleep(2)
            publish_button.click()
            time.sleep(10)
        except:
            publish_button = driver.find_element(By.XPATH,'//div[text()="Publish"]')
            time.sleep(2)
            publish_button.click()
            time.sleep(10)

        time.sleep(2)
        print(f'[INFO] {image} Posted Successfully')
        time.sleep(3)
        driver.get('https://www.pinterest.com/')
        time.sleep(2)
        
    def run(self):
        driver = self.openBrowser()
        driver.get('https://www.pinterest.com/')
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

    beenVerified = Pinterest_Auto_Posts(args)
    driver = beenVerified.run()

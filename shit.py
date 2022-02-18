from ast import If
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import regex as re
import requests
import html
from random import choice
import threading
username=input("Your Username: ")
password=input("Your Password: ")
options=Options()
options.headless = True
options.add_argument("--log-level=0")
driver=webdriver.Firefox(options=options)
def jokerquote():
    r=requests.get("https://everydaypower.com/joker-quotes/")
    matches=re.findall('(?<=“)([^”]*)',r.text)
    return choice(matches)
def driverreload(driver):
    while(True):
        driver.refresh()
        sleep(10)

driver.get("https://instagram.com")
while True:
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        print("logged in")
        break
    except Exception as e:
        pass
    sleep(0.2)
while(driver.current_url!="https://www.instagram.com/accounts/onetap/?next=%2F"):
    sleep(0.1)
driver.get("https://www.instagram.com/direct/inbox/")
while True:
    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()
        sleep(0.1)
        break
        
    except Exception as e:
        pass
i=0
threading.Thread(target=driverreload,args=(driver,))
while True:
    for x in range(10):
        try:
            driver.find_element(By.XPATH, f"/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{x}]/a/div/div[3]/div").click()
            sleep(0.2)
            driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(html.unescape(jokerquote()))
            driver.find_element(By.XPATH, "//button[contains(text(),'Send')]").click()
            test=driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div').text
            print(f"message sent to: {test}")
            driver.execute_script("window.history.go(-1)")
            sleep(0.2)
        except Exception as e:
            pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

PATH = "C:\WebDriver\chromedriver.exe"

print(Fore.GREEN + """    . . .
              \|/
            `--+--'
              /|\
             ' | '
               |
               |
           ,--'#`--.
           |#######|
        _.-'#######`-._
     ,-'###############`-.
   ,'#####################`,
  /#########################\
 |###########################|
|#############################|
|#############################|
|#############################|
|#############################|
 |###########################|
  \#########################/
   `.#####################,'
     `._###############_,'
        `--..#####..--'""")

print(" ")
#print(Fore.MAGENTA  + """ ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄  
#█   █   █ ▐  ▄▀   ▐ ▐ ▄▀   █ █      █ █  █ ▀  █ ▐ ▄▀   █ 
#▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄▀  █      █ ▐  █    █   █▄▄▄▀  
 #▄▀    █    █    ▌    █   █  ▀▄    ▄▀   █    █    █   █  
#█     █    ▄▀▄▄▄▄    ▄▀▄▄▄▀    ▀▀▀▀   ▄▀   ▄▀    ▄▀▄▄▄▀  
#▐     ▐    █    ▐   █    ▐            █    █    █    ▐   
 #          ▐        ▐                 ▐    ▐    ▐        """)        
print(" ")

x = input('Full TikTok URL Here: ')

s = Service("C:\WebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(x)
print(driver.title)

time.sleep(2)
element_reportproblem = driver.find_element_by_xpath('//*[@id="tiktok-verify-ele"]/div/div[4]/div/a[2]/span[2]')
element_reportproblem.click()
time.sleep(2)

element_refreshing = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[2]/div')
element_refreshing.click()
time.sleep(2)

element_submit = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/span')
element_submit.click()


while True:
    time.sleep(2)
    element_moreactions = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]')
    element_moreactions.click()
    time.sleep(2)
    element_report = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div[1]/div/div/div')
    element_report.click()

    time.sleep(2)
    element_reportaccount = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[2]/div/label[1]/span[1]/i')
    element_reportaccount.click()
    time.sleep(2)
    element_next = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[3]/button[2]')
    element_next.click()
    time.sleep(2)

    element_PIC = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[2]/div/label[1]/span[1]')
    element_PIC.click()
    time.sleep(2)
    element_next2 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[3]/button[2]')
    element_next2.click()
    time.sleep(2)

    element_HOB = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[2]/div/label[6]/span[1]/i')
    element_HOB.click()
    time.sleep(2)
    element_next3 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[3]/button[2]')
    element_next3.click()
    time.sleep(2)

    element_someoneiknow = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[2]/div/label[2]/span[1]/i')
    element_someoneiknow.click()
    time.sleep(2)
    element_submit = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/header/div[3]/div/div/div[2]/form/div[3]/button[2]')
    element_submit.click()    
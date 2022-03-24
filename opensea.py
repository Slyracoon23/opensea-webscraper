import PySimpleGUI as sg
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import re
import time
import os
import shutil
import xlwt
from xlwt import Workbook
# wb = Workbook()
# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')



# event, values = sg.Window('Scraper Bot',
#                   [[sg.T('Enter your URL'), sg.In(key='-ID-')],
#                   [sg.T('Enter your Path which is empty'), sg.In(key='-ID-1')],
#                   [sg.T('Enter your where file to be downloaded'), sg.In(key='-ID-2')],
#                   [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

# url = values['-ID-']
# destination=values['-ID-1']
# destination1=values['-ID-2']

PATH = "/home/slyracoon23/Downloads/geckodriver"
# path2 = destination
# options = webdriver.FirefoxOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--disable-user-media-security=true")
# options.add_argument("--use-fake-ui-for-media-stream")
# options.add_argument("--disable-popup-blocking")
# prefs = {"download.default_directory" : path2}
# options.add_experimental_option("prefs",prefs)
# driver = webdriver.Firefox(PATH, options=options)

profile_path = '/home/slyracoon23/.mozilla/firefox/z2gigiuf.default'
options=Options()
options.set_preference('profile', profile_path)

service = Service(PATH)
driver = Firefox(service=service, options=options)

# action = ActionChains(driver)

# Opening Website

# driver.get("https://opensea.io/collection/boredapeyachtclub")
# driver.get("https://opensea.io/collection/bored-ape-kennel-club?search[sortAscending]=true&search[sortBy]=PRICE")
driver.get("https://opensea.io/Slyracoon23")
# driver.maximize_window()
time.sleep(5)



# #Getting Artist Name

# Artist_name = driver.find_element_by_class_name("AccountLinkreact__DivContainer-sc-4gdciy-0").get_attribute('textContent')
# Artist_name= Artist_name.split(" ")
# Artist_name=Artist_name[2]

# XPATH: /html/body/div[1]/div/main/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div

# grid = driver.find_element_by_xpath(" /html/body/div[1]/div/main/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div")

while True:
    gridcells = driver.find_elements(By.XPATH, "//div[@role='gridcell']")


    for gridcell in gridcells:

        nft_info = (gridcell.text).splitlines()

        nft_type, tokenId, orderSide, price, *_ = nft_info

        print(nft_type, tokenId, orderSide, price, sep=",")

        # driver.execute_script("window.scrollTo(0, 250);")
    




    webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)

    scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
    clientHeight = driver.execute_script("return document.documentElement.clientHeight")
    scrollTop = driver.execute_script("return document.documentElement.scrollTop")

 
    print(scrollHeight, clientHeight, scrollTop, sep=',')

    if abs(scrollHeight - clientHeight - scrollTop) < 1:
        break

    time.sleep(8)






# #Making Folder for Downloading Images
# path = destination1+str(Artist_name)
# os.mkdir(path)



# #Getting other necessary Data

# Owner_Number = driver.find_element_by_class_name("item--ownership-count").get_attribute('textContent')
# Owner_Number = int(re.search(r'\d+', Owner_Number).group())

# Verfication_Status = driver.find_element_by_class_name("CollectionVerificationStatus--link").get_attribute('textContent')

# issue = Verfication_Status.split(' ')
# issue = issue[2:]

# Title = driver.find_element_by_class_name("item--title").get_attribute('textContent')

# Number_Quantity = driver.find_element_by_class_name("item--counts").get_attribute('textContent')
# Number_Quantity = re.findall('\d+', Number_Quantity)
# Number_Quantity = Number_Quantity[1]

# Product_Description = driver.find_elements_by_tag_name("p")
# Product_Description = Product_Description[0].get_attribute('textContent')

# chain = driver.find_elements_by_class_name("ChainInfo--label-value")
# chain = chain[1:]

# TokenID = chain[0].get_attribute('textContent')

# BlockChain = chain[1].get_attribute('textContent')

# #Main image url
# data1= driver.find_element_by_class_name("item--summary")
# imageurl= data1.find_element_by_class_name("Image--image").get_attribute('src')

# #Getting address

# data1 =driver.find_element_by_class_name("ChainInfo--label-value")
# driver.get(data1.find_element_by_tag_name('a').get_attribute('href'))
# time.sleep(3)
# address = driver.find_element_by_id("mainaddress").text
# content = driver.find_element_by_id("ContentPlaceHolder1_trContract")
# content1 = content.find_element_by_class_name("hash-tag").text

# #Getting Profile Picture

# driver.get("https://opensea.io/accounts/"+str(Artist_name))
# time.sleep(5)
# data2 = driver.find_element_by_class_name("ProfileImage--image")
# Imageurl2 = data2.find_element_by_class_name("Image--image").get_attribute('src')

# #Downlaoding High Res Image

# driver.get("https://imagecyborg.com/")
# time.sleep(3)
# url1 = driver.find_element_by_class_name("url-input").click()
# pyautogui.write(imageurl, interval=0.01)
# driver.find_element_by_class_name("download").click()
# time.sleep(20)
# driver.find_element_by_class_name("download").click()

# #Downloading Profile Picture

# driver.get("https://imagecyborg.com/")
# time.sleep(3)
# url1 = driver.find_element_by_class_name("url-input").click()
# pyautogui.write(Imageurl2, interval=0.01)
# driver.find_element_by_class_name("download").click()
# time.sleep(20)
# driver.find_element_by_class_name("download").click()
# time.sleep(5)
# src_files = os.listdir(path2)
# for file_name in src_files:
#     full_file_name = os.path.join(path2, file_name)
#     if os.path.isfile(full_file_name):
#         shutil.copy(full_file_name, path)

# sheet1.write(0,0,'URL')
# sheet1.write(0,1,'Collection Verification Status')
# sheet1.write(0,2,'Art Title')
# sheet1.write(0,3,'Artist Name')
# sheet1.write(0,4,'Artist Profile URL')
# sheet1.write(0,5,'# of Owners')
# sheet1.write(0,6,'# of Quanity')
# sheet1.write(0,7,'Detail Description')
# sheet1.write(0,8,'Issue')
# sheet1.write(0,9,'Chain Info Contract Address')
# sheet1.write(0,10,'Chain Info Token ID')
# sheet1.write(0,11,'Chain Info Blockchain')
# sheet1.write(0,12,'Creator Address')

# sheet1.write(1,0,url)
# sheet1.write(1,1,Verfication_Status)
# sheet1.write(1,2,Title)
# sheet1.write(1,3,Artist_name)
# sheet1.write(1,4,"https://opensea.io/accounts/"+str(Artist_name))
# sheet1.write(1,5,Owner_Number)
# sheet1.write(1,6,Number_Quantity)
# sheet1.write(1,7,Product_Description)
# sheet1.write(1,8,issue)
# sheet1.write(1,9,address)
# sheet1.write(1,10,TokenID)
# sheet1.write(1,11,BlockChain)
# sheet1.write(1,12,content1)

# wb.save('xlwt example.xls')
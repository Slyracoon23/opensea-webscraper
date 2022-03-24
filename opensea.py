import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import csv
import time
import sys

# Add PATH to your geckodriver when using firefox
PATH = "/home/slyracoon23/Downloads/geckodriver"

# Options for your Selenium webDriver
profile_path = '/home/slyracoon23/.mozilla/firefox/z2gigiuf.default'
options=Options()
options.set_preference('profile', profile_path)

# Instante Service and Driver
service = Service(PATH)
driver = Firefox(service=service, options=options)

# Get webpage
driver.get(sys.argv[1])
driver.maximize_window()
time.sleep(5)


# Save NFT-csv info
NFT_info = set()


while True:
    gridcells = driver.find_elements(By.XPATH, "//div[@role='gridcell']")


    for gridcell in gridcells:

        nft_info = (gridcell.text).splitlines()

        nft_type, tokenId, orderSide, price, *_ = nft_info

        print(nft_type, tokenId, orderSide, price, sep=",")


        # Save info into SET
        NFT_info.add((nft_type, tokenId, orderSide, price))

    


    # Scroll Down
    webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
    # Calculate how far you scrolled
    scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
    clientHeight = driver.execute_script("return document.documentElement.clientHeight")
    scrollTop = driver.execute_script("return document.documentElement.scrollTop")

 
    print(scrollHeight, clientHeight, scrollTop, sep=',')
    
    # Check if you reached the buttom of page
    if abs(scrollHeight - clientHeight - scrollTop) < 1:
        break

    time.sleep(8)

# Write output to CSV file
with open(f'{list(NFT_info)[0][0]}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(list(NFT_info))

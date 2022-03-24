import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from concurrent import futures
import csv
import time
import sys

# Add PATH to your geckodriver when using firefox
# PATH = "/home/slyracoon23/Downloads/geckodriver"

# # Options for your Selenium webDriver
# profile_path = '/home/slyracoon23/.mozilla/firefox/z2gigiuf.default'
# options=Options()
# # options.headless = True
# options.set_preference('profile', profile_path)


# # Instante Service and Driver
# service = Service(PATH)
# driver = Firefox(service=service, options=options)

# Get webpage
# driver.get(sys.argv[1])
# driver.maximize_window()
# time.sleep(5)


# Save NFT-csv info
url = sys.argv[1]


def query_webpage(tokenID):
    result = ()
    try:
        PATH = "/home/slyracoon23/Downloads/geckodriver"

        # Options for your Selenium webDriver
        profile_path = '/home/slyracoon23/.mozilla/firefox/z2gigiuf.default'
        options=Options()
        options.headless = True
        options.set_preference('profile', profile_path)


        # Instante Service and Driver
        service = Service(PATH)

        driver = Firefox(service=service, options=options)
        driver.get(url + str(tokenID))
        driver.maximize_window()
        time.sleep(5)
        # webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(3)

        gridcells = driver.find_elements(By.XPATH, "//div[@role='gridcell']")

        nft_info = (gridcells[0].text).splitlines()

        nft_type, tokenId, orderSide, price, *_ = nft_info

        print(nft_type, tokenId, orderSide, price, sep=",")

        result = (nft_type, tokenId, orderSide, price)

    except Exception as e:
        print(f'TokenID {tokenID} not queried')
        print(e)
        # time.sleep(5)
        # result = query_webpage(tokenID)
        result = tuple([f'FAILED: TokenID: {tokenID}'])



      
    # Save info into SET
    finally:
        driver.quit()
        return result




    
if __name__ == "__main__":

    NFT_info = set()

    tokenIDs = list(range(0,int(sys.argv[2])))

    # Write output to CSV file
    with futures.ThreadPoolExecutor() as executor:
        data = list(executor.map(query_webpage, tokenIDs ))




    with open(f'{data[0][0]}.csv', 'w') as f:

        writer = csv.writer(f)
        
        writer.writerows(data)

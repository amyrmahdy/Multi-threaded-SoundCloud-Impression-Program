from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def playing(url,views=100,seconds=30):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    driver = webdriver.Chrome(options=option, executable_path = "./chromedriver")
    driver.get(url)
    #ACCEPT BUTTON
    accept = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    accept.click()
    for _ in range(views):
        try:
            #REFRESH
            driver.get(url)
            #MUTE BUTTON
            mute = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/section/div/div[3]/div[5]/div/div[2]/button"))
            )
            mute.click()
            #PLAY BUTTOn
            # play = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.CLASS_NAME, "sc-button-play.playButton.sc-button.m-stretch"))
            # )
            # play.click()
            time.sleep(seconds)

        except:
            print("error")
            # driver.quit()
            # driver = webdriver.Chrome(options=option, executable_path = "../chromedriver")

    driver.quit()

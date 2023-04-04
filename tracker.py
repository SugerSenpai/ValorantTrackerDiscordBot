from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

url = "https://tracker.gg/valorant/profile/riot/"


def getTrackerScore(valorantName: str, valorantTag: str):
    accountUrl = ""
    accountUrl = url + valorantName + '%23' + valorantTag + '/overview'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(accountUrl)
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]"))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Page could not be loaded")
    element = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]')
    element.screenshot(valorantName.lower()+valorantTag.lower()+'.png')


def refreshTrackerScore(valorantName: str, valorantTag: str):
    accountUrl = ""
    accountUrl = url + valorantName + '%23' + valorantTag + '/overview'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(accountUrl)
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/main/div[1]/div/div/div[2]"))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Page could not be loaded")
    refresh = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/main/div[1]/div/div/div[2]')
    ActionChains(driver).move_to_element(refresh).click(refresh).perform()
    driver.quit
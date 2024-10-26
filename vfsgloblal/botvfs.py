import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

vfs_global_urls="https://visa.vfsglobal.com/arg/en/can"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()


driver.get(vfs_global_urls)

try:
    data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div/div[2]/div/div[1]/div/a/span')))
    data.click()
    time.sleep(2)
    scroll_y_coordinate = 1700
    driver.execute_script(f"window.scrollTo(0, {scroll_y_coordinate});")
    data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')))
    data.click()
    data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__39"]/p/div[9]/div/div[1]/p')))
    x=data.text
    print(x)


    time.sleep(10)
except:
    print("Program has failed to proceed")
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('chromedriver.exe')
service.start()
driver = webdriver.Chrome(service=service)
driver.get("https://forms.gle/ueXgvWTQRxAb56St7")

def fill_form(email, nrp, nama, jk, usia, alamat):
    inputs = driver.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
    radiobuttons = driver.find_element(By.CLASS_NAME, "Od2TWd.hYsg7c")

    time.sleep(1)

    inputs_array = [ 
        email, nrp, nama, usia, alamat
    ]

    for i in range(len(inputs)):
        inputs[i].clear()
        inputs[i].send_keys(inputs_array[i])

    for radio in radiobuttons:
        if radio.get_attribute("data-value").lower() == jk:
            radio.click()

    bt_next = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    bt_next.click()

fill_form("tanzilu@mail.com","123412","Tanzilu","Pria","28","Malang")

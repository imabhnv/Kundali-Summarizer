
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException

import time
import os

def getInfo(name, gender, hr, min, sec, day, month, year, place):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.astrosage.com/")

    try:
        driver.execute_script("""
            let popup = document.querySelector('.offer-free');
            if (popup) { popup.remove(); }
        """)
    except Exception:
        pass

    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys(name)

    if gender == 'male':
        driver.find_element(By.XPATH, '//*[@id="sex"]/option[1]').click()
    else:
        driver.find_element(By.XPATH, '//*[@id="sex"]/option[2]').click()

    driver.find_element(By.ID, "Day").clear()
    driver.find_element(By.ID, "Day").send_keys(day)

    driver.find_element(By.ID, "Month").clear()
    driver.find_element(By.ID, "Month").send_keys(month)

    driver.find_element(By.ID, "Year").clear()
    driver.find_element(By.ID, "Year").send_keys(year)

    driver.find_element(By.ID, "hrs").clear()
    driver.find_element(By.ID, "hrs").send_keys(hr)

    driver.find_element(By.ID, "min").clear()
    driver.find_element(By.ID, "min").send_keys(min)

    driver.find_element(By.ID, "sec").clear()
    driver.find_element(By.ID, "sec").send_keys(sec)

    place_input = driver.find_element(By.ID, "place")
    place_input.clear()
    place_input.send_keys(place)
    time.sleep(3)
    place_input.send_keys(Keys.ARROW_DOWN)
    place_input.send_keys(Keys.ENTER)

    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/form/div[7]/button").click()

    def safe_click(driver, element):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            driver.execute_script("arguments[0].click();", element)

    base = "/tmp"

    charts = {
        "birth_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[1]/a/div/div/h6[1]", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]"),
        "mangaldosh_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[8]/a/div/div/h6[1]", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div"),
        "kalsapradosh_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[17]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[3]/div/div"),
        "dasha_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[18]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div"),
        "ascendant_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[10]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div"),
        "career_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[20]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div"),
        "today_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[14]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div"),
        "numerology_chart": ("/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[23]/a/div/div/p", "/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[1]")
    }

    paths = {}
    for key, (click_xpath, shot_xpath) in charts.items():
        try:
            btn = driver.find_element(By.XPATH, click_xpath)
            safe_click(driver, btn)
            time.sleep(2)
            path = f"{base}/{key}.png"
            driver.find_element(By.XPATH, shot_xpath).screenshot(path)
            paths[key] = path
            driver.back()
        except NoSuchElementException:
            paths[key] = None

    driver.quit()
    return paths

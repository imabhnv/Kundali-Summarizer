from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException

import time

def getInfo(name, gender, hr, min, sec, day, month, year, place):
    options = Options()
    options.add_argument('--headless')       # ✅ Important
    options.add_argument('--disable-gpu')    # ✅ Extra stability

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options)

    driver.maximize_window()
    driver.get("https://www.astrosage.com/")

    try:
        driver.execute_script("""
            let popup = document.querySelector('.offer-free');
            if (popup) { popup.remove(); console.log("⚠️ Popup removed using JavaScript."); }
        """)
    except Exception as e:
        print("Popup JS Error:", e)

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
    submit_btn = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/form/div[7]/button")
    submit_btn.click()

    # 🔁 Helper for safe click
    def safe_click(driver, element):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            driver.execute_script("arguments[0].click();", element)

    time.sleep(1)
    try:
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[1]/a/div/div/h6[1]")
        safe_click(driver, nxt_btn)
        birth_chart_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Birth_chart.png"
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]").screenshot(birth_chart_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Birth chart button not found.")
        return driver

    time.sleep(2)
    try:
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[8]/a/div/div/h6[1]")
        mangal_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Mangaldosh_chart.png"
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div").screenshot(mangal_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Mangal Dosha button not found.")
        return driver
    
    time.sleep(2)
    try:
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[17]/a/div/div/p")
        safe_click(driver, nxt_btn)
        kalsarpdosh_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/KalSarpaDosh_chart.png"
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[3]/div/div").screenshot(kalsarpdosh_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Kal Sarpa Dosh button not found.")
        return driver
    
    time.sleep(2)
    try:
        dasha_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Dasha_chart.png"
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[18]/a/div/div/p")
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div").screenshot(dasha_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Dasha phal button not found.")
        return driver
    
    time.sleep(2)
    try:
        ascendant_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Ascendant.png"
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[10]/a/div/div/p")
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div").screenshot(ascendant_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Ascendant button not found.")
        return driver   
    
    time.sleep(2)
    try:
        career_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Career.png"
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[20]/a/div/div/p")
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div").screenshot(career_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Nature button not found.")
        return driver       
    
    time.sleep(2)
    try:
        today_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Today_chart.png"
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[14]/a/div/div/p")
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[2]/div/div").screenshot(today_path)
        driver.back()
    except NoSuchElementException:
        print("❌ Today button not found.")
        return driver       
    
    time.sleep(2)
    try:
        numerology_path = "D:/PROGRAMMING LANGUAGES/PYTHON/JyotishAI/Numerology_chart.png"
        nxt_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div/div[5]/div[1]/div/div[1]/div[23]/a/div/div/p")
        safe_click(driver, nxt_btn)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div/div[5]/div[1]/div[1]/div[1]").screenshot(numerology_path)
        driver.quit()
    except NoSuchElementException:
        print("❌ Numerology button not found.")
        return driver   
    
    return {
        "birth_chart": birth_chart_path,
        "mangaldosh_chart": mangal_path,
        "kalsapradosh_chart": kalsarpdosh_path,
        "dasha_chart": dasha_path,
        "ascendant_chart":ascendant_path,
        "career_chart": career_path,
        "today_chart":today_path,
        "numerology_chart":numerology_path
    }

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


URL = "https://www.catchtiger.com/en/domain-auctions"

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def app() -> None:
    chrome_options = set_chrome_options()
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1024, 768)
        driver.get(URL)

        time.sleep(10)

        e = driver.find_element_by_xpath('//input[@id="type-nl"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-be"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-eu"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-de"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-fr"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-ch"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-it"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        e = driver.find_element_by_xpath('//input[@id="type-li"]')
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()

        time.sleep(15)

        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

        time.sleep(2)

        a = driver.find_element_by_xpath('//div[@class="nr-results"]//a[text()="500"]')
        a.click()

        time.sleep(15)

        print(driver.page_source)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    app()

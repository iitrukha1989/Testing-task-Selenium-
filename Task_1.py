from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def yandex_Search(url_Value, site_Value):
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url_Value)

    search_Box = driver.find_element(By.XPATH, '//*[@id="text"]')
    search_Box.clear()
    search_Box.send_keys('Тензор')
    locator = (By.CSS_SELECTOR, '#text')
    search_Box = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(locator))
    time.sleep(2)
    assert search_Box
    search_Box.send_keys(Keys.RETURN)
    assert 'Тензор' in driver.page_source

    search_Word = driver.find_elements(By.CSS_SELECTOR,
                                       '#search-result > .serp-item a.link > b')
    value_Search = [elem.text.strip() for elem in search_Word[:5]]
    assert 'tensor.ru' in value_Search

    time.sleep(2)
    driver.close()
    driver.quit()


# url_Value = "https://www.yandex.ru/"
# site_Value = 'tensor.ru'
# yandex_Search(url_Value, site_Value)

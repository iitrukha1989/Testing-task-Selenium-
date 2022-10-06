from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time


def yandex_Image(url_Value):
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url_Value)

    image_Page = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[1]/nav/div/ul/li[3]/a/div[1]')
    image_Page.click()
    driver.switch_to.window(driver.window_handles[1])
    image_Page = driver.find_elements_by_xpath(
        "//div[@data-grid-name='im']")
    image_Page[0].click()
    assert "https://yandex.ru/images/" in driver.current_url
    time.sleep(2)
    image_Page = driver.find_elements_by_xpath("//div[@role='listitem']")
    image_Page[0].click()
    time.sleep(2)

    images_Value_1 = driver.find_elements_by_tag_name('img')
    tmp_Value = images_Value_1[1].get_attribute('src')
    ActionChains(driver).send_keys(Keys.RIGHT).perform()
    time.sleep(2)
    ActionChains(driver).send_keys(Keys.LEFT).perform()
    images_Value_2 = driver.find_elements_by_tag_name('img')
    assert tmp_Value == images_Value_2[1].get_attribute('src')

    time.sleep(2)
    driver.close()
    driver.quit()


# url_Value = "https://www.yandex.ru/"
# yandex_Image(url_Value)


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('https://www.litres.ru/')
time.sleep(3)
input = driver.find_element(By.XPATH, "//div[@class='SearchForm_searchFormWrapperAB__Nn4lQ']/input[@class='SearchForm_input__qDTKP']")
input.send_keys("стивен кинг оно")
input.send_keys(Keys.ENTER)
time.sleep(3)
list_book = []
while True:

    while True:
        wait = WebDriverWait(driver, 10)
        books = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='Art_content__ituUa Art_content_full___CBpM']")))
        forward = ''
        count = len(books)
        driver.execute_script("window.scrollBy(0, 4000)")
        time.sleep(3)
        books = driver.find_elements(By.XPATH, "//div[@class='Art_content__ituUa Art_content_full___CBpM']")
        if len(books) == count:
            break

    for book in books:
        name = book.find_element(By.CLASS_NAME, "ArtInfo_title__h_5Ay").text
        # price = book.find_element(By.CLASS_NAME, "ArtPrice_finalPrice__sFS_4").text
        author = book.find_element(By.CLASS_NAME, "ArtPersons_row__yX2gU").text
        url = book.find_element(By.XPATH, "./div/a").get_attribute('href')
        list_book.append({'name': name, 'author': author, 'url': url})
    forwards = driver.find_elements(By.XPATH, "//div[@class='PaginatedContent_pages__B9Lnu']/div[@class='PaginatedContent_paginator___2ugs']/ul[@class='Paginator_container__XXcz8']/li[@class='Paginator_arrow__SAzJS']/a")
    buttons = driver.find_elements(By.XPATH,"//div[@class='PaginatedContent_pages__B9Lnu']/div[@class='PaginatedContent_paginator___2ugs']/ul[@class='Paginator_container__XXcz8']/li[@class='Paginator_arrow__SAzJS']")
    print(forwards)
    print(len(buttons))
    if len(buttons) == 1:
        button = driver.find_element(By.XPATH,"//div[@class='PaginatedContent_pages__B9Lnu']/div[@class='PaginatedContent_paginator___2ugs']/ul[@class='Paginator_container__XXcz8']/li[@class='Paginator_arrow__SAzJS']")
        button.click()
    if len(buttons) == 2 and forwards[1].get_attribute('aria-disabled') == 'false':
        print(forwards[1].text)
        buttons[1].click()
    if len(buttons) == 1 and forwards[0].get_attribute('aria-label') == 'Назад':

        break





print(list_book)

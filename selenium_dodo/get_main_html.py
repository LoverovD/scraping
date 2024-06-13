import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# with open('C:/learning/scraping/selenium/delete_main.html', 'w') as file:
#     file.write(driver.page_source)


def get_data(url, t: int = 10):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) '
                                                         'Gecko/20100101 Firefox/126.0')
    service = webdriver.FirefoxService(executable_path="C:\\learning\\scraping\\selenium\\geckodriver-v0.34.0-win64"
                                                       "\\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)
    large = driver.find_element_by_xpath(By.XPATH, "//label[@data-testid='menu__pizza_size_Большая']")
    time.sleep(30)

    try:
        soup = BeautifulSoup(driver.page_source, "lxml")
        card = soup.find('div', class_="sc-1cyl9gi-0 euyXjR show").find('div', class_="popup-padding") \
            .find('div', class_="popup-inner undefined").find('div', class_="sc-1r4m23d-0 dMRDbG")
        main_block = card.find('div', class_="sc-1r4m23d-8 BudjO").find('div', class_="scroll__view") \
            .find('div', class_="sc-1r4m23d-9 gOJzYh")

        action.click(large)
        # driver.get(url)
        # time.sleep(10)
        # print('1')
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(10)


    # with open('C:/learning/scraping/selenium/delete_main.html', 'w') as file:
    #     file.write(driver.page_source)
    # soup = BeautifulSoup(driver.page_source)
    finally:
        driver.close()
        driver.quit()
    # print(soup)


def main():
    get_data('https://dodopizza.by/minsk/product/Adgika')


if __name__ == '__main__':
    main()

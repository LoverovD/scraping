from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from transliterate import translit
import requests
import time
import os


def create_pizza_directory(links, path, section_name):
    buttons = [
        ["/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/label[2]",
         "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/label[1]"],
        ["/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/label[2]",
         "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/label[2]"],

        ["/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/label[3]",
         "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/label[1]"],
        ["/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/label[3]",
         "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/label[2]"],

        ["/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/label[1]",
         "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/label[1]"]

    ]
    os.makedirs(f'C:\\learning\\scraping\\selenium\\pages\\{section_name}', exist_ok=True)
    for url in links:
        html_name = ['regular', 'regular_thin', 'large', 'large_thin', 'small']
        pizza_name = url.strip().split('/')[-1].replace('-', '_')
        os.makedirs(f'C:\\learning\\scraping\\selenium\\pages\\{section_name}\\{pizza_name}', exist_ok=True)

        options = webdriver.FirefoxOptions()
        options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) '
                                                             'Gecko/20100101 Firefox/126.0')
        service = webdriver.FirefoxService(executable_path="C:\\learning\\scraping\\selenium\\geckodriver-v0.34.0-win64"
                                                           "\\geckodriver.exe")
        driver = webdriver.Firefox(service=service, options=options)

        for but in buttons:
            try:
                driver.get(url=url)
                time.sleep(10)

                size_button = driver.find_element(By.XPATH, but[0]).click()
                time.sleep(3)
                thickness_button = driver.find_element(By.XPATH, but[1]).click()
                time.sleep(3)
                info_button = driver.find_element(By.XPATH, path).click()
                time.sleep(3)

                with open(f'C:/learning/scraping/selenium/pages/{section_name}/{pizza_name}/{html_name.pop(0)}.html',
                          'w') as file:
                    file.write(driver.page_source)

            except Exception as e:
                print(e)
        driver.close()
        driver.quit()


def main():
    links = [
        "https://dodopizza.by/minsk/product/Adgika",
        "https://dodopizza.by/minsk/product/country-pizza",
        "https://dodopizza.by/minsk/product/carbonara"
    ]

    path = "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/button"

    create_pizza_directory(links=links, path=path, section_name='pizza')


if __name__ == '__main__':
    main()


# headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
#     }
#
# with open('C:/learning/scraping/selenium/button.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# card = soup.find('div', class_="sc-1cyl9gi-0 euyXjR show").find('div', class_="popup-padding")\
#     .find('div', class_="popup-inner undefined").find('div', class_="sc-1r4m23d-0 dMRDbG")
# main_block = card.find('div', class_="sc-1r4m23d-8 BudjO").find('div', class_="scroll__view")\
#     .find('div', class_="sc-1r4m23d-9 gOJzYh")
#
# name = main_block.find('div', class_="sc-1r4m23d-10 cqGCBA").find('h1').text
# compound_list = main_block.find('div', class_="sc-1r4m23d-15 jxYrMP").text.strip().split(", ")
# compound = []
# for comp in compound_list:
#     compound.append(comp.rstrip("\xa0"))
# ###
# size_list = main_block.find('div', class_="sc-1r4m23d-13 gqjzdF").find('span').text.strip().split(', ')
# size = []
# for s in size_list:
#     size.append(s.rstrip("\xa0").strip())
# price = card.find('div', class_="sc-1r4m23d-7 dlYEuz").find('div', class_="sc-1r4m23d-17 fvLrvW"). \
#     find('span').text.strip()
#
# poor_quality_url = card.find('div', class_="sc-1r4m23d-1 giHWeV").find('div', class_="sc-1r4m23d-2 kUZMOh"). \
#     find('img').get('src').split('/')
# picture_url = "https://media.dodostatic.net/image/r:1875x1875/" + poor_quality_url[-1].replace('.jpg', '.png')
# picture = requests.get(picture_url, headers=headers)
# out = open(f"pictures\\{translit(name, reversed=True).replace(' ', '_')}.png", 'wb')
# out.write(picture.content)
# out.close()
# ###
# nutritional_sections = main_block.find('div', class_="sc-1r4m23d-10 cqGCBA").find('div', class_="sc-13bk731-1 bMzoXT"). \
#     find('div').find('div', class_="sc-6k321-0 dEgNfL sc-13bk731-2 dblGKH tooltip").find_all('section')
#
# nutritional_value = {
#     "energy_value": nutritional_sections[0].find('div').find_next_sibling().text.strip(),
#     "squirrels": nutritional_sections[1].find('div').find_next_sibling().text.strip(),
#     "fats": nutritional_sections[2].find('div').find_next_sibling().text.strip(),
#     "carbohydrates": nutritional_sections[3].find('div').find_next_sibling().text.strip()
# }
#
# product_info = {
#     "name": name,
#     "size": size,
#     "compound": compound,
#     "price": price,
#     "nutritional_value": nutritional_value,
# }
#
# for i in product_info:
#     print(f"{i}: {product_info[i]}")


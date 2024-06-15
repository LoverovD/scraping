from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def get_links(url, flag, missed_links):

    links_list = []
    with open("C:/learning/scraping/selenium/main.html") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find('section', {"id": flag}, class_="sc-1tj5y7k-2 hLTpDK")\
        .find_all('article', class_="sc-1gfzx1o-3 eJrNNZ")
    for article in articles:
        try:
            dirty_link = article.find('div', class_="sc-1gfzx1o-1 fnoJVX").find('a').get('href').split('/')
            link = "https://dodopizza.by/minsk/product/" + dirty_link[3].replace(' ', '%20')
        except AttributeError:
            # link = input(f"\nВведи ссылку на позицию след. за: {links_list[-1]} | ")
            link = missed_links.pop(0)
            continue
        finally:
            links_list.append(link)
    return [links_list, missed_links]


def create_html_directory(links, path, section_name):
    os.makedirs(f'C:\\learning\\scraping\\selenium\\pages\\{section_name}', exist_ok=True)
    for url in links:
        options = webdriver.FirefoxOptions()
        options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) '
                                                             'Gecko/20100101 Firefox/126.0')
        service = webdriver.FirefoxService(
            executable_path="C:\\learning\\scraping\\selenium\\geckodriver-v0.34.0-win64"
                            "\\geckodriver.exe")
        driver = webdriver.Firefox(service=service, options=options)

        try:
            driver.get(url=url)
            html_name = url.strip().split('/')[-1]
            time.sleep(15)

            info_button = driver.find_element(By.XPATH, path).click()
            time.sleep(5)

            with open(f'C:/learning/scraping/selenium/pages/{section_name}/{html_name}.html', 'w') as file:
                file.write(driver.page_source)

        except Exception as e:
            print(f"\nmissed: {url}\n")
            print(e)
        finally:
            driver.close()
            driver.quit()


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
                print(f"\nmissed: {url}\n")
                print(e)
        driver.close()
        driver.quit()


def main():
    missed_links = [
        "https://dodopizza.by/minsk/product/syrnaya-pizza",
        "https://dodopizza.by/minsk/product/fresh-chorizo",
        "https://dodopizza.by/minsk/product/double-chicken",
        "https://dodopizza.by/minsk/product/pizza-margarita",
        "https://dodopizza.by/minsk/product/Diablo",
        "https://dodopizza.by/minsk/product/ovoshi-i-griby",
        "https://dodopizza.by/minsk/product/dodster-spice",
        "https://dodopizza.by/minsk/product/kartoshkamini",
        "https://dodopizza.by/minsk/product/chicken-bytes",
        "https://dodopizza.by/minsk/product/greek-bals",
        "https://dodopizza.by/minsk/product/klassicheskiy-koktejl",
        "https://dodopizza.by/minsk/product/klubnichnyy-kokteyl",
        "https://dodopizza.by/minsk/product/syrniki-malina,"
    ]
    url = "https://dodopizza.by/minsk"
    print(f"\n________\nПИЦЦА...\n")
    path = "/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/button"
    links, missed_links = get_links(url, flag="qooaq", missed_links=missed_links)
    create_pizza_directory(links=links[1:], path=path, section_name='pizza')
    print(f"\n\n__________\nЗАВТРАК...\n")
    links, missed_links = get_links(url, flag="jszkv", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='breakfast')
    print(f"\n\n________\nСОУСЫ...\n")
    links, missed_links = get_links(url, flag="sjcdy", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='sauces')
    # _____________________________________
    print(f"\n\n__________\nЗАКУСКИ...\n")
    path = "/html/body/div[3]/div/div[2]/div/section/main/div/button"
    links, missed_links = get_links(url, flag="gwsxf", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='snacks')
    print(f"\n\n___________\nКОКТЕЙЛИ...\n")
    links, missed_links = get_links(url, flag="kjzvc", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='cocktails')
    print(f"\n\n_______\nКОФЕ...\n")
    links, missed_links = get_links(url, flag="pdkun", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='coffee')
    print(f"\n\n__________\nДЕСЕРТЫ...\n")
    links, missed_links = get_links(url, flag="ykvcn", missed_links=missed_links)
    create_html_directory(links=links, path=path, section_name='dessert')
    # print(f"\n\n__________\nНАПИТКИ...\n")  # без path
    # links, missed_links = get_links(url, flag="pdabk", missed_links=missed_links)
    # create_html_directory(links=links, path=path, section_name='beverages')
    # _____________________________________
    # print(f"\n\n________\nКОМБО...\n")
    # links, missed_links = get_links(url, "xxlrd", path=None, section_name='combo')


if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup


def get_links(url, flag):
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
        "https://dodopizza.by/minsk/product/11ee73e9a52671ba649ed23e04a5c110",
        "https://dodopizza.by/minsk/product/000d3a219740a94c11e8a4c36ff00f82",
        "https://dodopizza.by/minsk/product/000d3a262427a94911e8a4c5db9d41f8",
        "https://dodopizza.by/minsk/product/klassicheskiy-koktejl",
        "https://dodopizza.by/minsk/product/klubnichnyy-kokteyl",
        "https://dodopizza.by/minsk/product/syrniki-malina,"
    ]
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
            link = input(f"\nВведи ссылку на позицию след. за: {links_list[-1]} | ")
            continue
        finally:
            links_list.append(link)
    print(f"\n{links_list}")


def get_combo_links(url):
    pass


def main():
    url = "https://tury.ru/hotel/?cat=1317"
    print(f"\n________\nПИЦЦА...\n")
    get_links(url, "qooaq")
    print(f"\n\n________\nКОМБО...\n")
    get_links(url, "xxlrd")
    print(f"\n\n__________\nЗАВТРАК...\n")
    get_links(url, "jszkv")
    print(f"\n\n__________\nЗАКУСКИ...\n")
    get_links(url, "gwsxf")
    print(f"\n\n__________\nНАПИТКИ...\n")
    get_links(url, "pdabk")
    print(f"\n\n___________\nКОКТЕЙЛИ...\n")
    get_links(url, "kjzvc")
    print(f"\n\n_______\nКОФЕ...\n")
    get_links(url, "pdkun")
    print(f"\n\n__________\nДЕСЕРТЫ...\n")
    get_links(url, "ykvcn")
    print(f"\n\n________\nСОУСЫ...\n")
    get_links(url, "sjcdy")


if __name__ == '__main__':
    main()

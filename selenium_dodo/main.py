from bs4 import BeautifulSoup
# from transliterate import translit
# name = translit(article.find('div', class_="sc-1gfzx1o-1 fnoJVX").find('a').text, reversed=True)
# https://media.dodostatic.net/image/r:1875x1875/11EE7D5EEAB632F58FA9238A2CC13BBB.png


def get_links(url, flag):
    links_list = []
    with open("C:/learning/scraping/selenium/main.html") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find('section', {"id": flag}, class_="sc-1tj5y7k-2 hLTpDK")\
        .find_all('article', class_="sc-1gfzx1o-3 eJrNNZ")
    for article in articles:
        try:
            name = article.find('div', class_="sc-1gfzx1o-1 fnoJVX").find('a').text
            dirty_link = article.find('div', class_="sc-1gfzx1o-1 fnoJVX").find('a').get('href').split('/')
            link = "https://dodopizza.by/minsk/product/" + dirty_link[3].replace(' ', '%20')
        except AttributeError:
            print(f"\nОткрой позицию след. за: | {name} |")
            name = "ПРОШЛОЙ"
            continue
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

from bs4 import BeautifulSoup
from time import time
import requests
import csv


def get_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(end - start)
        return func
    return wrapper


cookies = {
    'PHPSESSID': 'p76sei16lhn7giqck4k049fpd4',
    '_ym_uid': '1717427778739951700',
    '_ym_d': '1717427778',
    'tmr_lvid': '1d5acb970121d629e9cb688b0fd89377',
    'tmr_lvidTS': '1717427778147',
    '_ym_isad': '1',
    '_ga': 'GA1.1.1631016427.1717427778',
    '_ym_visorc': 'w',
    '_ymab_param': 'l0JMswufSPtjMpCoL4sWfcQtM_qUbs4jxbgUWnEpsF44AfTw6SvXvvEnstCZjd6Oj98lyQcXxI-AeAkZWq5NvQI4Piw',
    '_tt_enable_cookie': '1',
    '_ttp': 'rDQBPbCPH9IvMVXhQhzqYLe6CgX',
    'domain_sid': 'EFrvGAJdIxQVxPcXI_5fI%3A1717427779744',
    'tt_deduplication_cookie': 'yandex_product',
    'tt_deduplication_cookie': 'yandex_product',
    'tmr_detect': '1%7C1717427800881',
    '_ga_HJ5N0VQP7V': 'GS1.1.1717427778.1.1.1717427800.38.0.0',
    '_ga_0S3RBN4SQD': 'GS1.1.1717427778.1.1.1717427800.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=p76sei16lhn7giqck4k049fpd4; _ym_uid=1717427778739951700; _ym_d=1717427778;
    # tmr_lvid=1d5acb970121d629e9cb688b0fd89377; tmr_lvidTS=1717427778147; _ym_isad=1; _ga=GA1.1.1631016427.1717427778;
    # _ym_visorc=w; _ymab_param=l0JMswufSPtjMpCoL4sWfcQtM_qUbs4jxbgUWnEpsF44AfTw6SvXvvEnstCZjd6Oj98lyQcXxI-AeAkZWq5NvQI4
    # Piw; _tt_enable_cookie=1; _ttp=rDQBPbCPH9IvMVXhQhzqYLe6CgX; domain_sid=EFrvGAJdIxQVxPcXI_5fI%3A1717427779744; tt_
    # deduplication_cookie=yandex_product; tt_deduplication_cookie=yandex_product; tmr_detect=1%7C1717427800881; _ga_HJ5
    # N0VQP7V=GS1.1.1717427778.1.1.1717427800.38.0.0; _ga_0S3RBN4SQD=GS1.1.1717427778.1.1.1717427800.0.0.0',
    'priority': 'u=0, i',
    'referer': 'https://algo.by/computers_and_networks/parts/videocard.html?utm_source=yandex_product&utm_medium=cpc&ut'
               'm_campaign=test_videocards_yandex_product&utm_content=14286072086&utm_term=---autotargeting&yclid=14776'
               '498081418182655',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 '
                  'Safari/537.36 Edg/125.0.0.0',
}


@get_execution_time
def make_list_of_links():
    list_of_links = []
    for page in range(1, 63):
        print(page)
        params = {
            'utm_source': 'yandex_product',
            'utm_medium': 'cpc',
            'utm_campaign': 'test_videocards_yandex_product',
            'utm_content': '14286072086',
            'utm_term': '---autotargeting',
            'yclid': '14776498081418182655',
            'sort': 'rating',
            'page': f'{page}',
        }

        response = requests.get(
            'https://algo.by/computers_and_networks/parts/videocard.html',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        with open("main.html", 'w') as file1:
            file1.write(response.text)

        with open("main.html") as file1:
            src = file1.read()

        soup = BeautifulSoup(src, "lxml")
        all_products = soup.find(class_="products_list").find_all(class_="product")

        for item in all_products:
            list_of_links.append(item.find(class_="product_image").find('a').get('href'))

    print("Количество ссылок на видеокарты:")
    print(len(list_of_links))
    return list_of_links


all_links = make_list_of_links()

counter = 1
for url in all_links:
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    with open(f"products/page_{counter}.html", 'w') as file:
        file.write(response.text)

    counter += 1

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________

product_parameters_titles = list()
count = 0
while True:
    try:
        with open(f"products/page_{count}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        # Поиск блока ("div", class_="block_title") с Техническими характеристиками

        product_all_title_blocks = soup.find(class_="main_content").find(class_="product_description_content")\
            .find_all("div", class_="block_title")
        for title_index in range(len(product_all_title_blocks)):
            if "Технические характеристики" in product_all_title_blocks[title_index].text:
                index = title_index
                break

        product_content_block = soup.find(class_="main_content").find(class_="product_description_content")\
            .find_all("div", class_="block_content_data")[index]
    except AttributeError:
        pass

    product_parameters_spans = product_content_block.find_all("span")

    # Создание словаря уникальных тех. характеристик для общей таблицы
    for span in product_parameters_spans:
        if span.text.strip() not in product_parameters_titles:
            product_parameters_titles.append(span.text.strip())

    count += 1
    if count == 200:
        count = 0
        break

product_parameters_titles.insert(0, "Название видеокарты")
# Создание таблицы в csv файле и передача туда названий колонок
with open(f"video_card.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(product_parameters_titles)

number_of_parameters = len(product_parameters_titles)

# ______________________________________________________________________________________________________________________

csv_data = []

while True:
    product_parameters_values = [None] * number_of_parameters

    try:
        with open(f"products/page_{count}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        product_name = soup.find(class_="main_content").find(class_="product_header_title")\
            .find("h1").text.strip()
        product_parameters_values[0] = product_name

        # Поиск блока ("div", class_="block_title") с Техническими характеристиками

        product_all_title_blocks = soup.find(class_="main_content").find(class_="product_description_content")\
            .find_all("div", class_="block_title")
        for title_index in range(len(product_all_title_blocks)):
            if "Технические характеристики" in product_all_title_blocks[title_index].text:
                index = title_index
                break

        product_content_block = soup.find(class_="main_content").find(class_="product_description_content")\
            .find_all("div", class_="block_content_data")[index]
    except AttributeError:
        count += 1
        continue

    product_parameters_spans = product_content_block.find_all("span")

    # Правильное заполнение словаря product_parameters_values для передачи его в таблицу
    for index in range(1, number_of_parameters):
        for index_of_span in range(len(product_parameters_spans)):
            if product_parameters_titles[index] == product_parameters_spans[index_of_span].text.strip():
                product_parameters_values[index] = product_parameters_spans[index_of_span].find_next().text.strip()

    with open(f"video_card.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(product_parameters_values)

    count += 1
    if count == 200:
        break

print("video_card.csv заполнен")


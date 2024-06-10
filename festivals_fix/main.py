import requests
from bs4 import BeautifulSoup
import json
import time
import random

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    }


def find_festival_links():
    fest_links = []
    counter = 0

    while True:
        url = f"https://www.skiddle.com/festivals/search/?sort=0&fest_name=&from_date=6%20Jun%202024&to_date=&genre" \
              f"%5B%5D=rock&maxprice=500&o={counter}"

        req = requests.get(url, headers=headers)

        if req.status_code == 404 or counter == 96:
            break
        else:
            print(f"\nПарсинг с {counter+1} фестиваля...")
            counter += 24
            print(f"       до {counter} фестиваля...")

        with open('try.html', 'w') as file:
            file.write(req.text)

        with open('try.html') as file:
            src = file.read()
        #

        try:
            soup = BeautifulSoup(src, 'lxml')
            all_fest_classes = soup.find('div', class_='bg-white').find('div', class_='grid')\
                .find('div', class_='grid__col-md-9 relative').find('div', class_="grid margin-top-10")\
                .find_all('div', class_="margin-bottom-20 grid__col-xs-6 grid__col-md-4 grid--justify-start")
        except Exception as ex:
            print(f"\n{ex}")
            print("Все ссылки собраны.")
            continue

        for fest in all_fest_classes:
            link = "https://www.skiddle.com" + fest.find('a').get('href')
            if link not in fest_links:
                fest_links.append(link)

        time.sleep(random.randrange(2, 4))

    print(f"\n\n{fest_links}\n")
    return fest_links


def create_festivals_json(links):
    json_data = []
    for url in links:

        req = requests.get(url, headers)

        # with open("festivals/1_fest.html", 'w') as file:
        #     file.write(req.text)
        #
        # with open("festivals/1_fest.html") as file:
        #     src = file.read()

        soup = BeautifulSoup(req.content, 'lxml')
        try:
            festival_name = soup.find('div', class_="MuiContainer-root MuiContainer-maxWidthLg css-viy0ph")\
                .find('div', class_="MuiBox-root css-1ofqig9").find('h1').text.strip()
            print(f"\nПарсинг информации о {festival_name}...")

            festival_date_span = soup.find('div', class_="MuiContainer-root MuiContainer-maxWidthLg css-viy0ph")\
                .find('div', class_="MuiBox-root css-1ofqig9").find('div', class_="MuiBox-root css-42ibn8")\
                .find('div', class_="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq")\
                .find('div', class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol").find('span')
            festival_days = festival_date_span.text.strip()
            festival_date = festival_date_span.find_next_sibling().text.strip()

            festival_genre_spans = soup.find('div', class_="MuiContainer-root MuiContainer-maxWidthLg css-viy0ph")\
                .find('div', class_="css-c8xceo").find('div', class_="MuiBox-root css-1excyhs").find_all('span')
            festival_genre = str()
            for genre in festival_genre_spans:
                festival_genre += f"{genre.text.strip()} / "

            festival_description = soup.find('div', class_="MuiContainer-root MuiContainer-maxWidthLg css-viy0ph")\
                .find('div', class_="css-c8xceo").find('div', class_="MuiBox-root css-isgnoj").find('p').text.strip()

            json_data.append(
                {
                    "Название фестиваля": festival_name,
                    "Дни проведения": festival_days,
                    "Дата проведения": festival_date,
                    "Жанры": festival_genre,
                    "Описание": festival_description
                }
            )
        except Exception as ex:
            print(f"\n{ex}")
            print(f"Не вышло спарсить информации о {festival_name}...\nПереходим к следующему\n")
            continue

        time.sleep(random.randrange(2, 4))

    print(f"\n\nЗапись данных в файл...")
    with open("projects_data.json", "a", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
    print(f"\nДанные записаны!")


def main():
    links = find_festival_links()
    print(f"\nВсего ссылок: {len(links)}")
    create_festivals_json(links)


if __name__ == '__main__':
    main()

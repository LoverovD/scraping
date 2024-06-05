import requests
from bs4 import BeautifulSoup
import time
import random
import json


def get_data():
    counter = 0
    projects = []

    while True:
        url = f"https://www.napartner.ru/startups/all/all/Startups/kpr_inverstors/page/{counter}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
        }

        req = requests.get(url, headers=headers)
        if req.status_code == 404 or counter == 9:
            break

        print(f"\n\nПарсинг {counter}-й страницы сайта\n")
        counter += 1

        with open(f"startup_htmls/{counter}_try.html", "w") as file:
            file.write(req.text)

        with open(f"startup_htmls/{counter}_try.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        main_startup_view_classes = soup.find('div', class_='middle').find('div', class_='startup_job')\
            .find('div', class_='all_startups_list').find_all('div', class_='main_startup_view')

        startup_links = []
        for view_class in main_startup_view_classes:
            startup_link = "https://www.napartner.ru/" + view_class.find('div', class_='image').find('div', class_='img')\
                .find('a').get('href')
            startup_links.append(startup_link)

        startup_counter = 1
        for link in startup_links:
            print(f"Парсинг {startup_counter}-й ссылки текущей страницы...")
            req = requests.get(link, headers=headers)

            with open(f"startup_htmls/{startup_counter}_startup.html", 'w') as file:
                file.write(req.text)

            with open(f"startup_htmls/{startup_counter}_startup.html") as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')
            startup_page = soup.find('div', class_='middle').find('div', class_='startup_page')
            startup_info = dict()

            startup_name = startup_page.find('div', class_='top').find('div', class_='center').find('div', class_='name')\
                .find('h1').text.strip()
            startup_info["Заголовок проекта"] = startup_name

            startup_common_info_classes = startup_page.find('div', class_='center').find_all('div', class_='har')
            for info_class in startup_common_info_classes:
                info_element = info_class.text.strip().split(':')
                startup_info[info_element[0]] = info_element[1]

            info_about_startup_div = startup_page.find('div', class_='bottom').find('div', class_='one_block')
            info_about_startup_name = info_about_startup_div.find('div', class_='name').text.strip()
            info_about_startup_text = info_about_startup_div.find('div', class_='text').text.strip().split('\n')
            startup_info[info_about_startup_name] = info_about_startup_text[0]

            startup_counter += 1
            projects.append(startup_info)
            time.sleep(random.randrange(2, 4))

    print(f"\n\nЗапись данных в файл...")
    with open("projects_data.json", "a", encoding="utf-8") as file:
        json.dump(projects, file, indent=4, ensure_ascii=False)
    print(f"\nДанные записаны!")


def main():
    get_data()


if __name__ == "__main__":
    main()

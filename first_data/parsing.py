import requests
from bs4 import BeautifulSoup
import csv

# cookies = {
#     '_ga': 'GA1.2.1916707329.1717342876',
#     '_gid': 'GA1.2.1175940609.1717342876',
#     'default_game_saved': 'Fortnite',
#     '_awl': '2.1717354536.5-7a212b0e4eeb152383358f1e7795159a-6763652d6575726f70652d7765737431-1',
# }
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_ga=GA1.2.1916707329.1717342876; _gid=GA1.2.1175940609.1717342876; default_game_saved=Fortnite; _awl=2.1717354536.5-7a212b0e4eeb152383358f1e7795159a-6763652d6575726f70652d7765737431-1',
#     'priority': 'u=0, i',
#     'referer': 'https://technical.city/ru/cpu',
#     'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
# }
#
# response = requests.get('https://technical.city/ru/cpu/rating', cookies=cookies, headers=headers)
#
#
# with open("new.html", 'w') as file:
#     file.write(response.text)
# ___________________________________

with open('new.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_positions = soup.find("tbody").find_all("tr")

with open("cpu.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            " title",
            " type",
            " socket",
            " performance",
            " cores",
            " year",
            " price",
            " power"
        )
    )

cpu_info = []
for item in all_positions:
    cpu_tds = item.find_all("td")

    number = cpu_tds[0].text.lstrip().rstrip()
    title = cpu_tds[1].find("a").text.lstrip().rstrip()
    type_spu = cpu_tds[2].find("span").text.lstrip().rstrip()
    socket = cpu_tds[3].text.lstrip().rstrip()
    performance = cpu_tds[4].text.lstrip().rstrip()
    cores_threads = cpu_tds[5].text.lstrip().rstrip()
    year = cpu_tds[6].text.lstrip().rstrip()
    price = cpu_tds[7].text.lstrip().rstrip()
    power_consumption = cpu_tds[8].text.lstrip().rstrip()

    cpu_info.append(
        {
            "title": title,
            "type": type_spu,
            "socket": socket,
            "performance": performance,
            "cores": cores_threads,
            "year": year,
            "price": price,
            "power": power_consumption,
        }
    )

    with open("cpu.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                type_spu,
                socket,
                performance,
                cores_threads,
                year,
                price,
                power_consumption
            )
        )



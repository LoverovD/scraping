import requests
from bs4 import BeautifulSoup


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
# }
#
#
# def editing_url(url):
#     url_elements = url.split('/')
#     up_element = url_elements[-1][0].upper()
#     ready_url = "https://www.bundestag.de/abgeordnete/biografien/" + up_element + '/' + url_elements[-1]
#     return ready_url
#
#
# def make_all_links_txt():
#     page = 0
#     all_members_links = list()
#     while True:
#         url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true" \
#               f"&offset={page * 12}&enodia=eyJleHAiOjE3MTc2MTcxODIsImNvbnRlbnQiOnRydWUsImF1ZCI6ImF1dGgiLCJIb3N0Ijoid3" \
#               f"d3LmJ1bmRlc3RhZy5kZSIsIlNvdXJjZUlQIjoiMTc4LjEyMS40NS4xNzkiLCJDb25maWdJRCI6IjhkYWRjZTEyNWZkMmMzOTMyYjk" \
#               f"0M2I1MmU5ZDJjZDY1MDU3NTRlMTYyMjEyYTJjZTFiYjVhZjE1YzBkNGJiZmUifQ==.OfC6ZkPV4c35e65S_bw23Rq3V21A5QaKTgA" \
#               f"oPAQ-m2w="
#         req = requests.get(url, headers)
#         if req.status_code == 404 or page == 64:
#             break
#         else:
#             page += 1
#         print(f"\nПарсинг ссылок на {page}-й странице...")
#
#         with open('try.html', 'w') as file:
#             file.write(req.text)
#
#         with open('try.html') as file:
#             src = file.read()
#
#         soup = BeautifulSoup(src, 'lxml')
#         all_classes = soup.find_all("div", class_="col-xs-4 col-sm-3 col-md-2 bt-slide")
#         for every_class in all_classes:
#             member_link = every_class.find('a').get('href')
#             cool_link = editing_url(member_link)
#             all_members_links.append(cool_link)
#
#     with open('member_url_list.txt', 'a') as file:
#         for line in all_members_links:
#             file.write(f'{line}\n')


def make_members_info_json():

    cookies = {
        'enodia': 'eyJleHAiOjE3MTc2MTc4OTksImNvbnRlbnQiOnRydWUsImF1ZCI6ImF1dGgiLCJIb3N0Ijoid3d3LmJ1bmRlc3RhZy5kZSIsIlN'
                  'vdXJjZUlQIjoiMTc4LjEyMS40NS4xNzkiLCJDb25maWdJRCI6IjhkYWRjZTEyNWZkMmMzOTMyYjk0M2I1MmU5ZDJjZDY1MDU3NT'
                  'RlMTYyMjEyYTJjZTFiYjVhZjE1YzBkNGJiZmUifQ==.9p-26z50HV4okXzUoj660Q_Q_uN7cNYoxfF_zEexqNY=',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'enodia=eyJleHAiOjE3MTc2MTc4OTksImNvbnRlbnQiOnRydWUsImF1ZCI6ImF1dGgiLCJIb3N0Ijoid3d3LmJ1bmRlc3RhZ
        # y5kZSIsIlNvdXJjZUlQIjoiMTc4LjEyMS40NS4xNzkiLCJDb25maWdJRCI6IjhkYWRjZTEyNWZkMmMzOTMyYjk0M2I1MmU5ZDJjZDY1MDU3
        # NTRlMTYyMjEyYTJjZTFiYjVhZjE1YzBkNGJiZmUifQ==.9p-26z50HV4okXzUoj660Q_Q_uN7cNYoxfF_zEexqNY=,
        'priority': 'u=0, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    }

    url = "https://www.bundestag.de/abgeordnete/biografien/A/abdi_sanae-861028"
    response = requests.get(url, cookies=cookies, headers=headers)

    with open('try.html', 'w') as file:
        file.write(response.text)


def main():
    # make_all_links_txt()
    make_members_info_json()


if __name__ == '__main__':
    main()

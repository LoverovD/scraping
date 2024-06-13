from bs4 import BeautifulSoup
from transliterate import translit
import requests


def parsing(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    card = soup.find('div', class_="sc-1cyl9gi-0 euyXjR show").find('div', class_="popup-padding")\
        .find('div', class_="popup-inner undefined").find('div', class_="sc-1r4m23d-0 dMRDbG")
    main_block = card.find('div', class_="sc-1r4m23d-8 BudjO").find('div', class_="scroll__view")\
        .find('div', class_="sc-1r4m23d-9 gOJzYh")

    name = main_block.find('div', class_="sc-1r4m23d-10 cqGCBA").find('h1').text.strip()
    compound_list = main_block.find('div', class_="sc-1r4m23d-15 jxYrMP").text.strip().split(", ")
    compound = []
    for comp in compound_list:
        compound.append(comp.rstrip("\xa0"))
    ###
    size_list = main_block.find('div', class_="sc-1r4m23d-13 gqjzdF").find('span').text.strip().split(', ')
    size = []
    for s in size_list:
        size.append(s.rstrip("\xa0").strip())
    price = card.find('div', class_="sc-1r4m23d-7 dlYEuz").find('div', class_="sc-1r4m23d-17 fvLrvW").\
        find('span').text.strip()

    poor_quality_url = card.find('div', class_="sc-1r4m23d-1 giHWeV").find('div', class_="sc-1r4m23d-2 kUZMOh").\
        find('img').get('src').split('/')
    picture_url = "https://media.dodostatic.net/image/r:1875x1875/" + poor_quality_url[-1].replace('.jpg', '.png')
    picture = requests.get(picture_url, headers=headers)
    out = open(f"pictures\\{translit(name, reversed=True).replace(' ', '_')}.png", 'wb')
    out.write(picture.content)
    out.close()
    ###
    nutritional_sections = main_block.find('div', class_="sc-1r4m23d-10 cqGCBA").find('div', class_="sc-13bk731-1 bMzoXT").\
        find('div').find('div', class_="sc-6k321-0 dEgNfL sc-13bk731-2 dblGKH tooltip").find_all('section')

    nutritional_value = {
        "energy_value": nutritional_sections[0].find('div').find_next_sibling().text.strip(),
        "squirrels": nutritional_sections[1].find('div').find_next_sibling().text.strip(),
        "fats": nutritional_sections[2].find('div').find_next_sibling().text.strip(),
        "carbohydrates": nutritional_sections[3].find('div').find_next_sibling().text.strip()
    }

    product_info = {
        "name": name,
        "size": size,
        "compound": compound,
        "price": price,
        "nutritional_value": nutritional_value,
    }
    return product_info


def main():
    print(parsing("https://dodopizza.by/minsk/product/syrniki-malina"))


if __name__ == '__main__':
    main()

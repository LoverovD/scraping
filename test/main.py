import re

from bs4 import BeautifulSoup
import sys


with open('index.html') as file:
    scr = file.read()

# print(scr)

soup = BeautifulSoup(scr, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find(), .find_all()
#
# page_h1 = soup.find('h1')
# print(page_h1)
#
# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)
#
# for el in page_all_h1:
#     print(el.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name)
# print(f"\n{user_name.text}")
# print(f"\n{user_name.text.strip()}")

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# user_info = soup.find_all("div", class_="user__info")
# print(user_info)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all('span')
# print(find_all_spans_in_user_info)
# for el in find_all_spans_in_user_info:
#     print(el.text)


# find_all_social_networks = soup.find(class_="social__networks").find_all('a')
# #print(find_all_social_networks)
# print('\n')
#
# for el in find_all_social_networks:
#     print(el)
# print('\n')
#
# for el in find_all_social_networks:
#     el_text = el.text
#     el_url = el.get('href')
#     print(f"{el_text} : {el_url}")


# .find.parent() and .find.parents()

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)


# .next_element and .previous_element след. и пред. эл. в глубину включительно

# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
# find_next_el = soup.find(class_="post__title").find_next().text
# print(find_next_el)


# .find_next_sibling() and .find_previous_sibling() след. и пред. эл. внутри искомого тэга

# find_a_by_text = soup.find('a', string=re.compile('Одежда')) # модуль регулярных выражений
# print(find_a_by_text)


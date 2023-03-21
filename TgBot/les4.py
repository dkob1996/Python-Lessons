import requests
from bs4 import BeautifulSoup
import re


def pars(name_hor):
    url = 'https://www.marieclaire.ru/astro/aries/day/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html')
    soup = str(soup)

    link_list = []
    start = 0
    for _ in range(12):
        start_ind = soup.find('<a class="astro-list__link" href="', start + 1)
        temp_str = soup[start_ind + 34: start_ind + 70]
        end_ind = temp_str.find('">')
        temp_link = temp_str[:end_ind]
        link_list.append(temp_link)
        start = soup.find('href="' + temp_link + '">') + 10

    name_list = ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']

    name_link_dict = {}

    for name, link in zip(name_list, link_list):
        name_link_dict[name] = link


    response = requests.get('https://www.marieclaire.ru' + name_link_dict[name_hor.lower()])

    soup = BeautifulSoup(response.text, 'html')
    soup = str(soup)
    start_ind_text = soup.find('class="block-text"') + 38
    end_ind_text = soup.find('</div><div class="astro-sign__other-signs mt-2">')
    return soup[start_ind_text: end_ind_text]
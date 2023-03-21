import requests
from bs4 import BeautifulSoup
import re



def currency(curr_name):
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html')

    quotes = soup.find_all('td')
    print(curr_name.capitalize())
    for i in range(len(quotes)):
        if curr_name.capitalize() == quotes[i].text:
            ind_el = i
            return (quotes[ind_el + 1].text)
    return ("There's no currency like this)")


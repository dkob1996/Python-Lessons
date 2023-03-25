import requests
from bs4 import BeautifulSoup
import re

def weather_bishkek(time_number):
    url = 'https://bishkek.nuipogoda.ru/погода-на-сегодня'
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    time_list = []
    for time in soup.find_all('span', class_= 'c1'):
        time_list.append(time.text)
    print(time_list)

    temperature_list =[]
    for temp in soup.find_all('span', class_= 'ht'):
        temperature_list.append(temp.text)
    print(temperature_list)

    wind_direction_list = []
    for obl in soup.find_all('span', class_ = 'wd'):
        wind_direction_list.append(obl.text)
    print(wind_direction_list)

    wind_speed_list =[]
    for speed in soup.find_all('span', class_='ws'):
        wind_speed_list.append(speed.text)
    print(wind_speed_list)

    weather_list = []
    for i in range(len(time_list)):
        str1 = 'Погода в Бишкеке: '
        str2 = 'Ветер: '
        str3 = 'Данные на: '
        str4 = '\n'
        str5 = str1 + str4 + temperature_list[i] + str4 + str2 + wind_direction_list[i] + ', ' + wind_speed_list[i] + str4 + str3 + time_list[i]
        weather_list.append(str5)
    #print(weather_list)
#    return weather_list[time_number]

    weather_dict = dict()
    weather_dict['00:00'] = weather_list[0]
    weather_dict['03:00'] = weather_list[1]
    weather_dict['06:00'] = weather_list[2]
    weather_dict['09:00'] = weather_list[3]
    weather_dict['12:00'] = weather_list[4]
    weather_dict['15:00'] = weather_list[5]
    weather_dict['18:00'] = weather_list[6]
    weather_dict['21:00'] = weather_list[7]
    weather_dict['24:00'] = weather_list[8]
    return weather_dict[time_number]

#print(weather_bishkek('03:00'))

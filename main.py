import requests
from bs4 import BeautifulSoup


def weather():
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    url = "https://www.gismeteo.ru/weather-grozny-5256/weekly/"
    req = requests.get(url=url, headers=headers)
    html = req.content
    soup = BeautifulSoup(html, "html.parser")

    day = soup.find("div", class_="widget-row widget-row-days-date").find_all('a')
    cloudiness = soup.find("div", class_="widget-row widget-row-icon").find_all('div', class_='row-item')
    degree = soup.find("div", class_="widget-row-chart widget-row-chart-temperature").find_all('div', class_='value style_size_m')

    # we create lists and put parsed data into this lists

    day_list=[]
    cloudiness_list=[]
    degree_list=[]

    for smg in day:
        day_list.append(smg.find('div', class_='day').text.strip() +', ' + smg.find('div', class_='date').text.strip())
    for smg in cloudiness:
        cloudiness_list.append(smg.find('div', class_='weather-icon tooltip')['data-text'].strip())
    for smg in degree:
        degree_list.append(str(smg.find('div', class_='maxt').find('span', class_='unit unit_temperature_c').text.strip())+
                           ' .. '+str(smg.find('div', class_='mint').find('span', class_='unit unit_temperature_c').text.strip()))

    # here we correlate days, cloudiness and degrees and unite them into a list.
    # Then we transform list into string
    a=[]
    for i in zip(day_list, cloudiness_list, degree_list):
        a.append('  '.join(i))
    a='\n\n'.join(a).replace('дек', '')
    return a





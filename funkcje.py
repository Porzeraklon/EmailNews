from bs4 import BeautifulSoup
from requests import get


def pogoda():
    URL = 'https://www.weatheronline.pl/Polska/Gdansk.htm'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    for weather in bs.find_all('table', class_='gr1'):
        temp_min = weather.find('span', class_='Temp_minus').get_text().strip()
        temp_max = weather.find('span', class_='Temp_plus').get_text().strip()
        return temp_min, temp_max

def kursy():
    URL = 'https://internetowykantor.pl/kurs-euro-nbp/'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    EUR = bs.find('span', class_='bem-single-rate-box__item-rate').get_text().strip()
    EUR_zmiana = bs.find('span', class_='bem-single-rate-box__direction ')
    kolor_EUR = "black"
    if EUR_zmiana == None:
        EUR_zmiana = bs.find('span', class_='bem-single-rate-box__direction is-up')
        if EUR_zmiana != None:
            EUR_zmiana = "+" + bs.find('span', class_='bem-single-rate-box__direction is-up').get_text().strip()
            kolor_EUR = "green"
        elif EUR_zmiana == None:
            EUR_zmiana = bs.find('span', class_='bem-single-rate-box__direction is-down').get_text().strip()
            kolor_EUR = "red"
        else:
            print("Coś nie działa z zmiana EUR")
    URL = 'https://internetowykantor.pl/kurs-dolara-nbp/'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    USD = bs.find('span', class_='bem-single-rate-box__item-rate').get_text().strip()
    USD_zmiana = bs.find('span', class_='bem-single-rate-box__direction ')
    kolor_USD = "black"
    if USD_zmiana == None:
        USD_zmiana = bs.find('span', class_='bem-single-rate-box__direction is-up')
        if USD_zmiana != None:
            USD_zmiana = "+" + bs.find('span', class_='bem-single-rate-box__direction is-up').get_text().strip()
            kolor_USD = "green"
        elif USD_zmiana == None:
            USD_zmiana = bs.find('span', class_='bem-single-rate-box__direction is-down').get_text().strip()
            kolor_USD = "red"
        else:
            print("Coś nie działa z zmiana USD")
    return EUR, EUR_zmiana, kolor_EUR, USD, USD_zmiana, kolor_USD

def wiadomosci():
    URL = 'https://wiadomosci.gazeta.pl/wiadomosci/0,0.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    i = 0
    for news in bs.find_all('article', class_="article"):

        t = news.find('h2').get_text().strip()
        o = news.find('p', class_='lead').get_text().strip()
        n = news.find('a')

        if i == 0:
            title1 = t
            opis1 = o
            link1 = n['href']

        if i == 1:
            title2 = t
            opis2 = o
            link2 = n['href']

        if i == 2:
            title3 = t
            opis3 = o
            link3 = n['href']

        if i == 3:
            title4 = t
            opis4 = o
            link4 = n['href']

        if i == 4:
            title5 = t
            opis5 = o
            link5 = n['href']

        if i == 5:
            title6 = t
            opis6 = o
            link6 = n['href']

        if i == 6:
            return title1, opis1, link1, title2, opis2, link2, title3, opis3, link3, title4, opis4, link4, title5, opis5, link5, title6, opis6, link6
        i = i + 1

def send_email():
    URL = 'https://emailwiadomosci.herokuapp.com/zaq1@WSXcde3$RFV'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    mails = []
    for mail in bs.find_all('p'):
        mails.append(mail.get_text().strip())
    return mails

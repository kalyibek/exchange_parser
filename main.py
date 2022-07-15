import requests
import csv
from bs4 import BeautifulSoup


URL = 'https://www.akchabar.kg/ru/exchange-rates/'
request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')
table = soup.find(id='rates_table').find('tbody')
banks = table.find_all('tr')
last_update_date = soup.find('div', class_='col-md-8 col-xs-12').text

file_name = f"{last_update_date.replace(':', ';')}.csv"
with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    header = ['Bank', 'buy', 'sale', 'buy', 'sale', 'buy', 'sale', 'buy', 'sale']
    currencies = [' ', 'USD', 'USD', 'EUR', 'EUR', 'RUB', 'RUB', 'KZT', 'KZT']
    writer.writerow(header)
    writer.writerow(currencies)

    for bank in banks:
        rates = bank.find_all('td')
        rates_list = []
        for rate in rates:
            rates_list.append(rate.text)
        writer.writerow(rates_list)

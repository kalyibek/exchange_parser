import requests
import csv
from bs4 import BeautifulSoup


URL = 'https://www.akchabar.kg/ru/exchange-rates/'
request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')
table = soup.find(id='rates_table')
banks = table.find('tbody').find_all('tr')
last_update_date = soup.find('div', class_='col-md-8 col-xs-12').text

file_name = f"{last_update_date.replace(':', ';')}.csv"
with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    currencies_list = [' ']
    currencies = table.find('thead').find_all('div', class_='val_wrapper')
    for currency in currencies:
        currencies_list.extend([currency.text, currency.text])
    writer.writerow(currencies_list)

    header_list = []
    header = table.find('thead').find('tr', class_='labels').find_all('td')
    for head in header:
        header_list.append(head.text)
    writer.writerow(header_list)

    for bank in banks:
        rates = bank.find_all('td')
        rates_list = []
        for rate in rates:
            rates_list.append(rate.text)
        writer.writerow(rates_list)

import requests
from bs4 import BeautifulSoup


class ScrapCoinmarket:
    def __init__(self):
        self.data = {}

    def get_scrap(self, c_name):
        r = requests.get('https://coinmarketcap.com/all/views/all/')
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('tbody')
        for row in table.find_all('tr'):
            try:
                if c_name == row.find('a', class_='cmc-table__column-name--name cmc-link').text:
                    symbol = row.find('td',
                                      class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--hide-sm cmc-table__cell--sort-by__symbol').text
                    mkt_cap = row.find('td',
                                       class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap').find(
                        'span', class_='sc-1ow4cwt-1 ieFnWP').text
                    price = row.find('td',
                                     class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price').text
                    circsup = row.find('td',
                                       class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply").text
                    volume = row.find('td',
                                      class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h").text
                    p_1h = row.find('td',
                                    class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h').text
                    p_24h = row.find('td',
                                     class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h').text
                    p_7d = row.find('td',
                                    class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d').text
                    self.data = {
                        'Name': row.find('a', class_='cmc-table__column-name--name cmc-link').text,
                        'Symbol': symbol,
                        'Market Cap': mkt_cap,
                        'Price': price,
                        'Circulating Supply': circsup,
                        'Volume(24h)': volume,
                        '%1h': p_1h,
                        '%24h': p_24h,
                        '%7d': p_7d
                    }
                    break
                else:
                    continue
            except AttributeError:
                continue
        for k, v in self.data.items():
            print(f'{k} - {v}')

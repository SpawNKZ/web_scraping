# Web Scraping
___
We will scrap information about all the related information about different cryptocurrencies

#### Installation
```
git clone https://github.com/diasprog/Assignment2Python.git
cd src
python3 web.py install
```
#### Usage
```
from web import ScrapCoinmarket
scrapper = ScrapCoinmarket()

```
#### Examples
```
>>> scrapper.get_scrap('Bitcoin')
Name - Bitcoin
Symbol - BTC
Market Cap - $939,930,832,472
Price - $49,902.22
Circulating Supply - 18,835,450 BTC
Volume(24h) - $35,338,490,241
%1h - -0.45%
%24h - 4.71%
%7d - 18.58%
```

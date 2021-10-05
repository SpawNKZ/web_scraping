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
# /simple/price endpoint with the required parameters
>>> scrapper.get_scrap('Bitcoin')
{'bitcoin': {'usd': 3462.04}}
```

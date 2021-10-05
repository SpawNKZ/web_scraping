# Web Scraping
___
We will scrap information about all the related information about different cryptocurrencies

#### Installation
```
git clone https://github.com/diasprog/Assignment2Python.git
cd pycoingecko
python3 setup.py install
```
#### Usage
```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```
#### Examples
```
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}
```

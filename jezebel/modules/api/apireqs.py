# provavelmente vai virar uma classe em modules/api
import requests as r
from jsongetter import *

HEADERS = []

def req_get(url, data=None, params=None):
    res = r.get(url)
    if res.status_code == 200:
        return get_json(res)
    else:
        return res.status_code

def req_post(self, url, data=None, params=None):
    if self.validate_data() != False:
        r.post(url, data, params)
    else:
        return False


# add validations to avoid errors when send post to api
def validade_data(data):
    if data != None:
        return data
    else:
        return False

# JUST TEST
print(req_get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc")) # marketsumamry
print(req_get("https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/hist")) # stats
print(req_get("https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/last")) # clande
print(req_get("https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist")) # clande


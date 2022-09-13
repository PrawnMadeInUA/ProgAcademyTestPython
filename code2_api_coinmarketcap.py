from json import tool
import coinmarketcapapi
cmc = coinmarketcapapi.CoinMarketCapAPI('e7c52ee6-d386-44de-8a89-e0a5970e8544')

tool = cmc.tools_priceconversion(amount=1, symbol='BTC', convert='USD')
res=tool.json

try:
   cmc_price=(res['price:'])
except:
	print('Can not return price from CoinMarketCap')


price = int(input('What is Bitcoin price today?'))
if price != cmc_price:	
	print('Are you sure? CoinmarketCap price is',cmc_price)
	price = int(input('Type confirmed price'))
else:	
	hold = int(input('How much $ do you have?'))

def total(a, b):
    return a/b

print('You can buy',total(hold, price),'BTC')



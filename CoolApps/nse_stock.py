from nsetools import Nse
nse = Nse()
#print(nse.get_index_list(as_json=True))
STOCK=nse.get_quote('HDFC')

print(STOCK.get('symbol')+" - "+ str(STOCK.get('lastPrice')) )


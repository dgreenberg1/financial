#import sys
#sys.path.append('/home/ubuntu/projects/financial')
from fetch import Fetch

fetch = Fetch()
params = [('sc', 431)]

stocklist = fetch.fetch_stocks(params)
print stocklist

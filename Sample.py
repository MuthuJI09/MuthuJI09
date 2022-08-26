# importing libraries
from bs4 import BeautifulSoup as BS
from pendulum import datetime
from pkg_resources import WorkingSet
import requests
import re
import datetime
import csv

# method to get the price of gold
def get_price(url):
	
	# getting the request from url
	data = requests.get(url ,verify=False)

	# converting the text
	soup = BS(data.text, 'html.parser')

	# finding metha info for the current price
	ans = soup.find("div", id="current-price").text
	
	# returning the price
	return ans

# url of the gold price
url = "https://www.goodreturns.in/gold-rates/madurai.html"

# calling the get_price method
ans = get_price(url)

# printing the ans

ans=re.search("₹.*",ans)
ans=str(ans.group())
ans=re.findall("\d",ans)
ans="".join(ans)
x=datetime.datetime.now()
x=x.strftime("%Y-%m-%d-%H:%M:%S")
ans=" ".join([x,ans])
print(ans)

with open("P1rice.csv", 'a', newline = '') as CSV:
    Csv=csv.writer(CSV,delimiter='\t')
    Csv.writerow(ans)

    

import urllib.request
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.nike.com/launch/?s=upcoming'

# query the website and return the html to the variable 'html'
with urllib.request.urlopen(quote_page) as response:
    html = response.read()

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(html, 'html.parser')

# gather the list of upcoming shoes and dates
nameStack = []
for shoe in soup.find_all('h3', {'class':'ncss-brand u-uppercase text-color-grey mb-1-sm mb0-md mb-3-lg fs12-sm fs14-md'}):
    nameStack.append(shoe.text[:-1])
colorStack = []
for shoe in soup.find_all('h6', {'class':'ncss-brand u-uppercase fs20-sm fs24-md fs28-lg'}):
    colorStack.append(shoe.text[:-1])
monthStack = []
for shoe in soup.find_all('p', {'class':'mod-h2 ncss-brand u-uppercase fs19-sm fs28-md fs34-lg'}):
    monthStack.append(shoe.text)
dayStack = []
for shoe in soup.find_all('p', {'class':'mod-h1 ncss-brand test-day fs30-sm fs40-md'}):
    dayStack.append(shoe.text)

# format the list of shoes to be sent to twitter.py
stack = []
shoeInfo = '{} {} - {} {}'
for item in zip(nameStack, colorStack, monthStack, dayStack):
    stack.append(shoeInfo.format(item[0], item[1], item[2], item[3]))
size = len(stack)
print('Successfully retrieved list of upcoming sneaker releases.')
# Google.py - A script that opens multiple web searchs via CLI  

import requests 
import sys 
import webbrowser 
import bs4

print('Searching...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
print('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieves the top search result links

soup = bs4.BeautifulSoup(res.text, features="html.parser")

print(res.text)

#Open a browser tab for each result
linkElems = soup.select(".kCrYT a")
print(len(linkElems))
numOpen = min(5, len(linkElems))
print('We are here!')
for i in range(numOpen):
    webbrowser.open('https://www.google.com'+ linkElems[i].get('href'))


#For some reason, the parsing isn't working right now
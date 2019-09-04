#Python 3
#XKCD.py - A way to download every XKCD comic

import requests
import os
import bs4

url = 'http://xkcd.com' #The XKCD URL
os.makedirs('xkcd', exist_ok=True) #This will verify if XKCD folder exists, else it will create it

while not url.endswith('#'):
    #Downloading the page
    print('Download page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)    
    #Find the URL of the comic
    comicElem = soup.select('#comic img')
    print (comicElem)

    if comicElem == []:
        print('comicElem is empty, no comic image found.')
    else:
        comicUrl = comicElem[0].get('src')
        # Downloading the image
        print('Downloading the image %s...' %(comicUrl))
        res = requests.get('http:' + comicUrl)
        res.raise_for_status()
    #Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #Get the prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    print('Done!')

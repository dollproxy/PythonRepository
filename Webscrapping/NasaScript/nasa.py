#Python 3
#Nasa.py - A way to get the daily Nasa pic

import requests
import os
import bs4

url = 'https://apod.nasa.gov/apod/astropix.html' #The URL of the Nasa daily pic website
os.makedirs('nasa', exist_ok=True) #Making the picture director

#Downloading the page
print('Downloading Nasa page')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

#Getting the daily image
dailyImage = soup.select('IMG')
print (dailyImage)

if dailyImage == []:
    print("I'm sorry, I couldn't find the image you are looking for.")
else:
    imageUrl = dailyImage[0].get('src')
    print('Downloading: %s' % imageUrl)
    res = requests.get('https://apod.nasa.gov/apod/' + imageUrl)
    res.raise_for_status()
    #Saving the Image
    imageFile = open(os.path.join('nasa', os.path.basename(imageUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()


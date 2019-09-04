import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)

print(type(exampleSoup))
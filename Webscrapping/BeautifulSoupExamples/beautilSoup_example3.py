import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())


elems = exampleSoup.select('#author')

#Will print the type of the element
print(type(elems))
#Will print the one match 
print(len(elems))
#Will print the text content in the Author ID
print(elems[0].getText())
#Will print the full HTML string
print(str(elems[0]))
#Will print the attributes found
print(elems[0].attrs)
import requests 

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt.utf8.gzip')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem! : %s' % (exc))

playFile = open('RomeoAandJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
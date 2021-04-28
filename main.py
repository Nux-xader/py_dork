'''
Buat yang mau nge recode, gw cuman minta 1.
Sisipin nama gw walau cuman di comment doang:)
______________________________________________

For those who want to recode, I only ask for 1.
Insert my name even though it's only in the comments :)
'''
import requests
from bs4 import BeautifulSoup

y = '\x1b[33m'
r = '\x1b[31m'
g = '\33[32;1m'
cy = '\33[36;1m'
w = '\33[37;1m'
b = '\33[34;1m'
attr = {'class': 'g'}
srchEngine = "https://www.google.com/search"
ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
result = ""
banner = r"""{}____________________________________________{}

Youtube  : {}1. {}https://youtube.com/c/ythack
           {}2. {}bit.ly/kelasit{}

Github   : {}github.com/nux-xader{}
Facebook : {}facebook.com/nux.xader{}
____________________________________________
{}
 _____         _____             _ 
|  __ \       |  __ \           | |
| |__) |   _  | |  | | ___  _ __| | __
|  ___/ | | | | |  | |/ _ \| '__| |/ /
| |   | |_| | | |__| | (_) | |  |   < 
|_|    \__, | |_____/ \___/|_|  |_|\_\
        __/ |                         
       |___,/  V 1.0
""".format(r,b,r,g,r,g,b,g,b,g,r,b)

print(banner)
# keyword = str(input(b+"Input Keyword : "+g))
payload = {'q':str(input(b+"Input Keyword : "+g))}
saveTo = str(input(b+"Save To : "+g))
if saveTo == "":
	print(b+"["+r+"!"+b+"]"+g+"Auto save to result.txt")
	saveTo = "result.txt"

data = requests.get(srchEngine, payload, headers=ua, timeout=25, allow_redirects=True)
if data.status_code != 200:
	print("Somethong Wrong\nStatus Code : "+str(data.status_code))
	exit()

parse = BeautifulSoup(data.text, "html.parser")
for i in parse.find_all('a', href=True):
	url = str(i['href'])
	if "http" in url and "google" not in url:
		index = url.index("http")
		result+=url[index:]+"\n"
with open(saveTo, "w") as f:
	f.write(result)
print(g+"Successfully save result to "+saveTo+b)
print("""
This Tools still in the development process
so don't forget to follow github.com/nux-xader
so you don't miss the update, thank you:)""")
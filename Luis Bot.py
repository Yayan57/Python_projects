import requests
import bs4
import random
import webbrowser
import threading
import csv
import RandomHeaders


def UrlGen(model, size, name):
    baseSize = 580
    ShoeSize = Size - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + baseSize
    ShoeSizeCode = int(RawSize)
    URL = 'http://www.adidas.com/us/' + str(name) + '/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(
        ShoeSizeCode) + '&wquantity=1'
    return URL


def checkStock(url, model):
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, '
                                       'like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    RawHTML = requests.get(url, headers=headers)
    Page = bs4.BeautifulSoup(RawHTML.text, "lxml")
    ListofRawSizes = Page.select('.size-dropdown-block')
    Sizes = str(ListofRawSizes[0].getText().replace('\t', ''))
    Sizes = Sizes.replace('\n\n', ' ')
    Sizes = Sizes.split()
    Sizes.remove('Select')
    Sizes.remove('size')
    for size in Sizes
        print(str(model) +'size:' + str(size) + 'is available')

def main(model, size):
    url = UrlGen(Model, size, Name)
    checkStock(url, model)

def sneakerBot(mode, size=None):
    while True:
        try:
            url = 'string'.format(model)
            Sizes = checkStock(url)
            if size != None:
                if str(size) in Sizes:
                    Dosomething()
            else:
                for a in Sizes:
                    DoSomething()
        except:
            pass

threads = (threading.Thread(name='ThreadNumber{}'.format(n), target = SneakerBot, args=(ModelNumber, size,))for size in SizeList for n in range(ThreadCount))
for t in threads: t.start()



Model = input('Model #')
Name = str(input('name of the shoe:'))
Name = Name.replace(' ', '-')
Size = float(input("Size:"))
Name = Name.lower()

URL = UrlGen(Model, Size, Name)

print(str(URL))

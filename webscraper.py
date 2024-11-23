import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request \
        .urlopen(self.site)
        xml = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(xml, parser)
        st = open("headlines.txt", "w")
        for item in sp.find_all("item"):
            title = item.find("title")
            if title is None:
                continue
            else:
                st.write("\n" + title.text)
        st.close()

news = "https://news.google.com/news/rss/headlines"

Scraper(news).scrape()




'''
7. Zaimplementuj non-data deskryptor, który przyjmować będzie adres strony WWW,
a następnie będzie zwracać listę linków, które znajdują się na tej stronie.
Wykorzystaj biiblioteki requests i beautifulsoup lub ich alternatywy.
'''
import requests
from bs4 import BeautifulSoup


class NonDataDescriptorLinks:
    def __init__(self, url):
        self.url = url

    def __get__(self, obj, objtype):
        reqs = requests.get(self.url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            url = link.get('href')
            if url and url != '#':
                urls.append(url)
        return urls


class MyClass:
    x = NonDataDescriptorLinks('https://sii.pl/')


m = MyClass()
print(m.x)

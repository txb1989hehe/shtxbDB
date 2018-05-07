
__author__ = 'luke_tang'
from pick_func import get_a_href
from bs4 import BeautifulSoup
import requests


class Anjuke_house(object):
    def __init__(self, url):
        self.url = url

    def all_floor_data(self):
        web = requests.get(self.url).text
        try:
            soup = BeautifulSoup(web, 'lxml')
            all_name = soup.select('div.infos > a.lp-name > h3 > span')
            all_address = soup.select('div.infos > a.address > span')
            all_price = soup.select('div.item-mod > a.favor-pos > p.price')
            name_list = []
            address_list = []
            price_list = []
            for name in all_name:
                name_list.append(name.get_text())
            for address in all_address:
                address_list.append(address.get_text())
            for price in all_price:
                price_list.append(price.get_text())
            show_list = get_a_href.py2_map(name_list, address_list, price_list)
            return show_list
        except Exception as e:
            return None

    def exect_data(self):
        soup = get_a_href.get_soup(self.url)
        data = soup.select('div.infos > a.tags-wrap > div.tag-panel')
        list1 = []
        for d in data:
            list1.append('-'.join(d.get_text().split('\n')))
        return list1

    def combine_data(self):
        listdata = self.all_floor_data()
        exectdata = self.exect_data()
        cdata = []
        for i in range(len(listdata)):
            cdata.append(listdata[i] + '\t' + exectdata[i])
        return cdata

    def savetxt(self):
        data = self.combine_data()
        if data:
            with open('anjuke1_house.txt', 'a+', encoding='utf-8') as tf:
                for onedata in data:
                    tf.write(onedata+'\n')
            return 'GET OK'
        else:
            return 'FAIL'


if __name__ == '__main__':
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    for page in range(1, 29):
        if page == 1:
            URL = 'https://sh.fang.anjuke.com/loupan/all/'
            anjuke = Anjuke_house(URL)
            print(anjuke.savetxt())
        else:
            URL = 'https://sh.fang.anjuke.com/loupan/all/p{}/'.format(page)
            anjuke = Anjuke_house(URL)
            print(anjuke.savetxt())
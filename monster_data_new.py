from bs4 import BeautifulSoup
import requests


class Monster_data:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_soup(self, hisurl):
        mainurl = self.url + hisurl
        webdata = requests.get(mainurl, headers=self.headers).content
        soup = BeautifulSoup(webdata, 'lxml')
        return soup

    def get_fiveurl(self):
        fivesubr = ('Fire%20(A)', 'Water%20(A)', 'Wind%20(A)', 'Dark%20(A)', 'Light%20(A)')
        base_url = 'http://summonerswar.wikia.com/wiki/Monster_Collection'
        for a in fivesubr:
            subrurl = base_url + '#' + a
            html = requests.get(subrurl,headers = self.headers).content
            subrsoup = BeautifulSoup(html,'lxml')
            monstersurl = subrsoup.select('td > a.image')
            monsters_list = []
            for b in monstersurl:
                monsters_list.append(b['href'])
            # monster_dict = {}
            # for b in monstersurl:
            #     monster_dict['url'] = b['href']
            #     monster_dict['name'] = b['title']
            #     monsters_list.append(monster_dict)
            #     monster_dict = {}
            return monsters_list

    def mainget_values(self):
        hisurls = self.get_fiveurl()
        for hisurl in hisurls:
            values_list = self.get_subr(hisurl)
            values_str = '\t'.join(values_list)
            with open('monsters_data.txt','a+',encoding='utf-8') as tf:
                tf.write(values_str + '\n')
        return 'Save ok~'

    def get_subr(self, hisurl):
        soup = self.get_soup(hisurl)
        monster_subrs = soup.select('div.monstertable > div > div > div')
        monster_name = hisurl.split('/')[-1]
        subr_list = []
        value_list = []
        for subr in monster_subrs:
            subr_list.append(subr.get_text())
        for i in range(1, len(subr_list),3):
            value_list.append(subr_list[i])
        value_list.insert(0, monster_name)

        monster_skills = soup.select('b > span.basic-tooltip')
        skill_list = []
        for skill in monster_skills:
            skill_list.append(skill.get_text())
        monster_values = value_list + skill_list
        return monster_values


if __name__ == '__main__':
    oneurl = 'http://summonerswar.wikia.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    monster = Monster_data(oneurl, headers)
    print(monster.mainget_values())


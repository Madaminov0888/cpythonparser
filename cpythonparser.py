import requests
from bs4 import BeautifulSoup
import lxml

MAIN_URL = 'https://cpython.uz/competitions/contests/?page='
JUST_URL = 'https://cpython.uz'


def get_past_contests_url(pages = 15, url = MAIN_URL) -> list:
    h = []
    for i in range(1, pages+1):
        url1 = url + str(i)
        response = requests.get(url = url1, verify=False)
        soup = BeautifulSoup(response.text, features='lxml')
        contests_tag = soup.find_all('div', {'class':'layout-spacing'})[3]
        tag1 = contests_tag.find('tbody')
        for tag in tag1.find_all('tr'):
            h.append(JUST_URL + str(tag.td.a.attrs['href']).strip()+'standings/')
    return h


def get_count(url_list = get_past_contests_url()) -> list:
    h = []
    for i in url_list:
        response = requests.get(url = i, verify=False)
        soup = BeautifulSoup(response.text, features='lxml')
        for users in soup.find('tbody').find_all('tr'):
            if str(users.td.p.text).strip() == '1':
                add = users.find_all('td')[1].span.find_all('a')
                if len(add) == 1:
                    h.append(str(users.find_all('td')[1].span.a.text).strip())
                else:
                    for img in add:
                        tag = str(img.attrs['href']).split('/')[2]
                        h.append(tag)
            else:
                break
    return h



def fatality(users_list = get_count())-> list:
    h = []
    set_list = set(users_list)
    for j in set_list:
        u = []
        cnt = users_list.count(j)
        u.extend([j, cnt])
        h.append(u)
    return h



h = ['genemator - 1', 'Lazizbek - 2', 'Sunnat - 3', 'ogabek8433 - 5', 'Bobur - 1', 'Dasturchi - 2', 'Quvonchbek - 8', 'temur.dusenbaev - 4', 'Husayn_Hasanov - 6', 'dusenbaev - 2', 'OtabekJurabekov - 4', 'timurruzmetov - 2', 'kharezmi - 11', 'p1ke - 4', 'm1808 - 1', 'Zohidbek - 6', 'ThA - 1', 'admin - 7', 'JavohirXoldorov - 1', 'Siroj - 1', 'bagbanpir - 4', 'Amirkhan666 - 1', 'AZD_creation - 4', 'karim - 1', 'dxz05 - 2', 'xursand_saydmurotov - 1', 'Shoxzod - 15', 'Mansurbek - 3', 'MDSPro - 6', 'cosmosc - 1', 'Rasulbek07 - 4', 'Dilbar - 1', 'alimurodov - 1', 'master87 - 1', 'ОбидСиндаров - 1', 'sapaevruzmat - 1', 'olimboy - 1', 'maftuna_karimboyeva - 1', 'Madaminov0888 - 13', 'Alibek - 3', 'mercurial - 1', 'timur_rahimquliyev - 1', 'Narzullayev.S_ - 3', 'muhammadjon - 1', 'The_Samurai - 7', 'FillerSeries - 1', 'zakam1999 - 1', 'hojinazar_otaxonov - 2', 'anonymous - 1', 'doniyor_samandarov - 2', 'umidbek_raximberganov - 2', 'Shoxrux - 1', 'Doniyor - 1', 'sanjarbek6665 - 1', 'Ibrohim - 5']
for i in h:
    print(i)
from bs4 import BeautifulSoup
import bs4
import requests


def get_soup(url):
    
    '''
    Скачиваем страничку, делаем soup
    '''
    
    req = requests.get(url)
    if req.status_code == 200:
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        return soup
    return None


def clean_line(line):
    line = re.sub('\[править\]', '', line)
    line = re.sub('\xa0', ' ', line)
    return line
    

link_wiki = 'https://ru.wikisource.org/wiki/Викитека:Школьная_программа'
soup_wiki = get_soup(link_wiki)
body = soup_wiki.find("div", {"class": "mw-content-ltr"})
body = list(body)[0]


#  h2 = Русская литература
#  h3 = Фольклор
#  h4 = Устное народное творчество
#  ul = «Помню, я ещё младшенька была…»


base = 'ru.wikisource.org'
a = list(body.children)
h2 = False
h3 = False
h4 = False
d = {}


for i in body.children:

    if i.name == 'h2':
        h2 = clean_line(i.text)
        d[h2] = {}
    
    if i.name == 'h3':
        h3 = clean_line(i.text)
        if h2: d[h2][h3] = {}
    
    if i.name == 'h4':
        h4 = clean_line(i.text)
        if h3: d[h2][h3][h4] = []
        else: d[h2][h4] = []
            
    if i.name == 'ul':
        
        if h4 in d[h2]: place = d[h2][h4]
        if h3 in d[h2]:
            if h4 in d[h2][h3]: place = d[h2][h3][h4]
            else:
                if len(d[h2][h3]) == 0: d[h2][h3] = []
                place = d[h2][h3]
        else: 
            if len(d[h2]) == 0: d[h2] = []
            place = d[h2]

        for name in i.find_all('li'):
            
            if name.find('a') != None and 'title' in name.a.attrs:
                if '(страница не существует)' not in name.a['title']:
                    link = base + name.a['href']
            else: link = ''
            
            place.append((name.text, link))

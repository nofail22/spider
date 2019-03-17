from bs4 import BeautifulSoup
import requests

from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        tre = table.find_all('tr')[2:]
        for index,tr in enumerate(tre):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"citt":city,"min_temp":int(min_temp)})
            # print({"citt":city,"min_temp":min_temp})
            print(ALL_DATA )



def main():
    urls = ['http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/gat.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hb.shtml'
            ]
    for url in urls:
        parse_page(url)

    #排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    data = ALL_DATA[0:10]
    # print(ALL_DATA)
    cities = list(map(lambda x:x['city'],data))
    temps = list(map(lambda  x:x['min_temp'],data))
    chart = Bar('温度')
    chart.add('',cities,temps)
    chart.render('temperature.html')



if __name__ == "__main__":
    main()






















import requests
import re

def parge_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    response = requests.get(url,headers=headers)
    text = response.text



def main():
    url = 'http://www.92yyy.com/?m=art-type-id-1.html'
    parge_page(url)

if __name__ == '__main__':
    main()

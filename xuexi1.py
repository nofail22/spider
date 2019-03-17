import requests
from lxml import etree

url = 'https://www.meipian.cn/1z3659pz'
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
resp = requests.get(url,headers=headers).text
# print(resp)
html = etree.HTML(resp)  #查找遍历
text = html.xpath('//div[@class="text well"]//h3/text()')  #遍历出这个需要的对象
# zhi = html.xpath('//div[@class="text well"]//ul/li/text()')
# for li in zhi:
# print(zhi)
# print(text)
for txt in text:
    print(txt)





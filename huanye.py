import requests
from lxml import etree

str = 'https://www.meiwen.com.cn' #拼接每一页的前缀

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

def get_url(url):
    response = requests.get(url, headers=HEADERS).text
    # response.text
    # response.content
    # requests 会默认使用自己猜测的编码方式将抓取下来的网页进行解码，然后存储到text属性上去
    # print(response.content.decode('utf-8'))                                                 #requests 解码编码 用到contenr
    html = etree.HTML(response)  # xpath
    rep = html.xpath('//ul[@class="tbody"]//li//a/@href')  # 匹配每一个的标题的url
    # print(rep)
    rep = map(lambda url:str+url,rep) # 匿名函数 lambda 表达式
    return rep  #返回


def parse_deti_page(url):
    # guigushiall = []
    response = requests.get(url,headers=HEADERS).text
                                                                 # text = response.content.decode('gbk')|('utf-8')  进行解码操作
    html = etree.HTML(response)
    title = html.xpath('//div[@id="title"]//h1/text()')
    print(title)    #打印出标题
    # guigushiall['title'] = title
    gushi = html.xpath('//div[@class="content"]//p/text()')
    for gushiwen in gushi:
        # guigushiall['gushi'] = gushiwen
        print(gushiwen)

    # guigushiall.append(guigushiall)
    print(gushi)

def spider():
    base_url = 'https://www.meiwen.com.cn/gushi/gui/{}.html'  #url 地址
    for x in range(1,11):    #for循环页数
        #第一个for 循环是来控制页数
        # print("="*30)
        # print(x)
        # print("="*30)
        url = base_url.format(x)      #塞进循环
        meiwen = get_url(url)
        for allmeiwen in meiwen:    #遍历所有的文章的url
            # print(allmeiwen)
            guigushi = parse_deti_page(allmeiwen)  #url传递到parse_deti_page 上进行每一页的解析





if __name__ == "__main__":
    spider()
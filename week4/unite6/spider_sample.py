import csv
import requests
from lxml import etree
fp=open("data.csv",'w',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(['name','actor','information','data','star','evaluate','introduction'])
urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
myheaders = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
}

for url in urls :
    html=requests.get(url,headers=myheaders)
    selector= etree.HTML(html.text)
    infos=selector.xpath("//ol[@class='grid_view']/li")
    arr=[]
    for info in infos:
        line=[]
        name=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()")
        line.append(''.join(name))
        introduction=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']/p/text()")
        for i in range(0,len(introduction)):
            s=''.join(introduction[i]).strip()
            if len(s):
                line.append(s)
        star=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span//text()")
        for i in range(0,len(star)):
            s=''.join(star[i]).strip()
            if len(s):
                line.append(s)
        # print(introduction[0])
        writer.writerow(line)

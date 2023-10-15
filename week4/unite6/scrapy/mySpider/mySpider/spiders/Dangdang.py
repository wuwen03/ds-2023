import scrapy
from urllib.parse import urljoin
from scrapy.http import Request
import csv

class DangdangSpider(scrapy.Spider):
    name = "Dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        file=open("data.csv",'a+',encoding="UTF-8")
        writer=csv.writer(file)
        writer.writerow(["name","author","price"])
        # file.write("1\n")
        selector=response.selector
        infos=selector.xpath("//html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li")
        # selector=response.css("//html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li")
        # file.write(str(selector)+"\n")
        # file.write(str(infos))
        for info in infos:
            name=info.xpath("./p[@class='name']/a/text()").extract_first()
            author=info.xpath("./p[@class='search_book_author']/span/a/@title").extract_first()
            price=info.xpath("./p[@class='price']/span[@class='search_now_price']/text()").extract_first()
            yield{"name":name,"author":author,"price":price}
            writer.writerow([name,author,price])
            # print(name,author,price)
            # temp=name+author+price+"\n"
            # file.write(temp)
        
        next_url=selector.xpath("/html/body/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/ul/li[10]/a/@href").extract_first()
        print(next_url)
        if next_url and next_url<"/pg9":
            url = response.urljoin(next_url)
            yield Request(url,callback=self.parse)
        # infos=selector.xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]").extract()
        # file.write(infos)
        pass
        

# -*- coding: utf-8 -*-
import scrapy
from proxyIp.items import ProxyipItem

class GetipSpider(scrapy.Spider):
    name = 'getIp'
    # allowed_domains = ['fsd']
    start_urls = ['http://www.ip181.com/']

    def parse(self, response):
        
        ips = response.xpath("//tr")
        for ip in ips:
            item = ProxyipItem()
            isHttps = ip.xpath('./td[4]/text()')
            ipType = "http://"
            if (str(isHttps).find("HTTP") == -1):
                continue
            if (str(isHttps).find("HTTPS") != -1):
                ipType = 'https://'
            item['ip'] = ipType +  ip.xpath('./td[1]/text()')[0].extract() + ":" + ip.xpath('./td[2]/text()')[0].extract()
            # print("*"*50)
            # print(ip.xpath('./td[1]/text()')[0].extract())
            yield item

import os
import sys
import logging
import scrapy
from blog.items import BlogItem

reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Myblog(scrapy.Spider):
	name = 'myblog'
	allowed_domains = ["cnblogs.com"]
	start_urls = ["http://www.cnblogs.com/TongWee"]
	def parse(self, response):
		titles = []
		links = []
		for sel in response.xpath('//*[@class="postTitle2"]'):
			title = sel.xpath('text()').extract()
			for ti in title:
				titles.append(ti)
				self.logger.info("<TITLE> : \t" + ti)
			link = sel.xpath('@href').extract()
			links.append(link)
		for i in range(0, len(titles) - 1):
			item = BlogItem()
			item['title'] = titles[i]
			item['link'] = links[i]
			yield item


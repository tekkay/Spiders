import scrapy

class NoticiaSpider(scrapy.Spider):
     name = 'noticiasspider'
     start_urls = ['https://g1.globo.com']

     def parse(self, response):
         for title in response.css('._q'):
              yield {'feed-post-link': feed-post-link.css('a ::text').extract_first()}
         ##for next_page in response.css('div.prev-post > a'):
             ##yield response.follow(next_page, self.parse)

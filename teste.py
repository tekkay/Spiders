import scrapy

scrapy shell https://g1.globo.com/

response.css("div.feed-post-body-title.gui-color-primary.gui-color-hover a::text").extract()


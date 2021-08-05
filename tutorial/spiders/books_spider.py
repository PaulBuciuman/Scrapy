import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for cat in response.xpath('//div[@class = "col-sm-8 col-md-9"]//section//ol[@class="row"]//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]//article[@class="product_pod"]'):
            
            yield {
                'title': cat.css('h3 a::text').get(),
                'price': cat.css('p.price_color::text').get()[1:],
            }

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
            

        

         
           
            

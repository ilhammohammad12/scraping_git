import scrapy
#scraping project in git

class AppleSpider(scrapy.Spider):
    name = 'Apple'
    start_urls = ['https://www.amazon.in/s?k=apple+tab&ref=nb_sb_noss']

    def parse(self, response):
        for products in response.css('.s-result-item'):
            yield {
                'Product_name': products.css('span.a-size-medium.a-color-base.a-text-normal::text').get(),
                'Product_Link': products.css('a.a-link-normal.a-text-normal::attr(href)').get(),
                'Rating': products.css('span.a-icon-alt::text').get(),
                'Price': products.css('span.a-price-whole::text').get()
                }
        next_page = response.css('li.a-last > a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

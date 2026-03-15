import scrapy
from pathlib import Path


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    async def start(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        # for saving the file
        #Path(filename).write_bytes(response.body)
        #self.log(f"Saved file {filename}")

        # for getting the products by checking the css name in the inspect in website
        # get() for single product, getall for all.
        a = response.css(".product_pod").get()   # getall() for all products

        print(a)

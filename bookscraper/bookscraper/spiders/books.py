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

def parse(self, response):
        # Select all book containers
        books = response.css(".product_pod")

        for book in books:
            yield {
                # The title is inside an <h3><a> tag's title attribute
                'name': book.css("h3 a::attr(title)").get(),
                
                # Price is inside a <p> with class 'price_color'
                'price': book.css(".price_color::text").get(),
                
                # Rating is a class name (e.g., "star-rating Three")
                # We extract the second class name
                'stars': book.css(".star-rating::attr(class)").get().replace("star-rating ", ""),
                
                # Stock status is inside a <p> with class 'instock availability'
                'in_stock': book.css(".instock.availability::text").getall()[-1].strip(),
                
                # Link to the book's detail page
                'url': response.urljoin(book.css("h3 a::attr(href)").get()),
            }

# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'

    start_urls = ['https://www.imdb.com/title/tt0106145/']

    def parse(self, response):
        navigation_link = response.url + 'fullcredits/'
        yield scrapy.Request(navigation_link, callback = self.parse_full_credits)

    def parse_full_credits(self, response):
        actor_list = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        for actor in actor_list:
            yield scrapy.Request('https://www.imdb.com'+actor, callback = self.parse_actor_page)

    def parse_actor_page(self, response):
        rough_film_list = response.css("div.filmo-row").css("a::text").getall()
        exact_list = [ i for i in rough_film_list if i[0:7] != 'Episode']
        actor_name = response.css("span.itemprop::text").get()
        
        for film in exact_list:
            yield {
                "actor": actor_name,
                "movie_or_TV_name": film
            }
        


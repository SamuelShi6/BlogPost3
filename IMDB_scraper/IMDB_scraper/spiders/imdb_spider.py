# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

# start by writing a new class inherited from Spider
class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'

    # url for my favorite movie
    start_urls = ['https://www.imdb.com/title/tt0330373/']

    def parse(self, response):
        '''
        assumes we start from the home page of the movie, and helps us navigate to the Cast & Crew Page.
        In the end, we will call the method `parse_full_credits(self,response)`
        @param response: an object that helps us crawl the web
        @return : this method does not return any data
        '''

        # specify the Cast & Crew Page
        navigation_link = response.url + 'fullcredits/'

        # call the parse_full_credits() method to the Cast & Crew page
        yield scrapy.Request(navigation_link, callback = self.parse_full_credits)

    def parse_full_credits(self, response):
        '''
        assume that we start on the Cast & Crew page and yields a scrapy.Request for the page of each actor listed on the page
        @param response: an object that helps us crawl the web
        @return : this method does not return any data
        '''
        # use list comprehension to generate the actor's list
        actor_list = [a.attrib["href"] for a in response.css("td.primary_photo a")]

        # write a for-loop to call the next method on each actor's page
        for actor in actor_list:
            yield scrapy.Request('https://www.imdb.com'+actor, callback = self.parse_actor_page)

    def parse_actor_page(self, response):
        '''
        assume that we are on the page of an actor and yields a dictionary with two key-value pairs, 
        of the form {"actor" : actor_name, "movie_or_TV_name" : movie_or_TV_name}. 
        the method should yield one such dictionary for each of the movies or TV shows on which that actor has worked.
        @param response: an object that helps us crawl the web
        '''
        # find the actor's name
        actor_name = response.css("span.itemprop::text").get()

        # find the list of the work that the actor has worked on 
        rough_film_list = response.css("div.filmo-row")
        # we are only interested in those with a valid IMDB page
        exact_list = [i.css("a::text").get() for i in rough_film_list if i.css("::attr(id)") and i.css("a")]
        
        # yield a dictionary for each of the film 
        for film in exact_list:
            yield {
                "actor": actor_name,
                "movie_or_TV_name": film
            }
        


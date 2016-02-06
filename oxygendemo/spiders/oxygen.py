import scrapy
from pyquery import PyQuery


class OxygenSpider(scrapy.Spider):
    name = "oxygenboutique.com"
    base_url = "http://www.oxygenboutique.com/"
    start_urls = ["http://www.oxygenboutique.com"]

    type_guess_keywords_map = {
        "A": ["apparel", "clothing", "dress"],
        "S": ["shoes", "sandals"],
        "B": ["bags", "bag"],
        "J": ["jewelry", "gold", "ring"],
        "R": ["accessories", "gold", "ring"],
    }

    def get_absolute_url(self, href):
        return "%s%s" % (self.base_url, href)

    def parse(self, response):
        pq = PyQuery(response.body)
        category_href_list = [c.attr("href") for c in pq("ul.mega_box ul li a").items()]

        for ct_href in category_href_list:
            yield scrapy.Request(url=self.get_absolute_url(ct_href), callback=self.parse_category)

    def parse_category(self, response):
        print response

    def parse_item(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
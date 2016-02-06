import random
from oxygendemo.items import OxygenItem
import scrapy
from pyquery import PyQuery

from oxygendemo.constants import RANDOM_CATEGORY_COUNT


class OxygenSpider(scrapy.Spider):
    name = "oxygenboutique.com"
    base_url = "http://www.oxygenboutique.com/"

    start_urls = ["http://www.oxygenboutique.com"]

    def get_absolute_url(self, href):
        return '{0}{1}'.format(self.base_url, href)

    def parse(self, response):
        pq = PyQuery(response.body)

        category_href_list = [c.attr("href") for c in pq("ul.mega_box ul li a").items()]
        random_category_href_list = random.sample(set(category_href_list), RANDOM_CATEGORY_COUNT)

        for href in random_category_href_list:
            yield scrapy.Request(url=self.get_absolute_url(href), callback=self.parse_category)

    def parse_category(self, response):
        pq = PyQuery(response.body)
        item_href_list = [c.attr("href") for c in pq(".itm a").items()]

        for href in item_href_list[:3]:
            yield scrapy.Request(url=self.get_absolute_url(href), callback=self.parse_item)

    def parse_item(self, response):
        pq = PyQuery(response.body)
        item_data = {
            "name": self.get_name(pq),
            "description": self.get_description(pq),
            "designer": self.get_designer(pq),
        }
        
        yield item_data

    def get_name(self, pq):
        return pq(".right h2").text()

    def get_description(self, pq):
        return pq("#accordion h3:contains('Description')").next().text()

    def get_designer(self, pq):
        return pq("#accordion h3:contains('Designer')").next().text()


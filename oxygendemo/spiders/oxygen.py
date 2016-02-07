import random
from oxygendemo.items import OxygenItem
import scrapy
from pyquery import PyQuery

from oxygendemo.constants import RANDOM_CATEGORY_COUNT


class OxygenSpider(scrapy.Spider):
    name = "oxygenboutique.com"
    base_url = "http://www.oxygenboutique.com/"

    start_urls = ["http://www.oxygenboutique.com"]

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
            "images": self.get_image_urls(pq),
            "sale_discount": self.get_sale_discount(pq),
            "stock_status": self.get_stock_status(pq),
            "code": self.get_code(pq),
            "link": response.request.url,
        }

        yield item_data

    def get_absolute_url(self, href):
        return '{0}{1}'.format(self.base_url, href)

    def get_name(self, pq):
        return pq(".right h2").text()

    def get_description(self, pq):
        return pq("#accordion h3:contains('Description')").next().text()

    def get_designer(self, pq):
        return pq("#accordion h3:contains('Designer')").next().text()

    def get_image_urls(self, pq):
        return [self.get_absolute_url(m.attr("href")) for m in pq(".cloud-zoom-gallery").items()]

    def get_sale_discount(self, pq):
        undiscounted_price = pq(".offsetMark").text()
        if not undiscounted_price:
            return 0

        discount_price = pq(".price .mark").next().text()
        return float(discount_price)/float(undiscounted_price) * 100

    def get_stock_status(self, pq):
        stock_status = {}
        for item in pq("table select option:not(:first-child)").items():
            if item.attr("disabled"):
                size = item.text().replace(" - Sold Out", "")
                stock_status[size] = 3
            else:
                stock_status[item.text()] = 1

        return stock_status

    def get_code(self, pq):
        name = self.get_name(pq)
        code = name.lower().replace(" ", "-")
        return code


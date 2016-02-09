import random
import re
import string
from decimal import Decimal

import scrapy
from pyquery import PyQuery

from oxygendemo.items import OxygenItem
from oxygendemo.utils import find_best_match, clean_price, get_exchange_rates
from oxygendemo.constants import RANDOM_CATEGORY_COUNT, IN_STOCK, OUT_OF_STOCK, TYPE_GUESS_KEYWORDS_MAP, \
    GENDER_GUESS_KEYWORDS_MAP, COLORS


class OxygenSpider(scrapy.Spider):
    name = "oxygenboutique.com"
    base_url = "http://www.oxygenboutique.com/"
    start_urls = ["http://www.oxygenboutique.com"]

    exchange_rates = get_exchange_rates()

    def parse(self, response):
        pq = PyQuery(response.body)

        category_href_list = [c.attr("href") for c in pq("ul.mega_box ul li a").items()]
        random_category_href_list = random.sample(set(category_href_list), RANDOM_CATEGORY_COUNT)

        for href in random_category_href_list:
            yield scrapy.Request(url=self.get_absolute_url(href), callback=self.parse_category_page)

    def parse_category_page(self, response):
        pq = PyQuery(response.body)
        item_href_list = [c.attr("href") for c in pq(".itm table a").items()]
        print item_href_list
        for href in item_href_list:
            yield scrapy.Request(url=self.get_absolute_url(href), callback=self.parse_item_page)

    def parse_item_page(self, response):
        pq = PyQuery(response.body)
        item_data = {
            "name": self.get_name(pq),
            "description": self.get_description(pq),
            "designer": self.get_designer(pq),
            "images": self.get_image_urls(pq),
            "sale_discount": self.get_sale_discount(pq),
            "stock_status": self.get_stock_status(pq),
            "code": self.get_code(pq),
            "gpb_price": self.get_gpb_price(pq),
            "usd_price": self.get_usd_price(pq),
            "eur_price": self.get_eur_price(pq),
            "type": self.get_best_match_type(pq),
            "gender": self.get_best_match_gender(pq),
            "raw_color": self.get_best_match_color(pq),
            "link": response.request.url,
        }
        yield OxygenItem(**item_data)

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
        sale_discount = float(discount_price) / float(undiscounted_price) * 100
        return round(sale_discount, 2)

    def get_stock_status(self, pq):
        stock_status = {}
        for item in pq("table select option:not(:first-child)").items():
            if item.attr("disabled"):
                size = item.text().replace(" - Sold Out", "")
                stock_status[size] = OUT_OF_STOCK
            else:
                stock_status[item.text()] = IN_STOCK

        return stock_status

    def get_code(self, pq):
        name = self.get_name(pq)
        return re.sub(r'\W+', '-', name.lower())

    def get_gpb_price(self, pq):
        pq(".price .mark").remove()
        price_str = pq(".price").text()
        price_decimal = clean_price(price_str)
        return round(price_decimal, 2)

    def get_usd_price(self, pq):
        gpb_price = Decimal(self.get_gpb_price(pq))
        usd_ex_rate = Decimal(self.exchange_rates.get("USD"))
        usd_price = gpb_price * usd_ex_rate
        return round(usd_price, 2)

    def get_eur_price(self, pq):
        gpb_price = Decimal(self.get_gpb_price(pq))
        eur_ex_rate = Decimal(self.exchange_rates.get("EUR"))
        eur_price = gpb_price * eur_ex_rate
        return round(eur_price, 2)

    def get_info_words(self, pq):
        name = self.get_name(pq)
        description = self.get_description(pq)
        designer = self.get_designer(pq)
        item_info = name.lower() + " " + description.lower() + " " + designer.lower()
        item_words = [word.strip(string.punctuation) for word in item_info.split()]
        return item_words

    def get_best_match_type(self, pq):
        info_words = self.get_info_words(pq)
        key_bundle = find_best_match(info_words=info_words, key_map=TYPE_GUESS_KEYWORDS_MAP)
        return key_bundle.get("name")

    def get_best_match_gender(self, pq):
        info_words = self.get_info_words(pq)
        key_bundle = find_best_match(info_words=info_words, key_map=GENDER_GUESS_KEYWORDS_MAP)
        return key_bundle.get("name")

    def get_best_match_color(self, pq):
        info_words = self.get_info_words(pq)

        match_colors = []
        for c in COLORS:
            match_count = info_words.count(c)
            if match_count > 0:
                d = {
                    "name": c,
                    "count": info_words.count(c)
                }
                match_colors.append(d)
        if match_colors:
            match_colors = sorted(match_colors, key=lambda k: k['count'], reverse=True)
            best_match_color = match_colors[0]
            return best_match_color.get("name")
        return None

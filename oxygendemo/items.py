# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
"""
{
   'code': 'le-apron-dress-in-reese',
   'description': 'Le Apron Dress in Reese by Frame Denim. This absolute summer classic is what you need on your warm weekends or festivals. It features hook fastening straps with a front patch pocket. The cotton is very light and the Reese wash is a true denim blue.',
   'designer': 'Frame Denim',
   'gender': 'F',
   'images': ['http://oxygenboutique.com/GetImage/cT0xMDAmdz01NiZoPTExMiZQSW1nPTg3ZTlhZDE0LWUyNDUtNDkzMS05NjMzLWNiZTQ1N2ZkYmE1Yy5qcGc1.jpg',
              'http://oxygenboutique.com/GetImage/cT0xMDAmdz0yNzAmaD00MTAmUEltZz04N2U5YWQxNC1lMjQ1LTQ5MzEtOTYzMy1jYmU0NTdmZGJhNWMuanBn0.jpg'],
   'link': 'http://www.oxygenboutique.com/Le-Apron-Dress-in-Reese.aspx',
   'name': 'Frame Denim Le Apron Dress in Reese',
   'usd_price': '331.50',
   'raw_color': 'blue',
   'sale_discount': 63.0,
   'stock_status': {'L': 1, 'M': 1, 'S': 1, 'XS': 1},
   'type': 'A'
 }
"""


class OxygendemoItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    designer = scrapy.Field()
    gender = scrapy.Field()
    images = scrapy.Field()
    link = scrapy.Field()
    code = scrapy.Field()
    usd_price = scrapy.Field()
    raw_color = scrapy.Field()
    sale_discount = scrapy.Field()
    stock_status = scrapy.Field()
    type = scrapy.Field()
    eur_price = scrapy.Field()
    gpb_price = scrapy.Field()
import scrapy


class OxygenItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    designer = scrapy.Field()
    gender = scrapy.Field()
    images = scrapy.Field(serializer=list)
    link = scrapy.Field()
    code = scrapy.Field()
    usd_price = scrapy.Field()
    raw_color = scrapy.Field()
    sale_discount = scrapy.Field(serializer=float)
    stock_status = scrapy.Field(serializer=dict)
    type = scrapy.Field()
    eur_price = scrapy.Field()
    gpb_price = scrapy.Field()

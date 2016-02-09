Simple Spider Task
==================

Pre-requisites
--------------
- python 2.7
- scrapy http://scrapy.org/
- pyquery

What you need to do
----
- crawl online retailer oxygenboutique.com for appropriate product pages
- return items representing products
- output in json format

What are we going to check
-----
- following rules
- crawl efficiency: ratio of items scraped to requests made
- number of items crawled
- clean code

Instructions
------------
- run "scrapy startproject oxygendemo",
- update items.py in oxygendemo/oxygendemo,
- create oxygen.py in oxygendemo/oxygendemo/spiders,
- write crawling rules (these few lines are a big part of the task - you want to crawl the site in an efficient way),
   - to find appropriate category listing pages,
   - to identify individual product pages (this rule should have a callback='parse_item'),
- fill out parse_item method to populate the item's fields (one method per field),
- don't use `xpath` for getting data, use `pyquery` instead
- (import from standard python libraries where required, but nothing external other than what's already imported),
- run "scrapy crawl oxygenboutique.com -o items.json -t json",
- when satisfied, upload `oxygen.py` and `items.json` to gist and send them to us.

Examples
--------
This url: http://www.oxygenboutique.com/Le-Apron-Dress-in-Reese.aspx could yield an item dictionary:
```python
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
```

Field details
-------------
- **type** - try and make a best guess, one of:
  - 'A' apparel
  - 'S' shoes
  - 'B' bags
  - 'J' jewelry
  - 'R' accessories
- **gender**, one of:
  - 'F' female
  - 'M' male
- **designer** - manufacturer of the item
- **code** - unique identifier from a retailer perspective
- **name** - short summary of the item
- **description** - fuller description and details of the item
- **raw_color** - best guess of what colour the item is (set to None if unidentifiable)
- **image_urls** - list of urls of large images representing the item
- **usd_price** - full (non-discounted) price of the item
- **sale_discount** - percentage discount for sale items where applicable 
- **stock_status** - dictionary of sizes to stock status
  - 1 - out of stock
  - 3 - in stock
- **link** - url of product page

Extra points
------------

- Get correct price of product for GBP and EUR currency
	- **eur_price** - full (non-discounted) price of the item
	- **gpb_price** - full (non-discounted) price of the item

Help
-----------

If you don't know how to start, this is good starting point http://doc.scrapy.org/en/master/topics/spiders.html?highlight=rules#crawlspider-example 
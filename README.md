Simple Spider Task
==================

Example web crawler for Scrapy.

Requirments
--------------
- python 2.7
- Scrapy 1.0.5
- pyquery 1.2.11

```
    pip install -r requirements.txt
```

Usage
-----
```
    scrapy crawl oxygenboutique.com -o items.json -t json
```

Examples
--------
This url: http://www.oxygenboutique.com/Arctic-Fox-iPhone-Case.aspx could yield an item dictionary

```
  {
    "code": "related-arctic-fox-iphone-case",
    "description": "Arctic Fox iPhone Case by Related Apparel. The Arctic Fox print from this seasons Related collection is on this uber cool iPhone case. You can wear the Arctic Fox printed pieces and now have a phone case to match.",
    "sale_discount": 0.0,
    "gender": "F",
    "stock_status": {
      "One Size": 1
    },
    "gpb_price": 10.0,
    "usd_price": 14.42,
    "designer": "Created by two generations of one family, Helen and Joanna Nicola, Related is a new contemporary brand offering stylish and wearable clothing for women. \u00a0Combining femininity with functionality and classic shapes with a hint of playfulness, the collection includes artfully inspired ready-to-wear day and evening pieces that meet the needs of today\u2019s fashion-savvy woman.",
    "link": "http://www.oxygenboutique.com/Arctic-Fox-iPhone-Case.aspx",
    "raw_color": null,
    "images": [
      "http://www.oxygenboutique.com//GetImage/cT0xMDAmdz04MDAmaD02MDAmUEltZz02NGM2ODVmZC0yZjUyLTQ1OGItYWFjNi1lNzEzOGE2NzllYzUuanBn0.jpg"
    ],
    "eur_price": 12.83,
    "type": "A",
    "name": "Related Arctic Fox iPhone Case"
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
- **sale_discount** - percentage discount for sale items where applicable 
- **stock_status** - dictionary of sizes to stock status
  - 1 - out of stock
  - 3 - in stock
- **link** - url of product page
- **usd_price** - full (non-discounted) price of the item
- **eur_price** - full (non-discounted) price of the item
- **gpb_price** - full (non-discounted) price of the item

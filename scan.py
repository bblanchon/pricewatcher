#!/usr/bin/env python
import os
import sys
import re
import urllib2
import lxml.html
from decimal import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricewatcher.settings")

from prices.models import Shop, Reference, Price

price_re = re.compile(r"(\d+).(\d{0,2})")
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def parse_price(string):
    m = price_re.search(string)
    if m and len(m.group(2)) > 0:
        return Decimal(m.group(1) + "." + m.group(2))
    elif m:
        return Decimal(m.group(1))
    else:
        return None 

def download_price(url, css_select):  
    req = urllib2.Request(url, headers={'User-Agent' : user_agent}) 
    html = urllib2.urlopen(req).read()
    soup = lxml.html.fromstring(html)
    matches = soup.cssselect(css_select)
    return parse_price(matches[0].text_content().strip())
 

for shop in Shop.objects.all():

    print shop.name

    for ref in shop.reference_set.all():

        print " Reference: " , ref.name

        try:
            price = download_price(ref.url, shop.css_select)
            print "  Found: " , price

            first_record = ref.price_set.order_by("timestamp").first()
            last_record = ref.price_set.order_by("-timestamp").first()

            if last_record != first_record and last_record.price == price:
                price_record = last_record
            else:
                price_record = Price(reference=ref)

            price_record.price = price
            price_record.save();

            print "  Saved " , price_record.id

        except Exception as e:
            print e




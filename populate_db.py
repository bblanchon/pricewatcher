#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricewatcher.settings")

    from prices.models import Shop, Product

    fnac = Shop.objects.create(
    	name="Fnac", 
    	url_regex=r"http://www\.fnac\.com/.*", 
    	css_select=".promoLabel .userPrice, .bigPricerFA strong.userPrice")

    amazon = Shop.objects.create(
    	name="Amazon", 
    	url_regex=r"http://www\.amazon\.fr/.*", 
    	css_select="#priceblock_ourprice,b.priceLarge")

    boulanger = Shop.objects.create(
    	name="Boulanger", 
    	url_regex=r"http://www\.boulanger\.fr/.*", 
    	css_select="div.price")

    darty = Shop.objects.create(
    	name="Darty", 
    	url_regex=r"http://www\.darty\.com/", 
    	css_select=".darty_prix .darty_big")

    gx7 = Product.objects.create(name="Panasonic GX7")

    gx7.reference_set.create(
        name="Argent 14-42mm (par Amazon)", 
        shop=amazon,
       	url = "http://www.amazon.fr/gp/product/B00FBA2DYK/")

    gx7.reference_set.create(
        name="Argent 14-42mm", 
        shop=boulanger,
       	url = "http://www.boulanger.fr/apn_panasonic_dmc-gx7_argent_14-42mm/p_73612_636226.htm")

    gx7.reference_set.create(
        name="Noir 20mm", 
        shop=boulanger,
        url = "http://www.boulanger.fr/apn_panasonic_dmc-gx7_noir_20mm/p_73612_636184.htm")

    gx7.reference_set.create(
        name="Silver 20mm",
        shop=boulanger,
        url = "http://www.boulanger.fr/apn_panasonic_dmc-gx7_silver_20mm/p_73624_628502.htm")

    gx7.reference_set.create(
    	name="Noir 14-42mm", 
        shop=darty,
       	url = "http://www.darty.com/nav/achat/photo_camescope/appareil_photo_compact/appareil_photo_hybride/panasonic_lumix_dmc-gx7k_noir_14-42_mm.html")

    gx7.reference_set.create(
        name="Argent 20mm", 
        shop=darty,
        url = "http://www.darty.com/nav/achat/photo_camescope/appareil_photo_compact/appareil_photo_hybride/panasonic_lumix_dmc-gx7k_noir_14-42_mm.html")

    gx7.reference_set.create(
    	name="Noir 14-42mm", 
        shop=fnac,
       	url = "http://www.fnac.com/Boitier-Hybride-Panasonic-DMC-GX7-Silver-Obj-Lumix-G-Vario-14-42-mm-F-3-5-5-6/a6207251/w-4")
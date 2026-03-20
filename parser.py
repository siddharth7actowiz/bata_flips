from validation import Store
from lxml import html
import json
from urllib.parse import quote
with open("paths.json","r") as f:
    xpaths=json.load(f)

def parser(data):
      tree=html.fromstring(data)
      sizes = tree.xpath(xpaths["size_xpath"])
      discounts = tree.xpath('//div[@name="discount"]//a/@data-refinement-value')
      brands = tree.xpath('//span[@class="cc-tile-product-brand"]//text()')
      colors=[]
      for cols in tree.xpath('//span[@class="cc-submenu-voice-group cc-p pb-0 text-center mt-1 font-weight-normal"]'):
          colour=cols.xpath('string(.//text())').strip()
          colors.append(colour)  
         #for removing duplicates
      sizes = list(set(sizes))
      discounts = list(set(discounts))
      brands = list(set(brands))
     
      #storing urls
      urls=[]
      BASE_URL="https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{color}/{size}/?prefn1=discountPercent&prefv1={discount}"
      #formatting urls
      for brand in brands:
        brand_slug = brand.lower().replace(" ", "-")   # e.g. BATA SUNSHINE → bata-sunshine
        for col in colors:
            col_slug=quote(col.lower().replace(" ", "-"))
            for size in sizes:
                for discount in discounts:
                    encoded_discount = discount.replace(" ", "%20").replace("%", "%25")

                    url = BASE_URL.format(
                        brand=brand,
                        color=col_slug,
                        size=size,
                        discount=encoded_discount
                    )
                    urls.append({
                    "Brand": brand,   # ✅ correct key
                    "Color": col_slug,
                    "Size": size,
                    "Discount": discount,
                    "Urls": url
})
      print(len(urls))
      
      return urls         

   

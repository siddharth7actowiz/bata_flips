from validation import Store
from lxml import html



def parser(data):
      tree=html.fromstring(data)
     
      sizes = tree.xpath('//div[@name="size"]//a/@data-refinement-value')
      discounts = tree.xpath('//div[@name="discount"]//a/@href')
      brands = tree.xpath('///span[@class="cc-tile-product-brand"]//text()')

     #for removing duplicates
      sizes = list(set(sizes))
      discounts = list(set(discounts))
      brands = list(set(brands))
      #storing urls
      urls=[]
      BASE_URL="https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{size}/?prefn1=discountPercent&prefv1={discount}"
      #formatting urls
      for brand in brands:
        brand_slug = brand.lower().replace(" ", "-")   # e.g. BATA SUNSHINE → bata-sunshine

        for size in sizes:
            for discount in discounts:
                encoded_discount = discount.replace(" ", "%20").replace("%", "%25")

                url = BASE_URL.format(
                    brand=brand_slug,
                    size=size,
                    discount=encoded_discount
                )
                urls.append(url)
      print(len(urls))
      return urls         

   

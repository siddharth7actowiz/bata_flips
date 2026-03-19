from validation import Store
from lxml import html



def parser(data):
      tree=html.fromstring(data)
     
      sizes = tree.xpath('//a[@data-refinement-id="size"]/@data-refinement-value')
      discounts = tree.xpath('//a[@data-refinement-id="discountPercent"]/@data-refinement-value')
      brands = tree.xpath('//a[@data-refinement-id="brand"]/@data-refinement-value')

     
      sizes = list(set(sizes))
      discounts = list(set(discounts))
      brands = list(set(brands))
      urls=[]
      BASE_URL="https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{size}/?prefn1=discountPercent&prefv1={discount}"
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

      return urls         

   

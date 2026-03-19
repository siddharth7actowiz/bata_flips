from pydantic import BaseModel

class Store(BaseModel):
    product_name: str
    product_id: str
    price: float
    discount: float
    discount_price: float
    ratings: float
    quantity: int
    currency: str
    image_url: str = ""
    product_url: str = ""
    brand: str = ""
    availability: str = ""

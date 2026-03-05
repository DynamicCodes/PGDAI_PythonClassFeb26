# work of pydantic for data validation

from pydantic import BaseModel
# import baseModel for data validation,


class Product(BaseModel):    # BaseModel is added to show pydantic, once added remove the below constructor
    id: int
    name: str
    description: str
    price: float
    quantity: int
# below constructor no need after basemodel.
'''
    def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
'''
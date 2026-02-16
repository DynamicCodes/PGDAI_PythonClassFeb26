from fastapi import FastAPI

from models.models import Product

from database.db import session

app = FastAPI()
@app.get("/")
def greet():
    return "welcome to first app"


# for geeting all the products

products = [

    #Product(1, "HP", "budget laptop", 100.11, 1),
    #Product(2, "DELL", "budget laptop", 45.11, 2),


    # for pydantic
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/products")
def get_all_products():
    # create db session
    db = session()
    # perform query
    db.query(Product).all()
    return products

@app.get("/products/{id}")
def get_product_by_id(id:int):
   # return products[id-1]
   for p in products:
       if p.id == id:
           return p

   return "product not found"

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"

    return "product not found"

@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return "product not found"
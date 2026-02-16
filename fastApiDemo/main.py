from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.models import Product

from database.db import session, engine
from database import database_models

from sqlalchemy.orm import Session

app = FastAPI()

# for CORS permission
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
)


# below line for creating table in database through alchemy
database_models.Base.metadata.create_all(bind=engine)

# function for initilizating with data if table is empty in DB else dont do anything
def init_db():
    db = session()

    count = db.query(database_models.Product).count()  # for reloading server without trying to save data again
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

    db.commit()

init_db()
# db = session() is used multiple times, which is bad, as we're not also closeding it.
# so create a function to have one connection
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()



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
def get_all_products(db: Session = Depends(get_db)):    # (db: Session = Depends(get_db) -> when use single db session to inject in the method
    # create db session
    #db = session()
    # perform query
    #db.query(Product).all()
    #return products

    # after db is injected
    db_products = db.query(database_models.Product).all()

    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int, db: Session = Depends(get_db)):   # from DB
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product

    return "product not found"
'''
def get_product_by_id(id:int):  # for list 
   # return products[id-1]
   for p in products:
       if p.id == id:
           return p

   return "product not found"
'''
@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):   # for db
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
'''
# for locla list
def add_product(product: Product):
    products.append(product)
    return product
'''
@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated successfully"
    else:
        return "No product found"
'''
# for local list
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"

    return "product not found"
'''
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "product not found"

'''
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return "product not found"
'''






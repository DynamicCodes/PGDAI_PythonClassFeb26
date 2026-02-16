from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# this file is for pydantic
db_url = "postgresql://postgres:root@localhost:5432/fastapi"   # postgres:root  <- user name and password
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
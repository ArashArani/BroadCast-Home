#کتاب خانه ها 
from sqlalchemy import *
from extentions import db 

#دیتابیس 


class Product(db.Model):
    __tablename__="products"
    id = Column(Integer , primary_key= True)
    name=Column(String,unique=True,nullable=False,index=True)
    description=Column(String ,nullable=False,index=True)
    quantity=Column(Integer,nullable=False , index=True)
    price=Column(String ,nullable=False, index=True)
    active = Column(INTEGER)
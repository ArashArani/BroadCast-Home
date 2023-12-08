#کتاب خانه ها 
from sqlalchemy import *
from extentions import db , get_current_time

#دیتابیس 


class Product(db.Model):
    __tablename__="products"
    id = Column(Integer , primary_key= True)
    name=Column(String,unique=True,nullable=False,index=True)
    decription=Column(String ,nullable=False,index=True)
    quantity=Column(Integer,nullable=False , index=True)
    price=Column(String ,nullable=False, index=True)
    date_created = Column(String(15), default=get_current_time)
    active = Column(INTEGER,nullable=False,)


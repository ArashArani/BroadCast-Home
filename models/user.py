#کتاب خانه ها 
from sqlalchemy import *
from extentions import db , get_current_time
from flask_login import UserMixin

#دیتابیس 


class User(db.Model, UserMixin):
    __tablename__="users"
    id = Column(Integer , primary_key= True)
    username=Column(String,unique=True,nullable=False,index=True)
    password=Column(String ,nullable=False,index=True)
    phone=Column(String (11),nullable=False , index=True , unique=True)
    gmail = Column(String , unique=True , nullable=True)
    first_name = Column(String,index=True , nullable=True)
    last_name = Column(String,index=True,nullable=True)
    address=Column(String , index=True , nullable=True)


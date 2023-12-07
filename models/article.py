#کتاب خانه ها 
from sqlalchemy import *
from extentions import db 

#دیتابیس 


class Article(db.Model):
    __tablename__="articles"
    id = Column(Integer , primary_key= True)
    name = Column(VARCHAR, unique=True, index=True , nullable=False)
    description = Column(VARCHAR, unique=True, index=True , nullable=False)


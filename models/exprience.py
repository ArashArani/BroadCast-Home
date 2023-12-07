#کتاب خانه ها 
from sqlalchemy import *
from extentions import db 

#دیتابیس 


class Experience(db.Model):
    __tablename__="experiences"
    id = Column(Integer , primary_key= True)
    name = Column(VARCHAR, unique=True, index=True , nullable=False)
    description = Column(VARCHAR, unique=True, index=True , nullable=False)


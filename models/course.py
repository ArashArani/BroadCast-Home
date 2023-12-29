#کتاب خانه ها 

from sqlalchemy import *

from extentions import db 

#دیتابیس 


class Course(db.Model):
    __tablename__="courses"
    id = Column(Integer , primary_key= True)
    name = Column(VARCHAR, unique=True, index=True , nullable=False)
    description = Column(VARCHAR, unique=True, index=True , nullable=False)
    teacher = Column(VARCHAR,nullable=True,index=True)
    price = Column (String,index=True,nullable=False)
    active = Column(Integer)

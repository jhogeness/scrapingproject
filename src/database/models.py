from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Sneaker(Base):
    __tablename__ = "sneakers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    name = Column(String)
    reviews_rating_number = Column(Float)
    reviews_amount = Column(Integer)
    old_price = Column(Float)
    new_price = Column(Float)
    _source = Column(String)
    _data_coleta = Column(DateTime, default=datetime.utcnow)
    

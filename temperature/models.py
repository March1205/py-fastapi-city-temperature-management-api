from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from models import Base


class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    date_time = Column(DateTime)
    temperature = Column(Float)
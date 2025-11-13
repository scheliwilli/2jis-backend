from sqlalchemy import create_engine
from sqlalchemy.sql import func
from database import Base

class Place(Base):
    __tablename__ = "places"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    category = Column(String(50))
    
    wheelchair_accessible = Column(Boolean, default=False)
    SIM_accessible = Column(Boolean, default=False)
    LowMobile_accessible = Column(Boolean, default=False)

    
class Rating(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(Integer,nullable=False)
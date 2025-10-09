from sqlalchemy import create_engine
from sqlalchemy.sql import func
from database import Base

class Place(Base):
    __tablename__ = "places"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    category = Column(String(50))
    
    wheelchair_accessible = Column(Boolean, default=False)
    has_ramp= Column(Boolean, default=False)
    has_wide_doors = Column(Boolean, default=False)
    rating = Column(Integer, default=False)
    
    description = Column(Text)
    creaded_at = Column(DateTime(timezone=True), server_default=func.now())
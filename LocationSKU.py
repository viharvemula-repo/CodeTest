from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


Base = declarative_base()


class LocationSKU(Base):
    __tablename__ = "locations_details"

    SKU = Column(Integer, primary_key=True)
    Name = Column(String)
    Location = Column(String)
    Department = Column(String)
    Category = Column(String)
    SubCategory = Column(String)

    def __init__(self, sku=None, name=None, location=None, department=None, category=None, subcategory=None):
        self.SKU = sku
        self.Name = name
        self.Location = location
        self.Department = department
        self.Category = category
        self.SubCategory = subcategory
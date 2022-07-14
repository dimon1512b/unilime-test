from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    asin = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    reviews = relationship("Review")


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True, default=None)
    text = Column(String, nullable=False)
    product_asin = Column(String, ForeignKey("products.asin"))

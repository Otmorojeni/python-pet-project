import re
from sqlalchemy import column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    """Category model."""

    __tablename__ = "categories"

    id = column(Integer, primary_key=True, index=True)
    name = column(String, unique=True, nullable=False, index=True)
    slug = column(String, unique=True, nullable=True, index=True)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse


class ProductBase(BaseModel):
    """Base model for product."""

    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the product.")
    description: Optional[str] = Field(None, max_length=500,
                                       description="The description of the product.")
    price: float = Field(..., gt=0, description="The price of the product.")
    category_id: int = Field(..., description="The ID of the category.")
    image_url: Optional[str] = Field(None, description="The URL of the product image.")

class ProductCreate(ProductBase):
    """Model for creating a product."""
    pass

class ProductResponse(ProductBase):
    """Model for product response."""

    id: int = Field(..., description="The ID of the product.")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime 
    category: CategoryResponse = Field(..., description="The category of the product.")

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    """Model for product list response."""

    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products.")
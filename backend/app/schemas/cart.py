from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    """Base model for cart item."""

    product_id: int = Field(..., description="The ID of the product.")
    quantity: int = Field(..., gt=0, description="The quantity of the product.")

class CartItemCreate(CartItemBase):
    """Model for creating a cart item."""
    pass

class CartItemUpdate(BaseModel):
    """Model for updating a cart item."""

    product_id: int = Field(..., description="The ID of the product.")
    quantity: int = Field(..., gt=0, description="The quantity of the product.")

class CartItem(BaseModel):
    """Model for cart item response."""

    product_id: int
    name: str = Field(..., description="The name of the product.")
    price: float = Field(..., description="The price of the product.")
    quantity: int = Field(..., description="The quantity of the product.")
    subtotal: float = Field(..., description="The subtotal for the cart item.")
    image_url: Optional[str] = Field(None, description="The URL of the product image.")

class CartResponse(BaseModel):
    """Model for cart response."""

    items: list[CartItem] = Field(..., description="The list of cart items.")
    total: float = Field(..., description="The total price of the cart.")
    items_count: int = Field(..., description="The total number of items in the cart.")
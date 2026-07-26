from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    """Base model for category."""

    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the category.")
    slug: str = Field(..., min_length=5, max_length=100,
                      description="The slug of the category.")

class CategoryCreate(CategoryBase):
    """Model for creating a category."""
    pass

class CategoryResponse(CategoryBase):
    """Model for category response."""

    id: int = Field(..., description="The ID of the category.")

    class Config:
        from_attributes = True
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float
    cost: float
    stock: int
    minStock: int
    category: str
    sku: str
    imageUrl: str

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    cost: float | None = None
    stock: int | None = None
    minStock: int | None = None
    category: str | None = None
    sku: str | None = None
    imageUrl: str | None = None

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    cost: float
    stock: int
    minStock: int
    category: str
    sku: str
    imageUrl: str

class Item:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        price: float,
        cost: float,
        stock: int,
        min_stock: int,
        category: str,
        sku: str,
        image_url: str
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.cost = cost
        self.stock = stock
        self.min_stock = min_stock
        self.category = category
        self.sku = sku
        self.image_url = image_url

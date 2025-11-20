from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate, ItemUpdate

class ItemService:
    items = []
    auto_increment = 1

    def obtener_todos(self):
        return self.items

    def crear(self, data: ItemCreate):
        item = Item(
            id=self.auto_increment,
            name=data.name,
            description=data.description,
            price=data.price,
            cost=data.cost,
            stock=data.stock,
            min_stock=data.minStock,
            category=data.category,
            sku=data.sku,
            image_url=data.imageUrl
        )
        self.items.append(item)
        self.auto_increment += 1
        return item

    def obtener(self, id: int):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def actualizar(self, id: int, data: ItemUpdate):
        item = self.obtener(id)
        if not item:
            return None

        if data.name is not None:
            item.name = data.name
        if data.description is not None:
            item.description = data.description
        if data.price is not None:
            item.price = data.price
        if data.cost is not None:
            item.cost = data.cost
        if data.stock is not None:
            item.stock = data.stock
        if data.minStock is not None:
            item.min_stock = data.minStock
        if data.category is not None:
            item.category = data.category
        if data.sku is not None:
            item.sku = data.sku
        if data.imageUrl is not None:
            item.image_url = data.imageUrl

        return item

    def eliminar(self, id: int):
        item = self.obtener(id)
        if not item:
            return False
        self.items.remove(item)
        return True

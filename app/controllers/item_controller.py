from app.services.item_service import ItemService
from app.schemas.item_schema import ItemCreate, ItemUpdate

service = ItemService()

def get_items():
    return service.obtener_todos()

def create_item(data: ItemCreate):
    return service.crear(data)

def get_item(id: int):
    return service.obtener(id)

def update_item(id: int, data: ItemUpdate):
    return service.actualizar(id, data)

def delete_item(id: int):
    return service.eliminar(id)

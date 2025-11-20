from fastapi import APIRouter, HTTPException
from app.controllers import item_controller
from app.schemas.item_schema import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=list[ItemResponse])
def obtener_items():
    return item_controller.get_items()

@router.post("/", response_model=ItemResponse)
def crear_item(data: ItemCreate):
    return item_controller.create_item(data)

@router.get("/{id}", response_model=ItemResponse)
def obtener_item(id: int):
    item = item_controller.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.put("/{id}", response_model=ItemResponse)
def actualizar_item(id: int, data: ItemUpdate):
    item = item_controller.update_item(id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.delete("/{id}")
def eliminar_item(id: int):
    ok = item_controller.delete_item(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"message": "Item eliminado"}

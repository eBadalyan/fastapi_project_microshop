from typing import Annotated

from fastapi import Path, APIRouter


router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{items_id}/")
def get_item_by_id(items_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": items_id,
        },
    }
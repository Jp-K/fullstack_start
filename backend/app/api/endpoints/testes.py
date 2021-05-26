from fastapi import APIRouter, HTTPException, Depends
from typing import Optional, List, Any
from database import crud
from sqlalchemy.orm import Session
from app import deps

router = APIRouter()



@router.get("/")
def read_root(db:Session = Depends(deps.get_db)) -> Any:
    user = crud.user.get(db = db, id = 1)
    if not user:
        raise HTTPException(status_code=404, detail="não encontrei nada não parcero")
    return user


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@router.post("/")
def post_root(liste: List[int]):
    global lista
    lista = liste
    print("deu post: ", lista)
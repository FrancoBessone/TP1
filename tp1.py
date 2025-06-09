from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Mensaje(BaseModel):
        id: Optional[int] = None
        user: str
        mensaje: str

app = FastAPI()

mensajes_db: List[Mensaje] = []

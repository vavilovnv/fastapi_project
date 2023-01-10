import sys
from fastapi import APIRouter
from typing import Optional, Union

from .entity import router

# Объект router, в котором регистрируем обработчики
api_router = APIRouter()
api_router.include_router(router, prefix="/entities", tags=["entities"])

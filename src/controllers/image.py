from fastapi import APIRouter
from services import image as imageService
from fastapi import Request
from dto.image_dto import Image

router = APIRouter(prefix="/image")

@router.post("/predict")
async def predict(image : Image, request : Request):
   return await imageService.predict(image, request)
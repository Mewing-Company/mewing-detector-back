from fastapi import Request
from dto.image_dto import Image

async def predict(image : Image, request: Request):
    try:
        print(image) 
        body = await request.json()
        print(body)
        return 3 
    except Exception as e:
        print(e)
        return e
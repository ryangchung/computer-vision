from fastapi import APIRouter, HTTPException
from schemas.website import Website
from db.db import get_productive_value, add_website
from tensor_model.src.model import predict_productivity, take_screenshot

router = APIRouter()


@router.post("/check-productivity")
def check_productivity(website: Website):
    productive = get_productive_value(website.url)
    if productive is None:
        path = take_screenshot(website.url)
        productive = predict_productivity(path)
        add_website(website.url, productive)
    print({"url": website.url, "productive": productive})

    return {"url": website.url, "productive": productive}

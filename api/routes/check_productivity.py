from fastapi import APIRouter, HTTPException
from schemas.website import Website
from db.db import Database
from tensor.src.model import ProductivityModel

router = APIRouter()
db = Database()
model = ProductivityModel("tensor/model.h5")

@router.post("/check-productivity")
def check_productivity(website: Website):
    productive = db.get_productive_value(website.url)
    if productive is None:
        path = model.take_screenshot(website.url)
        productive = model.predict_productivity(path)
        db.add_website(website.url, productive)
    print({"url": website.url, "productive": productive})

    return {"url": website.url, "productive": productive}

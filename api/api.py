import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import add_website as db_add_website, get_productive_value

# Import model.py
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tensor_model/src"
    )
)
from tensor_model.src.model import predict_productivity, take_screenshot


class Website(BaseModel):
    url: str


def decide_productivity(url: str) -> bool:
    screenshot_path = (
        "../tensor_model/dataset/real_time/"
        + url.replace("/", "$").replace(":", "#")
        + ".png"
    )
    take_screenshot(url)
    return predict_productivity(screenshot_path)


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],  # Allow frontend URL
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )

    @app.get("/")
    def read_root():
        return {"message": "You are not supposed to be here"}

    @app.post("/check-productivity")
    def check_productivity(website: Website):
        productive = get_productive_value(website.url)
        if productive is None:
            productive = decide_productivity(website.url)
            db_add_website(website.url, productive)
        return {"url": website.url, "productive": productive}

    return app


app = create_app()

import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import add_website as db_add_website, get_productive_value


class Website(BaseModel):
    url: str


def decide_productivity(url: str) -> bool:
    # TODO: Call ML model to predict productivity
    return True


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
        return {"message": "Hello, World!"}

    @app.post("/check-productivity")
    def check_productivity(website: Website):
        productive = get_productive_value(website.url)
        if productive is None:
            productive = decide_productivity(website.url)
            db_add_website(website.url, productive)
        return {"url": website.url, "productive": productive}

    return app


app = create_app()

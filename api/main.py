import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.website import Website


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.db import (
    add_website as db_add_website,
    get_productive_value,
    initialize_database,
)

# Import model.py
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tensor_model/src"
    )
)
from tensor_model.src.model import predict_productivity, take_screenshot


def create_app():
    app = FastAPI()

    initialize_database()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post("/check-productivity")
    def check_productivity(website: Website):
        productive = get_productive_value(website.url)
        if productive is None:
            path = take_screenshot(website.url)
            productive = predict_productivity(path)
            db_add_website(website.url, productive)
        print({"url": website.url, "productive": productive})

        return {"url": website.url, "productive": productive}

    return app


app = create_app()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.check_productivity import router as check_productivity_router


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(check_productivity_router)

    return app


app = create_app()

from pydantic import BaseModel

class Website(BaseModel):
    url: str
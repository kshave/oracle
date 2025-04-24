from pydantic import BaseModel

class EnlightenResponse(BaseModel):
    response: str

class HealthResponse(BaseModel):
    status: str
from pydantic import BaseModel


class AIResponse(BaseModel):
    text: str

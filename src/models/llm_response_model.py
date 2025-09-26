from pydantic import BaseModel

class LLMResponseModel(BaseModel):
    response: str
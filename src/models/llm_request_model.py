from typing import List, Literal
from pydantic import BaseModel

class DialogMessage(BaseModel):
    content: str
    role: Literal["system", "user", "assistant"]

class LLMRequestModel(BaseModel):
    prompt: List[DialogMessage]

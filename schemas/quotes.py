from pydantic import BaseModel, constr, ConfigDict
from typing import Optional

class QuoteCreate(BaseModel):
    text: constr(strip_whitespace=True, min_length=1, max_length=500)
    author: Optional[constr(strip_whitespace=True, max_length=100)] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "Your only limit is you",
                "author": "Anonymous"
            }
        }
    )

class QuoteRead(BaseModel):
    id: int
    text: str
    author: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

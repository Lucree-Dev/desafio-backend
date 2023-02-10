from pydantic import BaseModel, Field
from typing import Optional

class Card(BaseModel):
    title: str = Field(min_length=1, max_length=30)
    pan: str = Field(min_length=16, max_length=16)
    expiry_mm: str = Field(regex="\d{2}")
    expiry_yyyy: str = Field(regex="\d{4}")
    security_code: str = Field(min_length=3, max_length=3)
    date: str = Field(regex="\d{2}/\d{2}/\d{4}")
    owner_id: Optional[str]

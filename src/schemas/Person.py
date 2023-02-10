from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=15)
    birthday: str = Field(regex="\d{4}-\d{2}-\d{2}")
    password: str = Field(min_length=6)
    username: str = Field(min_length=1, max_length=15)
    user_id: Optional[str]
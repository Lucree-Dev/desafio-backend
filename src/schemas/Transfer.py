from pydantic import BaseModel, Field

class CreditCard(BaseModel):
    card_id: str

class Transfer(BaseModel):
    friend_id: str
    total_to_transfer: int = Field(ge=1)
    billing_card: CreditCard

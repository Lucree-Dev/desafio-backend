from pydantic import BaseModel


class Auth(BaseModel):
    username: str
    password: str


class Person(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    password: str
    username: str
    user_id: str


class Card(BaseModel):
    card_id: str
    title: str
    PAN: str
    expiry_mm: str
    expiry_yyyy: str
    security_code: str
    date: str


class BillingCard(BaseModel):
    card_id: str


class Transfer(BaseModel):
    friend_id: str
    total_to_transfer: float
    billing_card: BillingCard

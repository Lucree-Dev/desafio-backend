from pydantic import BaseModel

class UserModel(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    password: str
    username: str
    user_id: str

class UserFriendsModel(BaseModel):
      user_id: str
      friend_id: str

class CardModel (BaseModel) :
      user_id: str
      card_id: str
      title: str
      pan: str
      expiry_mm: str
      expiry_yyyy: str
      security_code: str
      date: str

class TransferModel(BaseModel):
      friend_id: str
      total_to_transfer: str
      card_id:str
      
class Bank_statementModel(BaseModel):
      friend_id: str
      user_id: str
      value: str
      date: str
      from_card: str
from fastapi import APIRouter
from fastapi import Depends

from auth.auth import auth_wrapper
from db import BankStatement as BankStatementORM
from db import Card as CardORM
from db import Person as PersonORM
from db import SQLITE_DB

bank = APIRouter()


@bank.get("/bank-statement")
def all_bank_statement(username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            bs_list = []
            query = BankStatementORM.select()
            for bs in query:
                person = PersonORM.select().where(PersonORM.id == bs.user_id).get()
                friend = PersonORM.select().where(PersonORM.id == bs.friend_id).get()
                card = CardORM.select().where(CardORM.id == bs.from_card).get()
                bs_dict = dict(user_id=person.user_id,
                               friend_id=friend.user_id,
                               value=bs.value,
                               date=bs.date,
                               from_card=card.card_id)
                bs_list.append(bs_dict)
            return bs_list
    except Exception as error:
        raise error


@bank.get("/bank-statement/{userid}")
def bank_statement_by_userid(userid: str, username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            person = PersonORM.select().where(PersonORM.user_id == userid).get()
            query = BankStatementORM.select().where(BankStatementORM.user_id == person.id)
            bs_person_list = []
            for bs in query:
                friend = PersonORM.select().where(PersonORM.id == bs.friend_id).get()
                card = CardORM.select().where(CardORM.id == bs.from_card).get()

                bs_dict = dict(
                    user_id=person.user_id,
                    friend_id=friend.user_id,
                    value=bs.value,
                    date=bs.date,
                    from_card=card.card_id
                )
                bs_person_list.append(bs_dict)
            return bs_person_list
    except Exception as error:
        pass

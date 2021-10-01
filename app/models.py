from peewee import *
from .database import conn

db = conn()

class User(Model):
      first_name = TextField()
      last_name = TextField()
      birthday = TextField()
      password = TextField()
      username = TextField()
      user_id = TextField()

      class Meta:
            database = db 

      def insert_users():
            usersList = [
                  {'first_name' : "João", 'last_name' : "das Neves", 'birthday' : "1989-10-01",'password' : "1231", 'username' : "joao_das_neves", 'user_id' : "1"},
                  {'first_name' : "Maria", 'last_name' : "dos Santos", 'birthday' : "1970-09-02",'password' : "1232", 'username' : "maria_dos_santos", 'user_id' : "2"},
                  {'first_name' : "Paulo", 'last_name' : "Araujo", 'birthday' : "1983-08-03",'password' : "1233", 'username' : "paulo_araujo", 'user_id' : "3"},
                  {'first_name' : "Pedro", 'last_name' : "Gomes de Barros", 'birthday' : "2000-07-04",'password' : "1234", 'username' : "pedro_gomes_de_barros", 'user_id' : "4"}
            ]
            User.insert_many(usersList).execute()
    
class UserFriends(Model):
      user_id = TextField()
      friend_id = TextField()

      class Meta:
            database = db

      def insert_friends():

            user_friends =[
                  {'user_id' : "1", 'friend_id' :"2"},
                  {'user_id' : "1", 'friend_id' :"4"},
                  {'user_id' : "4", 'friend_id' :"1"},
                  {'user_id' : "4", 'friend_id' :"3"},
                  {'user_id' : "3", 'friend_id' :"4"},
                  {'user_id' : "2", 'friend_id' :"1"}
            ]

            UserFriends.insert_many(user_friends).execute()

class Card (Model) :
      user_id = TextField()
      card_id = TextField()
      title = TextField()
      pan = TextField()
      expiry_mm = TextField()
      expiry_yyyy = TextField()
      security_code = TextField()
      date = TextField()

      class Meta:
            database = db

      def insert_cards():
            cardsList = [
                  {'user_id' : '1','title' : "Cartão 1", 'pan' : "5527952393064634", 'expiry_mm' : "05",'expiry_yyyy' : "2022", 'security_code' : "656", 'date' : "2015-11-26", 'card_id' : "1"},
                  {'user_id' : '2','title' : "Cartão 2", 'pan' : "2379451656413535", 'expiry_mm' : "01",'expiry_yyyy' : "2025", 'security_code' : "654", 'date' : "2015-05-12", 'card_id' : "2"},
                  {'user_id' : '3','title' : "Cartão 3", 'pan' : "9978451345864468", 'expiry_mm' : "03",'expiry_yyyy' : "2025", 'security_code' : "185", 'date' : "2015-06-11", 'card_id' : "3"},
                  {'user_id' : '4','title' : "Cartão 4", 'pan' : "5523419975545166", 'expiry_mm' : "01",'expiry_yyyy' : "2024", 'security_code' : "143", 'date' : "2015-07-10", 'card_id' : "4"},
                  {'user_id' : '5','title' : "Cartão 5", 'pan' : "5527952393064634", 'expiry_mm' : "07",'expiry_yyyy' : "2025", 'security_code' : "357", 'date' : "2015-08-09", 'card_id' : "5"}
            ]
            Card.insert_many(cardsList).execute()

class Transfer(Model):
      friend_id = TextField()
      total_to_transfer = TextField()
      card_id = TextField() 

      class Meta:
            database = db

      def insert_transfers():
            transferList = [
                  {'friend_id' : '2', 'total_to_transfer' : '100', 'card_id' : '1'},
                  {'friend_id' : '1', 'total_to_transfer' : '100', 'card_id' : '2'}
            ]
            Transfer.insert_many(transferList).execute()



class Bank_statement(Model):
      friend_id = TextField()
      user_id = TextField()
      value = TextField()
      date = TextField()
      from_card = TextField() 

      class Meta:
            database = db

      def insert_bank_statement():
            bank_statmentList = [
                  {'friend_id' : '2', 'user_id' : '1', 'value' : '150.25', 'date' : "2021-08-30", "from_card": "1"},
                  {'friend_id' : '4', 'user_id' : '1', 'value' : '235.65', 'date' : "2021-04-26",  "from_card": "1"}
            ]
            Bank_statement.insert_many(bank_statmentList).execute()



















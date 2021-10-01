from fastapi import FastAPI
from peewee import prefetch
from app import *
from playhouse.shortcuts import model_to_dict, dict_to_model



app = FastAPI()

@app.get("/")
def read_root():
      '''
      Ao descomentar o codigo na rota raiz o banco de dados é criado
      e preenchido automaticamente, em seguido comentar novamente.
      Obs: configurar as informações da sua base de dados no arquivo 
      database.py dentro da pasta app.
      '''

      #User.create_table()
      #User.insert_users()

      #UserFriends.create_table()
      #UserFriends.insert_friends()

      #Card.create_table()
      #Card.insert_cards()

      #Transfer.create_table()
      #Transfer.insert_transfers()

      #Bank_statement.create_table()
      #Bank_statement.insert_bank_statement()


      return "Banco de dados criado com sucesso"
      

@app.post("/account/person")
def insert_user(user : UserModel):

      '''
      Inserindo um novo usuário
      '''

      User.create(
            first_name = user.first_name,
            last_name = user.last_name, 
            birthday = user.birthday, 
            password = user.password, 
            username = user.username, 
            user_id = user.user_id
      )

      return 'salvo com sucesso'


@app.get("/account/friends/{id}") 
def list_friends(id: int):

      '''
      listando os amigos de um determinado usuário
      '''
      user_friends =[]

      for x in UserFriends.select().where(UserFriends.user_id == id) :
           for y in User.select().where(User.user_id == x.friend_id):
            user_friends.append(model_to_dict(y))
      return user_friends


@app.post("/account/card")
def insert_card(card: CardModel):
      '''
      Cadastrando um cartão no banco de dados
      '''
      Card.create(
            user_id = card.user_id,
            card_id = card.card_id, 
            title = card.title, 
            pan = card.pan, 
            expiry_mm = card.expiry_mm,
            security_code = card.security_code,
            date = card.date
      )

      return 'salvo com sucesso'


@app.put("/account/card")
def update_card(card: CardModel):

      '''
      Atualizando informações de um determinado cartão
      '''

      Card.update(
            user_id = card.user_id,
            card_id = card.card_id, 
            title = card.title, 
            pan = card.pan, 
            expiry_mm = card.expiry_mm,
            security_code = card.security_code,
            date = card.date
      ).where(Card.card_id == card.card_id).execute()

      return 'atualizado com sucesso'


@app.delete("/account/card/{id}")
def delete_card(id):

      '''
      Deletando um cartão
      '''

      Card.delete().where(Card.card_id == id).execute()
      return 'deletado com sucesso'

    
@app.get("/account/cards")
def list_cards():
      '''
      pegando  todos os cartões cadastrados no banco
      '''
      cards =[]
      for x in Card.select() :
            cards.append(model_to_dict(x))
      return cards


@app.post("/account/transfer")
def register_transfer(transfer: TransferModel):
      '''
      Efetuando uma transferencia pra um amigo e em seguida
      gerando o extrado da transação
      '''
      Transfer.create(
            friend_id = transfer.friend_id, 
            total_to_transfer = transfer.total_to_transfer, 
            card_id = transfer.card_id, 
      )

      user_billing_card =''

      for card in Card.select().where(Card.card_id == transfer.card_id) :
            user_billing_card = card.user_id

      Bank_statement.create(
            friend_id = transfer.friend_id, 
            user_id = user_billing_card, 
            value =  transfer.total_to_transfer, 
            date = transfer.card_id, 
            from_card = transfer.card_id, 
      )

      return 'salvo com sucesso'


@app.get("/account/transfers")
def transfer_data():

      '''
      Buscando informações de todas as transferencias realizadas
      '''

      transfers =[]
      for x in Transfer.select() :
            transfers.append(model_to_dict(x))
      return transfers
 

@app.get("/account/bank-statement")
def transfer_data():

      '''
      pegando todos os extratos e transacoes no banco
      '''

      bank_statements =[]
      for x in Bank_statement.select() :
            bank_statements.append(model_to_dict(x))
      return bank_statements


@app.get("/account/bank-statement/{id}")
def transfer_data(id):

      '''
      pegando todos os extratos e transacoes de um determinado cliente
      '''

      bank_statements = []

      for x    in Bank_statement.select().where(Bank_statement.user_id == id) :
            bank_statements.append(model_to_dict(x))

      return bank_statements

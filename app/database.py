from peewee import MySQLDatabase

def conn(): 
      return MySQLDatabase('lucree', user='root', password='',host='127.0.0.1')




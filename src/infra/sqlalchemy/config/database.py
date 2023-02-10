from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.environ.get('UID')}:{os.environ.get('PASSWORD')}@{os.environ.get('SERVER')}:3306/{os.environ.get('DATABASE')}?autocommit=True"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

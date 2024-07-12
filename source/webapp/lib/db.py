import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


load_dotenv()

# BUG: возможно прийдется исправить type: str
SQLALCHEMY_DATABASE_URI = str(os.getenv("SQLALCHEMY_DATABASE_URI"))

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

db = SQLAlchemy(model_class=Base)

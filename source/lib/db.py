from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://wkxgrsna:Pdwbcq78MxRZPpURw1Nnh-yLYl5hQySu@cornelius.db.elephantsql.com/wkxgrsna")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


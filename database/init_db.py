from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
DATABASE_URL = "sqlite:///database/quotes.db"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)





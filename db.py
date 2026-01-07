from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///leads.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class LeadDB(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    service = Column(String)
    location = Column(String)
    status = Column(String)

Base.metadata.create_all(engine)

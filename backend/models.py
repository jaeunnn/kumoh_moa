from sqlalchemy import Column, Integer, String
from database import Base

class Bachelor(Base):
    __tablename__ = "bachelor"
    
    not_id = Column(String, primary_key=True)
    not_title = Column(String, nullable=False)
    not_date = Column(String, nullable=False)
    not_url = Column(String, nullable=False)

class Event(Base):
    __tablename__ = "event"
    
    evt_id = Column(String, primary_key=True)
    evt_title = Column(String, nullable=False)
    evt_date = Column(String, nullable=False)
    evt_url = Column(String, nullable=False)

class Cheering(Base):
    __tablename__ = "cheering"
    
    cheer_id = Column(Integer, primary_key=True, autoincrement=True)
    cheer_message = Column(String, nullable=False)

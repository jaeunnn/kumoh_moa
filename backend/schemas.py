from pydantic import BaseModel
from typing import Optional

class BachelorBase(BaseModel):
    not_title: str
    not_date: str
    not_url: str

class BachelorCreate(BachelorBase):
    not_id: str

class Bachelor(BachelorBase):
    not_id: str
    
    class Config:
        from_attributes = True

class EventBase(BaseModel):
    evt_title: str
    evt_date: str
    evt_url: str

class EventCreate(EventBase):
    evt_id: str

class Event(EventBase):
    evt_id: str
    
    class Config:
        from_attributes = True

class CheeringBase(BaseModel):
    cheer_message: str

class CheeringCreate(CheeringBase):
    pass

class Cheering(CheeringBase):
    cheer_id: int
    
    class Config:
        from_attributes = True

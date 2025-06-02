from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Event, Cheering, Bachelor
from schemas import EventCreate, BachelorCreate, CheeringCreate
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Bachelor CRUD
def get_bachelors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bachelor).offset(skip).limit(limit).all()

def get_bachelor(db: Session, bachelor_id: str):
    return db.query(Bachelor).filter(Bachelor.not_id == bachelor_id).first()

def create_bachelor(db: Session, bachelor: BachelorCreate):
    db_bachelor = Bachelor(**bachelor.dict())
    db.add(db_bachelor)
    db.commit()
    db.refresh(db_bachelor)
    return db_bachelor

# Event CRUD
def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()

def get_event(db: Session, event_id: str):
    return db.query(Event).filter(Event.evt_id == event_id).first()

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Cheering CRUD
def get_random_cheering(db: Session):
    return db.query(Cheering).order_by(func.random()).first()

def get_all_cheerings(db: Session):
    return db.query(Cheering).all()

def get_cheering_count(db: Session):
    return db.query(Cheering).count()
    
# Crawlering
def save_events_bulk(db: Session, events_data: List[Dict[str, Any]]):
    try:
        for event_data in events_data:
            existing = db.query(Event).filter(Event.evt_id == event_data['evt_id']).first()
            
            if existing:
                for key, value in event_data.items():
                    setattr(existing, key, value)
            else:
                new_event = Event(**event_data)
                db.add(new_event)
        
        db.commit()
        logger.info(f"이벤트 데이터 저장 완료: {len(events_data)}개")
        
    except Exception as e:
        db.rollback()
        logger.error(f"이벤트 데이터 저장 실패: {e}")
        raise

def save_bachelors_bulk(db: Session, bachelors_data: List[Dict[str, Any]]):
    try:
        for bachelor_data in bachelors_data:
            existing = db.query(Bachelor).filter(Bachelor.not_id == bachelor_data['not_id']).first()
            
            if existing:
                for key, value in bachelor_data.items():
                    setattr(existing, key, value)
            else:
                new_bachelor = Bachelor(**bachelor_data)
                db.add(new_bachelor)
        
        db.commit()
        logger.info(f"학사공지 데이터 저장 완료: {len(bachelors_data)}개")
        
    except Exception as e:
        db.rollback()
        logger.error(f"학사공지 데이터 저장 실패: {e}")
        raise
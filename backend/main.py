from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from sqlalchemy.orm import Session
from typing import List
import logging
from contextlib import asynccontextmanager

from database import get_db, engine
from models import Base
import crud
import schemas
from scheduler import crawler_scheduler

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 라이프사이클 관리"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully!")
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}")
        raise
    
    crawler_scheduler.start()
    logger.info("Application started - Scheduler started")
    
    yield
    
    crawler_scheduler.stop()
    logger.info("Application shutdown - Scheduler stopped")

app = FastAPI(
    title="Crawling API", 
    version="1.0.0",
    lifespan=lifespan
)

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://20.196.104.117"],  # 프론트엔드 주소
    allow_origins=["http://localhost:80"],  # 프론트엔드 주소
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# Health Check
@app.get("/")
async def root():
    return {"message": "Crawling API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Bachelor APIs
@app.get("/bachelors/", response_model=List[schemas.Bachelor])
def read_bachelors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """학사 공지사항 목록 조회"""
    bachelors = crud.get_bachelors(db, skip=skip, limit=limit)
    return bachelors

@app.get("/bachelors/{bachelor_id}", response_model=schemas.Bachelor)
def read_bachelor(bachelor_id: str, db: Session = Depends(get_db)):
    """특정 학사 공지사항 조회"""
    db_bachelor = crud.get_bachelor(db, bachelor_id=bachelor_id)
    if db_bachelor is None:
        raise HTTPException(status_code=404, detail="Bachelor notice not found")
    return db_bachelor

@app.post("/bachelors/", response_model=schemas.Bachelor)
def create_bachelor(bachelor: schemas.BachelorCreate, db: Session = Depends(get_db)):
    """학사 공지사항 생성"""
    return crud.create_bachelor(db=db, bachelor=bachelor)

# Event APIs
@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """이벤트 목록 조회"""
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

@app.get("/events/{event_id}", response_model=schemas.Event)
def read_event(event_id: str, db: Session = Depends(get_db)):
    """특정 이벤트 조회"""
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    """이벤트 생성"""
    return crud.create_event(db=db, event=event)

# Cheering APIs
@app.get("/cheering/random", response_model=schemas.Cheering)
def get_random_cheering_message(db: Session = Depends(get_db)):
    """무작위 응원 메시지 조회"""
    cheering = crud.get_random_cheering(db)
    if cheering is None:
        raise HTTPException(status_code=404, detail="No cheering messages found")
    return cheering

@app.get("/cheering/", response_model=List[schemas.Cheering])
def get_all_cheering_messages(db: Session = Depends(get_db)):
    """모든 응원 메시지 조회 (관리용)"""
    cheerings = crud.get_all_cheerings(db)
    return cheerings

@app.get("/cheering/count")
def get_cheering_count(db: Session = Depends(get_db)):
    """응원 메시지 총 개수"""
    count = crud.get_cheering_count(db)
    return {"total_count": count}

# 크롤링 APIs
@app.post("/crawl/manual")
async def manual_crawl():
    """수동 크롤링 실행"""
    try:
        result = await crawler_scheduler.manual_crawl()
        return result
    except Exception as e:
        logger.error(f"Manual crawling failed: {e}")
        raise HTTPException(status_code=500, detail="Crawling failed")

@app.get("/crawl/status")
async def crawl_status():
    """크롤링 스케줄러 상태 확인"""
    return {
        "scheduler_running": crawler_scheduler.scheduler.running,
        "jobs": len(crawler_scheduler.scheduler.get_jobs())
    }

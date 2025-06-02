from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import logging
from database import SessionLocal
from crawlers.event_crawler import EventCrawler
from crawlers.bachelor_crawler import BachelorCrawler
import crud

logger = logging.getLogger(__name__)

class CrawlingScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.event_crawler = EventCrawler()
        self.bachelor_crawler = BachelorCrawler()
    
    async def crawl_all_data(self):
        logger.info("Starting scheduled crawling...")
        
        try:
            await self._crawl_events()
            await self._crawl_bachelors()
            
            logger.info("Scheduled crawling completed!")
            
        except Exception as e:
            logger.error(f"Scheduled crawling failed: {e}")
    
    async def manual_crawl(self):
        logger.info("Starting manual crawling...")
        
        try:
            await self._crawl_events()
            await self._crawl_bachelors() 
            
            logger.info("Manual crawling completed!")
            return {"message": "Manual crawling completed successfully"}
            
        except Exception as e:
            logger.error(f"Manual crawling failed: {e}")
            return {"message": f"Manual crawling failed: {str(e)}"}
    
    async def _crawl_events(self):
        try:
            events_data = await self.event_crawler.crawl()
            if events_data:
                db = SessionLocal()
                try:
                    crud.save_events_bulk(db, events_data)
                finally:
                    db.close()
        except Exception as e:
            logger.error(f"Events crawling failed: {e}")
    
    async def _crawl_bachelors(self):
        try:
            bachelors_data = await self.bachelor_crawler.crawl()
            if bachelors_data:
                db = SessionLocal()
                try:
                    crud.save_bachelors_bulk(db, bachelors_data)
                finally:
                    db.close()
        except Exception as e:
            logger.error(f"Bachelors crawling failed: {e}")
    
    def start(self):
        # 자정마다 실행 (0시 0분)
        self.scheduler.add_job(
        self.crawl_all_data,
        CronTrigger(hour='*/6', minute=0, timezone='Asia/Seoul'),
        id="test_crawling",
        replace_existing=True
    )
        
        self.scheduler.start()
        logger.info("Crawler scheduler started")
    
    def stop(self):
        self.scheduler.shutdown()
        logger.info("Crawler scheduler stopped")

crawler_scheduler = CrawlingScheduler()
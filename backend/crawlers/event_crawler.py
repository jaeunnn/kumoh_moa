import asyncio
import time
from typing import List, Dict, Any
from .base_crawler import BaseCrawler
import logging

logger = logging.getLogger(__name__)

class EventCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.kumoh.ac.kr/ko/sub06_01_01_02.do"
    
    async def crawl(self) -> List[Dict[str, Any]]:
        """행사안내 크롤링"""
        logger.info("행사안내 크롤링 시작...")
        
        try:
            soup = await self.fetch_page(self.base_url)
            board_table = soup.select_one('#jwxe_main_content > div.contents-wrapper > div.board-area.ko.board.list > div.board-list01 > table > tbody')
            
            if not board_table:
                logger.warning("게시판 테이블을 찾을 수 없습니다.")
                return []
            
            rows = board_table.find_all('tr')
            events = []
            
            for row in rows:
                try:
                    event_data = await self._extract_event_data(row)
                    if event_data:
                        events.append(event_data)
                        # 부하 방지를 위한 작은 딜레이
                        await asyncio.sleep(0.1)
                except Exception as e:
                    logger.error(f"행사 데이터 추출 실패: {e}")
                    continue
            
            logger.info(f"행사안내 크롤링 완료: {len(events)}개 항목")
            return events
            
        except Exception as e:
            logger.error(f"행사안내 크롤링 실패: {e}")
            return []
    
    async def _extract_event_data(self, row) -> Dict[str, Any]:
        """행 데이터에서 이벤트 정보 추출"""
        # 게시글 번호 추출
        number_element = row.select_one('td.number')
        if not number_element or not number_element.get_text(strip=True):
            return None
        
        evt_id = number_element.get_text(strip=True)
        
        # 제목 추출
        title_element = row.select_one('td.title.left > a > span.title-wrapper')
        if not title_element:
            title_element = row.select_one('td.title.left > a')
        
        if not title_element:
            return None
        
        evt_title = title_element.get_text(strip=True)
        
        # 등록일 추출
        date_element = row.select_one('td.date')
        if not date_element:
            return None
        
        evt_date = date_element.get_text(strip=True)
        
        # URL 추출
        url_element = row.select_one('td.title.left > a')
        if not url_element or not url_element.get('href'):
            return None
        
        href = url_element.get('href')
        if href.startswith('?') or href.startswith('&'):
            evt_url = self.base_url + href
        else:
            evt_url = href
        
        return {
            'evt_id': evt_id,
            'evt_title': evt_title,
            'evt_date': evt_date,
            'evt_url': evt_url,
        }
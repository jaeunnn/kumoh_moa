import requests
from bs4 import BeautifulSoup
import logging
from typing import List, Dict, Any
import asyncio

logger = logging.getLogger(__name__)

class BaseCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    async def fetch_page(self, url: str) -> BeautifulSoup:
        """웹페이지를 비동기로 가져와서 BeautifulSoup 객체 반환"""
        try:
            # 비동기적으로 실행하기 위해 run_in_executor 사용
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.session.get(url, timeout=10)
            )
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
            
        except requests.RequestException as e:
            logger.error(f"웹페이지 요청 실패 ({url}): {e}")
            raise
        except Exception as e:
            logger.error(f"페이지 파싱 실패 ({url}): {e}")
            raise
    
    async def crawl(self) -> List[Dict[str, Any]]:
        """크롤링 실행 (하위 클래스에서 구현)"""
        raise NotImplementedError("하위 클래스에서 구현해야 합니다")
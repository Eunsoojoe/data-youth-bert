# task 01 _ URL 열기, URL과 대화하는 것처럼.
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import os
import time
import urllib.request

# parameter : driver(driver가 있어야지만 접속 가능), url
driver_path = "C:/Users/Admin/Desktop/Data_youth/Resources/chromedriver.exe"
url = 

# get chromedriver (가상 브라우저를 크롬과 연동시킨다.)
browser = webdriver.Chrome(executable_path=driver_path) #파일 창 열어주기
#webdriver 라이브러리 중 chrome을 여는 기능을 쓸 것이야. path는 driver_path를 쓸 것이야.

# open the url
browser.get(url)   #browser에서 나는 url을 가지고 올 것이다. brower를 통해 url을 열 것이다.

# # get linkes of 'more'
# page = browser.page_source #page에서 source 가지고 와
# soup = BeautifulSoup(page, "html.parser") #page의 html 텍스트를 parsing해서 soup로 저장

# 검색어 입력
QUERY = '위드 코로나'
serach_query = urllib.parse.urlencode({'query': QUERY}, encoding='utf-8')
URL = f"https://www.youtube.com/c/newskbs/{seary_query}"

link_pattern = "https://www.youtube.com/c/newskbs/?"

more_links = soup.find_all('div',{'class' : 'W9yFB'}) # get classes(first parsing)
print(more_links)


# 검색 결과 내 링크 찾기 : news.naver.come으로 시작하는 모든 링크 반환
def get_news_links(link_pattern):
    links = []
    links_number = 0
 


           

    print(f"총 {len(links)}개의 뉴스를 찾았습니다.")  # 확인용
    return links









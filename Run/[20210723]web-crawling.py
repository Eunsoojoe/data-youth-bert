# task 01 _ URL 열기, URL과 대화하는 것처럼.
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# parameter : driver(driver가 있어야지만 접속 가능), url
driver_path = "../Resources/chromedriver"
url = "https://play.google.com/store/apps/top/category/GAME"

# get chromedriver (가상 브라우저를 크롬과 연동시킨다.)
browser = webdriver.Chrome(executable_path=driver_path) #파일 창 열어주기
#webdriver 라이브러리 중 chrome을 여는 기능을 쓸 것이야. path는 driver_path를 쓸 것이야.

# open the url
browser.get(url)   #browser에서 나는 url을 가지고 올 것이다. brower를 통해 url을 열 것이다.

# get linkes of 'more'
page = browser.page_source #page에서 source 가지고 와
soup = BeautifulSoup(page, "html.parser") #page의 html 텍스트를 parsing해서 soup로 저장
#개발자 도구를 보니 '더보기' 버튼의 class가 모두 'W9YFB'였다.
#class를 기준으로 1차적 파싱
more_links = soup.find_all('div',{'class' : 'W9yFB'}) # get classes(first parsing)
print(more_links)

# get href(link)
count = 0
more_link_list = []
for more_link in more_links:
    each_more_link = "https://play.google.com"+more_link.a['href'] #설명 필요!
    browser.get(each_more_link)    # 각각의 더보기 링크 접속

    each_more_page = browser.page_source
    each_more_soup = BeautifulSoup(page, "html.parser")
    each_more_games = soup.find_all('div', {'class': 'wXUyZd'})


    # for every link, 각 게임에 대해서
    game_list = []
    for game in each_more_games:
        each_game_link = "https://play.google.com"+game.a['href']
        browser.get(each_game_link)
        game_info_page = browser.page_source
        game_info_soup = BeautifulSoup(game_info_page, "html.parser")

        game_title = game_info_soup.find('h1', {'class': 'AHFaub'}).text
        game_info_des = game_info_soup.find('div', {'jsname': 'sngebd'}).text

        game_info_list = [game_title,game_info_des,each_game_link]
        game_list.append(game_info_list)

    game_info_df= pd.Dataframe(game_list,column=['title','discription','url'])

    save_fname = '../output/game_info_'+str(count)+'.csv'
    game_info_df.to_csv(save_fname,encoding ='utf-8-sig')
    count=+1
    browser.exit()


exit()

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions

wd = "./chromedriver"  # 다운 받은 웹드라이버 위치
addr = "http://m.sports.news.naver.com/kbaseball/news/read.nhn?oid=108&aid=0002688114&m_view=1&sort=LIKE" 
# 크롤링하고자하는 사이트 주소
# 개인적으론 모바일 페이지로 하는게 더 가볍고 빠를것같은 기분이 든다.

driver = webdriver.Chrome(wd)
driver.get(addr)

pages = 0 # 한 페이지당 약 20개의 댓글이 표시
try:
    while True: # 댓글 페이지가 몇개인지 모르므로.
        driver.find_element_by_css_selector(".u_cbox_btn_more").click()
        time.sleep(1.5)
        print(pages, end=" ")
        pages+=1
    
except exceptions.ElementNotVisibleException as e: # 페이지 끝
    pass
    
except Exception as e: # 다른 예외 발생시 확인
    print(e)

    
html = driver.page_source
dom = BeautifulSoup(html, "lxml")

# 댓글이 들어있는 페이지 전체 크롤링
comments_raw = dom.find_all("span", {"class" : "u_cbox_contents"})

# 댓글의 text만 뽑는다.
comments = [comment.text for comment in comments_raw]

comments[:3]


# 결과
['경기 지고있는데 쪼개고있던 이대호는 우리 정서에 맞아서 안까이냐?',
 '메이저리그 였으면 빈볼 타석마다 맞고 벤치클리어링 나서 오도어가 죽탱이 한대 칠만한 일인데.. 로저스가 과연 믈브였어도 저렇게 할 수 있었을까 싶다.',
 '다음부터는 자제 좀 하기를']









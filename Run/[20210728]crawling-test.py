# import module
import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import URLError, HTTPError
from selenium import webdriver
import time
import csv
import re
import pandas as pd
import openpyxl
import xlrd
import xlsxwriter

# 변수 설정
QUERY = '비트코인 "파이어족"'
serach_query = urllib.parse.urlencode({'query':QUERY},encoding = 'utf-8')
URL = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&{serach_query}\
    &sort=0&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all"

link_pattern = "https://news.naver.com/main/read.naver?"
search_PAGE = 8

# driver 설정
driver_path = 'Resources\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 검색 결과 내 링크 찾기 : news.naver.come으로 시작하는 모든 링크 반환
def get_news_links(page_num, link_pattern):
    links = []
    for page in range(page_num):
        print(f"Scrapping page : {page+1}")
        req = requests.get(f"{URL}&start={10*page+1}");
        soup = BeautifulSoup(req.text,'lxml')
        results = soup.find_all('a',{'href': re.compile(link_pattern)})  
        for result in results:
            links.append(result['href'])

    print(f"총 {len(links)}개의 뉴스를 찾았습니다.")  # 확인용
    return links

# 한 페이지 별로 필요한 정보 스크레이핑
def extract_info(url, wait_time = 1, delay_time = 0.3):
    driver.implicitly_wait(wait_time)
    driver.get(url)

    # 댓글 창 있으면 다 '더보기' 클릭
    while True:
        try:
            more_comments = driver.find_element_by_css_selector('u_cbox_in_view_comment')
            more_comments.click()
            time.sleep(delay_time)

        except:
            break

    # html 페이지 읽어오기
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')

    try:
        # 기사 제목
        title = soup.find('h3',{'id':'articleTitle'}).get_text(strip=True)

        # 기사 날짜
        article_time = soup.find('span',{'class':'t11'}).get_text(strip=True)

        # 언론사
        press = soup.find('div',{'class':'press_logo'}).find('a').find('img')['title']

        reply = []

        # 댓글 내용
        contents = soup.find_all("span",{"class":"u_cbox_contents"})
        contents = [content.text for content in contents]

        # 취합
        reply_number = 0
        
        for i in contents:
            reply_number = reply_number + 1
            naver_result = [press,title,article_time, i]
            results_test.append(naver_result)
            print(i)
            print(naver_result)
            print("------")
            if reply_number > 10:
                break 
            
        print("완료")
        return results_test

    except:
        print("오류")
        


# 각 페이지 돌면서 스크래핑
def extract_contents(links):
    Contents = []
    for link in links:
        Content = extract_info(f"{link}&m_view=1")  # 각각의 링크에 대해 extract_info 호출
        Contents.append(Content)                    # extract_info의 결과로 나오는 dic 저장
    return Contents


# 모든 작업 진행
def main():
    global search_PAGE
    news_links = get_news_links(search_PAGE, link_pattern)
    result = extract_contents(news_links)
    driver.quit()
    return result
    print(result[0])



# 출력 결과 저장
def save_to_file(lst):
    file = open('test7.csv', mode="w",encoding = "UTF-8")
    writer = csv.writer(file)
    writer.writerow(['press','title','article_time','contents'])

    for result in lst:
        writer.writerow(list(result.values()))
    file.close()
    return
    
results_test = []
NAVER_RESULT = main ()
save_to_file(NAVER_RESULT)

r_csv = pd.read_csv("test7.csv")

save_xlsx = pd.ExcelWriter("test7.xlsx")
r_csv.to_excel(save_xlsx, index = False) 

save_xlsx.save()





















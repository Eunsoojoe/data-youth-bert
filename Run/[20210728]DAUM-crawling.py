from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup as bs

import pandas as pd
import time

url = "https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EB%B0%B1%EC%8B%A0%EC%A0%91%EC%A2%85%20%22%EC%9C%84%ED%83%81%EC%83%9D%EC%82%B0%22"
web = requests.get(url).content
source = bs(web, 'html.parser')

# for urls in source.find_all('h2', {'class': "service"}):
#     new_url_content = urls["href"]
#     print(new_url_content)

urls_list = []
for urls in source.find_all('a', {'class': "tit_main ff_dot"}):
    new_url_content = urls["href"][-21:-4]
    new_url = "https://news.v.daum.net/v/" + new_url_content

    urls_list.append(new_url)

urls_list
driver_path = 'Resources\chromedriver.exe'  # driver path
driver = webdriver.Chrome(executable_path=driver_path)

contents_list = []
results_list = []

for i in range(10):
    driver.get(urls_list[i])
    # print(driver.current_url)

    time.sleep(3)
    #print(driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[3]/button').text)
    try:
        while driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[3]/button').text != '':
            driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[3]/button').click()
            time.sleep(3)
    except:
        pass


    time.sleep(2)


    # html 페이지 읽어오기
    html = driver.page_source
    soup = bs(html, 'lxml')

    try:
        # 기사 제목
        title = soup.find('h3', {'class': 'tit_view'}).get_text(strip=True)

        # 기사 날짜
        article_time = soup.find('span', {'class': 'num_date'}).get_text(strip=True)

        # 언론사
        press = soup.find('em', {'class': 'info_cp'}).find('a').find('img')['alt']

        reply = []

        # 댓글 내용
        for k in range(1, 30):
            try:
                contents = driver.find_element_by_xpath(
                    '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[4]/div/div/div/div/div[3]/ul[2]/li[' + str(
                        k) + ']/div/p').text
                contents = contents.replace("\n", " ")
                print(contents)
                url_daum = ""
                daum_result = [press,url_daum, title, article_time, contents]
                print(daum_result)
                results_list.append(daum_result)
            except:
                pass
    except:
        pass
print(results_list)
results_df = pd.DataFrame(results_list)
results_df.columns = ['channel','url','title','date','command']
results_df.to_excel('./백신접종_경제2_다음.xlsx',encoding='utf-8-sig')


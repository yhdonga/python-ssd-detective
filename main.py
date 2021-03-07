import os
from time import sleep #지정한 초만큼 여유를 주는 것
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
# from private import private 

driver_path = r"/Users/mun-yeonghun/Workspace/chromedriver_mac"
driver_name = "chromedriver"
driver_path = os.path.join(driver_path,driver_name)
driver = webdriver.Chrome(driver_path)
base_url = r"https://www.naver.com/"
# login_url = r"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

# driver.get(login_url)
# sleep(3)

# my_id = private["id"]
# my_pw = private["pw"]
# naver_id = driver.find_element_by_id("id")
# naver_pw = driver.find_element_by_id("pw")
# sleep(2)

# naver_id.click()
# pyperclip.copy(my_id)
# naver_id.send_keys(Keys.COMMAND, 'v')
# sleep(2)
# naver_pw.click()
# pyperclip.copy(my_pw)
# naver_pw.send_keys(Keys.COMMAND, 'v')
# sleep(2)

# driver.find_element_by_id("log.login").click()
# sleep(2)

news_urls = {
    "조선일보" : "https://news.naver.com/main/ranking/office.nhn?officeId=023",
    "한겨레" : "https://news.naver.com/main/ranking/office.nhn?officeId=028"
}

driver.get(news_urls["조선일보"])
news_list_box = driver.find_elements_by_class_name("rankingnews_list")[1]
news_lists = news_list_box.find_elements_by_tag_name("li")
top_rank_news = news_lists[0]
top_rank_news.find_element_by_tag_name("a").click()
driver.find_element_by_id("articleTitleCommentCount").click()
sleep(2)
while True:
    try:
        driver.find_element_by_class_name("u_cbox_box_more").click()
        sleep(0.2)
    except:
        break

cboxs = driver.find_elements_by_class_name("u_cbox_comment_box")
cbox = cboxs[0]
nickname = cbox.find_element_by_class_name("u_cbox_nick").text
print(nickname)
date = cbox.find_element_by_class_name("u_cbox_date").text
print(date)
contents = cbox.find_element_by_class_name("u_cbox_contents").text
print(contents)
like = cbox.find_element_by_class_name("u_cbox_cnt_recomm").text
print(like)
dislike = cbox.find_element_by_class_name("u_cbox_cnt_unrecomm").text
print(dislike)
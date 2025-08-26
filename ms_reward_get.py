from random import uniform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


import time
import random
import os


keywords=["玉米的功效","洗澡水","corazon的意思","飞天意面教","windows","liquid","下雨","下雪","冰雹","飓风","台风","大西洋","印度洋",
          "selenium","泰康人寿","北京大学","清华大学","中国人大","昌平邮编","泰山","泰安","青岛","斯通或与","文言文的历史","全球通史",
          "ox","butter","juggle","spelunker","justice","er","et","mandare","mandate","mandariin","斜率","交线",
          "印度洋","北京化工大学","211","985","110","警察局","vpn","局域网","shit","orphone","iphone","xiaomi",
          "ipad","oled","lcd","macbook air","macbook pro","macmini","macstudio","iphone16pro","iphone16promax","iphone16plus","iphone16e","apple",
          "tesla","保险","中间人士","平凡之路","脑残","中国近代史","谷歌","泡沐","邓紫棋","周杰伦","bibe","babs","意大利首都"]

options=Options()
options.add_argument('--disable-gpu')
driver=webdriver.Edge(options=options)

email=os.getenv("MS_EMAIL")
password=os.getenv("MS_PASSWORD")

try:
    driver.get("https://rewards.bing.com/")
    time.sleep(uniform(4,6))
    if "login.live.com" in driver.current_url:
        print("需要登陆，正在执行登录")
        driver.find_element(By.NAME,"loginfmt").send_keys(email)
        driver.find_element(By.ID,"idButton9").click()
        time.sleep(uniform(7,10))
        driver.find_element(By.NAME, "passwd").send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(uniform(9,11))
        print("登陆完成")

    driver.get("https://www.bing.com")
    time.sleep(uniform(7,8))


    for i in range(40):
        search_query=random.choice(keywords)
        search_box=driver.find_element(By.NAME,"q")
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(4, 7))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * Math.random());")
        time.sleep(random.uniform(7, 15))
        print(f"Search {i+1}/40: {search_query}")

    print("搜索完成，积分应已累积！请检查 https://rewards.microsoft.com/")

finally:
    driver.quit()
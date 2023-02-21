from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver.get("https://www.yanolja.com/")

hotelbtn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/section[1]/section/section/section[2]/div/a[2]')
hotelbtn.click()
driver.implicitly_wait(3)
# areas = driver.find_elements(By.CLASS_NAME, 'SubhomeRegionList_region2DepthItem__3gARE')

potent = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div[2]/ul/li[1]/a')
    # 인기지역 클릭
potent.click()

href_list = []
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
link = soup.select('a.SubhomeRegionList_region2DepthItem__3gARE')
for i in link:
    href = i['href']
    href_list.append(href)
# areas_list = []
# areas = driver.find_elements(By.CLASS_NAME, 'SubhomeRegionList_region2DepthItem__3gARE')
# for area in areas:
#     areas_list.append(area)
# # areas_list에 인기지역 6곳 추가 완료.

i = 0
for i in range(len(href_list)):
    driver2.get('https://www.yanolja.com' + href_list[i])
    driver2.implicitly_wait(3)
    # html = driver.page_source # page의 html 소스를 받아오기
    # soup = BeautifulSoup(html, 'html.parser') # html 소스를 컴퓨터 언어로 전환
    # names = soup.select('div.PlaceListTitle_container__qe7XH > strong')
    names = driver2.find_elements(By.CLASS_NAME, 'PlaceListTitle_text__2511B.normal')
    # names = 리스트 형태로 저장.
    rates = driver2.find_elements(By.CLASS_NAME, 'PlaceListScore_rating__3Glxf')
    if i == 4:
        areaname = driver2.find_element(By.CLASS_NAME, 'PlaceListTitle_small__aZtDV').text
    else:
        areaname = driver2.find_element(By.CLASS_NAME, 'PlaceListTitle_normal__318s-').text
    print(areaname)
    print('---------------------')
    num = 0
    for name, rate in zip(names, rates): # zip 함수 알고리즘
        if num == 5:
            break
        else:
            num += 1
            print(name.text, rate.text)
    print('---------------------')
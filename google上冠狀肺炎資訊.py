from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
#找到輸入框

q = driver.find_element_by_name('q')
q.send_keys('武漢肺炎')

q.send_keys(Keys.RETURN)

driver.page_source

soup = BeautifulSoup(driver.page_source, 'lxml')

for ele in soup.select('#kp-wp-tab-overview h3'):
    print(ele.text)
    

for p in range(7):
    driver.find_element_by_link_text('下一頁').click()
    soup = soup = BeautifulSoup(driver.page_source, 'lxml')
    for ele in soup.select('#rso h3'):
        print(ele.text) 
    time.sleep(1)


driver.close()
driver.quit() 
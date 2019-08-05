from selenium import webdriver
import time

baidu = webdriver.Chrome()
baidu.get("http://www.baidu.com")
time.sleep(5)

elements = baidu.find_elements_by_tag_name('a')

for element in elements:
    print(element.text)
    if "视频" in element.text:
        element.click()



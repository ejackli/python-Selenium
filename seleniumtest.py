from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

website= webdriver.Chrome()
website.get("http://www.google.com")
#website.fullscreen_window()
website.find_element_by_name("q").send_keys("selenium\n")

#不可以运行
#website.find_element_by_link_text('Google Search').click()
#website.find_element_by_name("btnK").click()
#website.find_element_by_css_selector("[jsname] [value='Google Search']").click()

#可以运行
website.back()
website.find_element_by_name("q").send_keys("youtube")
website.find_element_by_name("q").send_keys(Keys.RETURN)
#website.find_element_by_name("q").submit()

time.sleep(5)
website.quit()
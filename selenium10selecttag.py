from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

page = webdriver.Chrome()
page.get("https://www.timeanddate.com/")

page.find_element_by_css_selector("[title='Time Zone and other travel tools']").click()
page.back()
#Select(page.find_element_by_id("month")).select_by_visible_text("December")

#selectElements = page.find_element_by_id("month")
selectElements = page.find_element_by_css_selector(r"[onchange='document\.cf\.typ\[1\]\.checked\=true']")
months = Select(selectElements)
#months.select_by_visible_text('December')
months.select_by_value('12')
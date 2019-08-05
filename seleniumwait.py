from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://www.google.com")

js='window.open("https://www.timeanddate.com/");'      #打开新窗口
driver.execute_script(js)

windows = driver.window_handles   #获取句柄的list
driver.switch_to.window(windows[1])  #切换句柄到第二个窗口

# 等待：
element = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Time Difference Calculator']"))
)
element.click()


# 等待元素出现在DOM
#WebDriverWait(self._driver).until(EC.presence_of_element_located((By.ID, value)))

# 等待元素显示在页面
#WebDriverWait(self._driver,10).until(EC.visibility_of_element_located((By.NAME, value)))

# 等待元素从页面消失
#WebDriverWait(self._driver, 10, 0.2).until_not(EC.visibility_of_element_located((By.CLASS_NAME, value))))

# 等待页面的title显示
#WebDriverWait(self._driver, 5,0.2).until(EC.title_contains(title))


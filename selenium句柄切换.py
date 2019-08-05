from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

js='window.open("https://www.timeanddate.com/");'      #打开新窗口
driver.execute_script(js)

h1= driver.current_window_handle    #获取当前句柄
print("h1=" + h1)                   #打印当前句柄

windows = driver.window_handles   #获取句柄的list
for i in windows:                  #打印句柄list
    print(i )

driver.switch_to.window(windows[1])  #切换句柄到第二个窗口


h2= driver.current_window_handle    #获取当前句柄
print("h2=" + h2)                   #打印当前句柄




driver.find_element_by_css_selector("[title='Time Zone and other travel tools']").click()
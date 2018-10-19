from selenium import webdriver
#控制浏览器
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
#driver.find_element_by_css_selector("/html/body/div[1]/div[1]/div/div[3]/a[1]").click()
driver.find_element_by_xpath("//*[@id='kw']").send_keys("测试")
driver.find_element_by_xpath("//*[@id='su']").click()
#返回true
element=WebDriverWait(driver,5,0.5).until(EC.title_is("测试_百度搜索"))
print(element)
#find_elements_by_id() 定位一组元素


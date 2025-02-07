from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=r'C:\Webdriver\geckodriver.exe')
driver = webdriver.Firefox(service=service)

print('打开浏览器')
driver.get('https://github.com')
# 在此处添加其他操作（如查找元素、点击按钮等）

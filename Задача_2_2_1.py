from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/selects1.html')
x = int(driver.find_element_by_id('num1').text)
y = int(driver.find_element_by_id('num2').text)
solve = x + y


select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(solve)) # ищем элемент с текстом "Python"
driver.find_element_by_tag_name('button').click()

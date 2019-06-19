from selenium import webdriver
import math, os, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/math.html')
x = int(driver.find_element_by_id('input_value').text)

driver.find_element_by_id('answer').send_keys(str(calc(x)))

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

driver.find_element_by_id('robotCheckbox').click()
driver.find_element_by_id('robotsRule').click()

button.click()

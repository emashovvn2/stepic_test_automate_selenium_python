from selenium import webdriver
import math, os, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/get_attribute.html')
x = int(driver.find_element_by_id('treasure').get_attribute('valuex'))

driver.find_element_by_id('answer').send_keys(str(calc(x)))
driver.find_element_by_id('robotCheckbox').click()
driver.find_element_by_id('robotsRule').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/form/div/div/button').click()

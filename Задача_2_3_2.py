from selenium import webdriver
import math, os, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/alert_accept.html')
driver.find_element_by_tag_name('button').click()
confirm = driver.switch_to.alert
confirm.accept()
time.sleep(3)
x = int(driver.find_element_by_id('input_value').text)
driver.find_element_by_id('answer').send_keys(str(calc(x)))
driver.find_element_by_tag_name('button').click()

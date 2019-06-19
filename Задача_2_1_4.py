from selenium import webdriver
import math, os, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('https://suninjuly.github.io/execute_script.html')
x = int(driver.find_element_by_id('input_value').text)

driver.find_element_by_id('answer').send_keys(str(calc(x)))
driver.execute_script("window.scrollBy(0, 100);")
button = driver.find_element_by_xpath("/html/body/div/form/button")
#driver.execute_script("return arguments[0].scrollIntoView(true);", button)

driver.find_element_by_id('robotCheckbox').click()
driver.find_element_by_id('robotsRule').click()

button.click()

from selenium import webdriver
import math, os, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/explicit_wait2.html')

button = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR"))


driver.find_element_by_tag_name('button').click()

x = int(driver.find_element_by_id('input_value').text)
driver.find_element_by_id('answer').send_keys(str(calc(x)))
driver.find_element_by_tag_id('solve').click()

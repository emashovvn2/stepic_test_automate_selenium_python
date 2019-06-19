from selenium import webdriver
import os, time




gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
driver = webdriver.Firefox(executable_path=gecko+'.exe')
driver.get('http://suninjuly.github.io/file_input.html')

driver.find_element_by_xpath('/html/body/div/form/div/input[1]').send_keys('qwe')
driver.find_element_by_xpath('/html/body/div/form/div/input[2]').send_keys('qwe2')
driver.find_element_by_xpath('/html/body/div/form/div/input[3]').send_keys('qwe@asd.ru')
file = driver.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file.send_keys(file_path)
driver.find_element_by_tag_name("button").click()


from selenium import webdriver
import math, os, time, unittest

class unittest1(unittest.TestCase):
  def test_1(self):
    self.gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    self.browser = webdriver.Firefox(executable_path=self.gecko+'.exe')
    self.link = "http://suninjuly.github.io/registration1.html"
    #self.browser = webdriver.Chrome()
    self.browser.get(self.link)
    # Ваш код, который заполняет обязательные поля
    self.element1 = self.browser.find_element_by_css_selector('[placeholder = "Введите имя"]')
    self.element1.send_keys("Мой ответ1")
    self.element2 = self.browser.find_element_by_css_selector('[placeholder = "Введите фамилию"]')
    self.element2.send_keys("Мой ответ2")
    self.element3 = self.browser.find_element_by_css_selector('[placeholder = "Введите Email"]')
    self.element3.send_keys("Мой ответ3")
    # Отправляем заполненную форму
    self.button = self.browser.find_element_by_css_selector("button.btn")
    self.button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    self.welcome_text = self.welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    self.assertEqual(self.welcome_text, 'Поздравляем! Вы успешно зарегистировались!', "ot good")
    self.browser.close()

  def test_2(self):
    self.gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    self.browser = webdriver.Firefox(executable_path=self.gecko+'.exe')
    self.link = "http://suninjuly.github.io/registration2.html"
    #self.browser = webdriver.Chrome()
    self.browser.get(self.link)
    # Ваш код, который заполняет обязательные поля
    self.element1 = self.browser.find_element_by_css_selector('[placeholder = "Введите имя"]')
    self.element1.send_keys("Мой ответ1")
    self.element2 = self.browser.find_element_by_css_selector('[placeholder = "Введите фамилию"]')
    self.element2.send_keys("Мой ответ2")
    self.element3 = self.browser.find_element_by_css_selector('[placeholder = "Введите Email"]')
    self.element3.send_keys("Мой ответ3")
    # Отправляем заполненную форму
    self.button = self.browser.find_element_by_css_selector("button.btn")
    self.button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    self.welcome_text = self.welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    self.assertEqual(self.welcome_text, 'Поздравляем! Вы успешно зарегистировались!', "ot good")
    self.browser.close()
    
if __name__ == "__main__":
    unittest.main()
    

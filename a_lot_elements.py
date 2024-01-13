# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = 'http://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     link = browser.find_element(By.CLASS_NAME, 'text')
#     print(link.text)

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_elements(By.CLASS_NAME, 'text')
    for i in link:
        print(i.text.split())

from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    p_elements = browser.find_elements(By.XPATH, "//div[@class='text']")
    for i in p_elements:
        print(i.text)
    # Проходимся по списку найденных элементов и выводим их текст
    for i, p_element in enumerate(p_elements):
        print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")
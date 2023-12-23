from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание объекта ChromeOptions для дополнительных настроек браузера
options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
options_chrome.add_argument('--headless')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://donrobot.ru/'
    browser.get(url)
    
    # Ищем элемент по тегу 'a' (ссылку)
    a = browser.find_element(By.CLASS_NAME, 'text_oned')
    
    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.text)
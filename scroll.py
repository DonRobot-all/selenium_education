# import time
# from selenium import webdriver

# with webdriver.Chrome() as browser:
    # browser.get('http://parsinger.ru/scroll/1/')
    # # browser.execute_script("window.scrollBy(0,5000)")
    # # time.sleep(10)


    # for i in range(0, 20000, 1000):
    #     browser.execute_script(f"window.scrollBy(0,{i})")
    #     time.sleep(1)

    
# Представим, что у вас есть сайт, который имеет разные высоты страниц. 
# Мы можем получить значение высоты непосредственно той части сайта, 
# которая попадает в область вашей видимости, или значение высоты всего сайта.

# Команда return document.body.scrollHeight вернёт значение высоты основного 
# элемента на странице — body.

# import time
# from selenium import webdriver

# with webdriver.Chrome() as browser:
#     browser.get('https://donrobot.ru')
#     height = browser.execute_script("return document.body.scrollHeight")
#     time.sleep(2)
#     print(height)
#     browser.execute_script("alert('Что ты натворил')")
#     time.sleep(2)
    # Код window.innerHeight используется для получения высоты, 
    # window.innerWidth — для получения ширины видимой области.
    # Определённые методы, такие как .click() или .send_keys()и др., 
    # могут быть выполнены только в случае, если нужный элемент расположен 
    # в этой видимой зоне экрана.


# Синтаксис: webdriver.execute_script(script, *args).

# В методе .execute_script() можно использовать различные полезные параметры. Полный список всех событий можно просмотреть тут и тут, но ниже приведены те, которые чаще всего используются при написании парсеров:

#     .execute_script("return arguments[0].scrollIntoView(true);", element) — прокручивает родительский контейнер элемента таким образом, чтобы element, для которого вызывается scrollIntoView, был виден пользователю.

#     .execute_script("window.open('http://parsinger.ru', 'tab2');") — создаст новую вкладку в браузере с именем "tab2".

#     .execute_script("return document.body.scrollHeight") — вернёт значение высоты элемента <body>.

#     .execute_script("return window.innerHeight") — вернёт значение высоты окна браузера.

#     .execute_script("return window.innerWidth") — вернёт значение ширины окна браузера.

#     .execute_script("window.scrollBy(X, Y)") — прокрутит документ на заданное число пикселей по осям X и Y.
#         X — смещение в пикселях по горизонтали.
#         Y — смещение в пикселях по вертикали.

#     .execute_script("alert('Ура Selenium')") — вызывает модальное окно Alert.

#     .execute_script("return document.title;") — возвращает title открытого документа.

#     .execute_script("return document.documentURI;") — возвращает URL документа.

#     .execute_script("return document.readyState;") — возвращает состояние загрузки страницы; вернёт "complete", если страница загрузилась.

#     .execute_script("return document.anchors;") — возвращает список всех якорей на странице.
#         [x.tag_name for x in browser.execute_script("return document.anchors;")] — этот код позволяет получить список всех тегов с якорями. Очень полезная инструкция, особенно если при скроллинге элемент для "зацепления" не найден.

#     .execute_script("return document.cookie;") — возвращает строку, содержащую все cookies документа, разделённые точкой с запятой.

#     .execute_script("return document.domain;") — возвращает домен текущего документа.

#     .execute_script("return document.forms;") — возвращает список всех форм на странице.

#     .execute_script("window.scrollTo(x-coord, y-coord);") — прокручивает документ до указанных координат:
#         x-coord — позиция по горизонтальной оси, которая будет отображена вверху
#         y-coord — позиция по вертикальной оси, которая будет отображена вверху слева.

#     .execute_script("return document.getElementsByClassName('container');") — возвращает список всех элементов с классом 'container'.
#     .execute_script("return document.getElementsByTagName('container');") — возвращает список всех элементов с тегом 'container'.
     
#     .execute_script("return document.getElementById('some-id');") —  возвращает элемент с указанным ID 'some-id'.


# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     tags_input = browser.find_elements(By.TAG_NAME, 'input')

#     for input in tags_input:
#         input.send_keys(Keys.DOWN)
#         time.sleep(1)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# # Инициализация драйвера
# driver = webdriver.Chrome()

# # Открыть веб-страницу (замените URL на ваш адрес)
# driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

# # Найти элемент на странице с использованием локатора By
# draggable = driver.find_element(By.ID, "draggable")

# # Использование ActionChains для выполнения перетаскивания элемента
# actions = ActionChains(driver)

# # 1. Переместить блок влево на 100px
# actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

# # 2. Переместить блок вниз на 100px
# actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

# # 3. Переместить блок вправо на 100px
# actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

# # 4. Переместить блок вверх на 100px
# actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

# # Закрыть браузер после завершения
# driver.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.7/5/index.html")
actions = ActionChains(driver)
a = driver.find_element(By.ID, 'button1')
time_wait = a.get_attribute('value')
element = driver.find_element(By.ID, "button1")
actions.click_and_hold(element).pause(float(time_wait)).release(element).perform()
a = driver.find_element(By.ID, 'button2')
time_wait = a.get_attribute('value')
element = driver.find_element(By.ID, "button2")
actions.click_and_hold(element).pause(float(time_wait)).release(element).perform()
a = driver.find_element(By.ID, 'button3')
time_wait = a.get_attribute('value')
element = driver.find_element(By.ID, "button3")
actions.click_and_hold(element).pause(float(time_wait)).release(element).perform()
a = driver.find_element(By.ID, 'button4')
time_wait = a.get_attribute('value')
element = driver.find_element(By.ID, "button4")
actions.click_and_hold(element).pause(float(time_wait)).release(element).perform()
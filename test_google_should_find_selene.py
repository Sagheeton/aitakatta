#просто импорт браузера
from selene import have, be
from selene.support.shared import browser
#импорт вебдрайвера
from selenium import webdriver
#нужные для прописывание драйвера импорты
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#импотируем предварительно установленную библиотеку
import chromedriver_autoinstaller

#устанавливаем нужный драйвер, если его еще нет и передаем в переменую
s = chromedriver_autoinstaller.install()
#заявляем опции
options = Options()
#необязательный аргумент, как я понимаю, для открытия в полный размер браузера
options.add_argument("start-maximized")
#расположение браузера
# options.binary_location=r'C:\Users\saghe\AppData\Local\Vivaldi\Application\vivaldi.exe'
#создаем драйвер
driver = webdriver.Chrome(service=Service(s))

#сообщаем браузеру какой дрейвер использовать
browser.set_driver(driver);

#наконец открываем браузер
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser tests in Python'))
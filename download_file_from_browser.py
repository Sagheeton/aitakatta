import os.path
import time

from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': os.path.join(current_dir, 'downloads'),
    'download.prompt_for_download': False
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver
browser.open('https://demoqa.com/upload-download')

os.remove(r'downloads\sampleFile.jpeg')

s('#downloadButton').click()
time.sleep(2)

assert os.path.getsize(r'downloads\sampleFile.jpeg') == 4096, 'Filesize is not 4096'
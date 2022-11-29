import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Library.Config import Config
from selenium.webdriver.chrome.options import Options


path=r"C:\Users\ASUS\PycharmProjects\Ajio_search_module\screenshot\\"

# firefox_path=r"C:\Users\ASUS\Downloads\geckodriver-v0.32.0-win32\geckodriver.exe"
@pytest.fixture(params=["Chrome","Edge"])

def _driver(request):
    if request.param=="Chrome":
        driver=webdriver.Chrome(Config.Chrome_driver_path)
        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")

    # elif request.param=="Firefox":
    #     options=Options()
    #     options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
    #     driver=webdriver.Firefox(executable_path=Config.Firefox_driver_path,options=options)
    #     # driver=webdriver.Firefox(Config.Firefox_driver_path)

    elif request.param=="Edge":
        driver=webdriver.Edge(Config.Edge_driver_path)
        opt = webdriver.ChromeOptions
        opt.add_argument("--disable-notifications")


    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.save_screenshot(path + "screenshot.png")
    driver.close()



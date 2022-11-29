import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Library.Config import Config

from DATA.reading_objects import ReadExcel
read_excel=ReadExcel
locators_objects=read_excel.read_locators(Config.read_locators,"search_objects")
#define a class and create methods or functions

class Search:
    def __init__(self,driver):
        self.driver=driver

#Search a product
    def search_product(self,Search_keys):
        self.driver.find_element(*locators_objects["search_bar"]).send_keys(Search_keys)
        time.sleep(3)
        self.driver.find_element(*locators_objects["search_bar"]).click()
        time.sleep(2)

    def btn_click(self):
        self.driver.find_element(*locators_objects["btn_click"]).click()
        time.sleep(5)

#Sort a product
    def sort_click(self):
        self.driver.find_element(*locators_objects["sort_click"]).click()
        time.sleep(5)

    def sort_by_hightest(self):
        self.driver.find_element(*locators_objects["sort_by_highest"]).click()
        time.sleep(2)


    def sort_by_discount(self):
        self.driver.find_element(*locators_objects["sort_by_discount"]).click()
        time.sleep(2)

    def sort_by_relevance(self):
        self.driver.find_element(*locators_objects["sort_by_relevance"]).click()
        time.sleep(2)

    def sort_by_whatsnew(self):
        self.driver.find_element(*locators_objects["sort_by_whatsnew"]).click()
        time.sleep(5)

    def sort_by_lowest(self):
        self.driver.find_element(*locators_objects["sort_by_lowest"]).click()


#Mouse functions
#MEN
    def men_search(self):
        act_obj = ActionChains(self.driver)
        men_search = self.driver.find_element(*locators_objects["men_search"])
        act_obj.move_to_element(men_search).perform()
        time.sleep(2)
        self.driver.find_element(*locators_objects['trousers_enter']).click()
#WOMEN
    def women_search(self):
        act_obj = ActionChains(self.driver)
        women_search = self.driver.find_element(*locators_objects["women_search"])
        act_obj.move_to_element(women_search).perform()
        time.sleep(2)
        self.driver.find_element(*locators_objects['dresses_enter']).click()
#KIDS
    def kids_search(self):
        act_obj = ActionChains(self.driver)
        kids_search = self.driver.find_element(*locators_objects["kids_search"])
        act_obj.move_to_element(kids_search).perform()
        time.sleep(2)
        self.driver.find_element(*locators_objects['games_enter']).click()

# INDIE

    def indie_search(self):
        act_obj = ActionChains(self.driver)
        indie_search = self.driver.find_element(*locators_objects["indie_search"])
        act_obj.move_to_element(indie_search).perform()
        time.sleep(2)
        self.driver.find_element(*locators_objects["kalamkari_enter"]).click()

# HOME AND KITCHEN
    def home_and_kit(self):
        act_obj = ActionChains(self.driver)
        home_and_kit = self.driver.find_element(*locators_objects["home_and_kit"])
        act_obj.move_to_element(home_and_kit).perform()
        time.sleep(2)
        self.driver.find_element(*locators_objects["fengshui_enter"]).click()

#Filters

#Price
    def price_btn(self):
        self.driver.find_element(*locators_objects["price_btn"]).click()
        time.sleep(3)
        self.driver.find_element(*locators_objects["price_2_25"]).click()
        time.sleep(2)

#Occasion
    def occ_btn(self):
        self.driver.find_element(*locators_objects["occ_click"]).click()
        time.sleep(3)
        self.driver.find_element(*locators_objects["occ_cas"]).click()

#Discount
    def dis_click(self):
        self.driver.find_element(*locators_objects["dis_click"]).click()
        time.sleep(2)
        self.driver.find_element(*locators_objects["dis_20"]).click()
        time.sleep(2)



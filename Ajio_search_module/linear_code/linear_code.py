import time

from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path=r"C:\Users\ASUS\Downloads\chromedriver_win32\chromedriver.exe"
opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

driver=webdriver.Chrome(path,options=opt)
driver.get('https://www.ajio.com/')
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(30)
# search=driver.find_element("xpath",'//input[@name="searchVal"]')
# btn=driver.find_element("xpath",'//button[@type="submit"]/..//span')
# driver.find_element("xpath",'//a[@class="search-suggestionList  "]')

#Search
# To search a product by product name
# search.send_keys("Kurta")
# btn.click()

# search.send_keys("jeANs")
# search.send_keys(Keys.ENTER)

# To search a product by brand name

# search.send_keys("Puma")
# search.send_keys(Keys.ENTER)

# To search a product by product code

# search.send_keys("441132678001")
# search.send_keys((Keys.ENTER))

# To search a product by product description

# search.send_keys("kurta with palazzo")
# search.send_keys(Keys.ENTER)

#Negative test case
# search.send_keys("b2r477j89")
# search.send_keys(Keys.ENTER)


#############################
#SORT BY
# driver.find_element_by_xpath("//div[@class = 'filter-dropdown']").click()
# driver.find_element("xpath",'//div[@class="filter-dropdown"]/..//select//option[1]').click()
# time.sleep(2)
# driver.find_element("xpath",'//div[@class="filter-dropdown"]/..//select//option[2]').click()
# time.sleep(2)
# driver.find_element("xpath",'//div[@class="filter-dropdown"]/..//select//option[3]').click()
# time.sleep(2)
# driver.find_element("xpath",'//div[@class="filter-dropdown"]/..//select//option[4]').click()
# time.sleep(2)
# driver.find_element("xpath",'//div[@class="filter-dropdown"]/..//select//option[5]').click()
# # time.sleep(2)

#################################

driver.find_element("xpath",'//input[@name="searchVal"]').send_keys("shoes")
driver.find_element("xpath",'//button[@type="submit"]/..//span').click()
time.sleep(2)
for i in range(1,6):
    driver.find_element("xpath", f'//div[@class="filter-dropdown"]/..//select//option[{i}]').click()



##############################
#APPLY FILTERS
#Price
driver.find_element("xpath",'//span[text()="price"]').click()
time.sleep(3)
driver.find_element("xpath",'//label[@for="Rs.2001-2500"]').click()
time.sleep(2)
#
# #Occasion
# driver.find_element('//span[text()="occasion"]').click()
# time.sleep(3)
# driver.find_element('//label[@for="Casual"]').click()
#
# #Discount
# driver.find_element('//span[text()="discount"]').click()
# time.sleep(2)
# driver.find_element('//label[@for="21-30%"]').click()
# time.sleep(2)
#
#
# #MOUSE MOVEMENTS
# act_obj=ActionChains(driver)
#MEN
# men_search=driver.find_element("xpath",'//a[@title="MEN"]')
# act_obj.move_to_element(men_search).perform()
# time.sleep(2)
# driver.find_element("xpath",'//a[@title="Trousers & Pants"]').click()

#WOMEN
# women_search=driver.find_element("xpath",'//a[@title="WOMEN"]')
# act_obj.move_to_element(women_search).perform()
# time.sleep(2)
# driver.find_element("xpath",'//a[@title="Dresses"]').click()

#KIDS
# kids_search=driver.find_element("xpath",'//a[@title="KIDS"]')
# act_obj.move_to_element(kids_search).perform()
# time.sleep(2)
# driver.find_element("xpath",'//a[@title="Gaming, Robots & Vehicles"]').click()

#INDIE
# indie_search=driver.find_element("xpath",'//a[@title="INDIE"]')
# act_obj.move_to_element(indie_search).perform()
# time.sleep(2)
# driver.find_element("xpath",'//a[@title="Kalamkari"]').click()

#HOME AND KITCHEN
# home_and_kit=driver.find_element("xpath",'//a[@title="HOME AND KITCHEN"]')
# act_obj.move_to_element(home_and_kit).perform()
# time.sleep(2)
# driver.find_element("xpath",'//a[@title="Fengshui"]').click()
import pytest
from POM.SEARCH_MODULE import Search
from DATA.reading_objects import ReadExcel
from Library.Config import Config
class Test_Search:
    read_xl=ReadExcel()

#creating an object of the class in reading_objects file and accessing the methods in the object

    details=read_xl.read_keys(Config.read_keys)
    @pytest.mark.parametrize('Search_keys',details)

#This allows us to pass multiple arguments and fixtures at the testfunction

    def test_search01(self,Search_keys,_driver):
        try:
            sc3 = Search(_driver)
            sc3.search_product(Search_keys)
            sc3.btn_click()
            sc3.sort_click()
            sc3.sort_by_whatsnew()
            sc3.price_btn()
            sc3.dis_click()
            sc3.occ_btn()

        except:
           "TEST CASE FAILED"

        text = _driver.find_element("xpath", '//div[@class="header2"]').text
        if text==Search_keys:
            _driver.close()
            assert True,"TEST PASSED"

#Mouse operations of searching a product
    def test_search02(self, _driver):
        try:
            sc2 = Search(_driver)
            sc2.men_search()
            sc2.women_search()
            sc2.kids_search()
            sc2.indie_search()
            sc2.home_and_kit()

        except:
            "TEST CASE FAILED"










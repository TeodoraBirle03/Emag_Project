from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class FavoritesPage(BasePage):

    SEARCH_INPUT = (By.ID, 'searchboxTrigger')

    def search_after(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('biscuiti')
        self.driver.find_element(By.XPATH, f'(//a[@class="searchbox-suggestion-result searchbox-active-item"])[2]').click()
        actual = self.driver.current_url
        expected  = 'https://www.emag.ro/search/dulciuri-1/biscuiti/c?ref=autosuggest_category1%252Csearch_bar_biscuiti'
        self.assertEqual(actual, expected, 'You have landed on the wrong page')
        sleep(2)

    def click_on_favorites_icon_by_product_name(self, product_name):
        print('teodora')
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{product_name}")]/parent::div/parent::div/parent::div/parent::div//i[@class="em em-fav em-fav-bold"]').click()
        sleep(1)

    def click_favorites_list(self):
        self.driver.find_element(By.ID, "my_wishlist").click()
        sleep(2)

    def verify_favorites_url(self):
        self.verify_page_url('https://www.emag.ro/favorites?ref=ua_favorites')

   # # trebuie sa verific ca lista este completa, contine 2 produse

    def verify_element_is_displayed_in_favorites(self, product_name):
        self.verify_element_is_displayed_as_list(product_name)
        # elem_list = self.driver.find_elements(by, product_name)
        # print(elem_list)
        # self.assertEqual(len(elem_list), 1, 'Elements not displayed')

    def click_sterge_produs(self, product_name):
        self.driver.find_element(By.XPATH, f'//span[contains(text(), "{product_name}")]/parent::a/parent::h2/parent::div/parent::div//span[contains(text(), "Sterge")]').click()
        # self.verify_element_is_displayed_as_list(self, by, product_name)

    def verify_element_is_not_displayed(self, by, product_name):
        elem_list = self.driver.find_elements(by, product_name)
        self.assertEqual(len(elem_list), len(elem_list)-1, 'Element is still displayed')





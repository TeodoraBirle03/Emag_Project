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

    ACCEPT_COOKIES_BTN = (By.XPATH, '//button[text()="Accept"]')
    INTRA_IN_CONT_CLOSE_BTN = (By.XPATH, '(//i[@class="em em-close"]/parent::button)[3]')
    SEARCH_INPUT = (By.ID, 'searchboxTrigger')
    DELETE_BTN = (By.XPATH, '//span[contains(text(), "Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g" )]/parent::a/parent::h2/parent::div/parent::div//span[contains(text(), "Sterge")]')

    def navigate_to_home_page(self):
        self.driver.get('https://www.emag.ro/')

    def click_accept_cookies_btn(self):
        self.click_if_present(*self.ACCEPT_COOKIES_BTN)

    def click_intra_in_cont_close_btn(self):
        self.click_if_present(*self.INTRA_IN_CONT_CLOSE_BTN)

    def search_after(self):
        self.wait_and_fill_elem(*self.SEARCH_INPUT)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('biscuiti')
        self.driver.find_element(By.XPATH, f'(//a[@class="searchbox-suggestion-result searchbox-active-item"])[2]').click()
        sleep(2)

    def click_on_favorites_icon(self, product_name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{product_name}"]/parent::div/parent::div/parent::div/parent::div//i[@class="em em-fav em-fav-bold"]').click()

    def click_favorites_list(self):
        self.driver.find_element(By.ID, "my_wishlist").click()
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/favorites?ref=ua_favorites'
        self.assertEqual(actual, expected, 'You have landed on the wrong page')

    def click_sterge_produs(self, product_name):
        self.driver.find_element(By.XPATH, f'//span[contains(text(), "{product_name}")]/parent::a/parent::h2/parent::div/parent::div//span[contains(text(), "Sterge")]').click()







from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get('https://emag.ro')
sleep(2)
driver.find_element(By.XPATH, '//button[text()="Accept"]').click()
sleep(2)
driver.find_element(By.XPATH, '(//i[@class="em em-close"]/parent::button)[3]').click()
# driver.find_element(By.XPATH, f'//button[@class="js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none"]').click()
sleep(1)

# scriu in campul de cautare "biscuiti"
driver.find_element(By.ID, "searchboxTrigger").send_keys('biscuiti')
sleep(2)
# fac click pe randul doi
driver.find_element(By.XPATH, f'(//a[@class="searchbox-suggestion-result searchbox-active-item"])[2]').click()
sleep(2)
# driver.find_element(By.XPATH, f'(//i[@class="em em-close"]/parent::button)[3]').click()


# fac click pe inima de la produs

biscuit1 = driver.find_element(By.XPATH, f'//a[contains(text(), "Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g")]/parent::div/parent::div/parent::div/parent::div//i[@class="em em-fav em-fav-bold"]')
biscuit1.click()

sleep(2)
biscuit2 = driver.find_element(By.XPATH, f'//a[contains(text(), "2 x Biscuiti cu unt Leibniz, 200 gr.")]/parent::div/parent::div/parent::div//i[@class="em em-fav em-fav-bold"]')
biscuit2.click()
sleep(2)
driver.find_element(By.ID, "my_wishlist").click()
sleep(2)
driver.find_element(By.XPATH, '//span[contains(text(), "Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g" )]/parent::a/parent::h2/parent::div/parent::div//span[contains(text(), "Sterge")]').click()
sleep(2)
# driver.find_element(By.XPATH, f"//a[contains(text(), "Sampon L'Oreal Paris Elseve Dream Long reparator pentru par lung, deteriorat, 400 ml")]/parent::div/parent::div/parent::div/parent::div//i[@class="em em-fav em-fav-bold"]")
# (//span[contains(text(), "Sampon de par")])[1]
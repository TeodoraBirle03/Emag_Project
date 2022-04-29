from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.favorites_page import FavoritesPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.product_page = ProductsPage()
    context.cart_page = CartPage()
    context.favorites_page = FavoritesPage()


def after_all(context):
    context.browser.close()
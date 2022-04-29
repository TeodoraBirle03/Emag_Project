from behave import *

# @given('home: I am a user on emag.ro Home page')
# def step_impl(context):
#     context.home_page.navigate_to_home_page()
#     context.home_page.click_accept_cookies_btn()
#     context.home_page.click_intra_in_cont_close_btn()

@when('home: I search after "biscuiti"')
def step_impl(context):
    context.favorites_page.search_after()

@when('products: I add product to favorites list by "{product_name}"')
def step_impl(context, product_name):
    context.favorites_page.click_on_favorites_icon_by_product_name(product_name)

@when('products: I click on favorites icon')
def step_impl(context):
    context.favorites_page.click_favorites_list()

@then('products: I verify that I am on favorites page')
def step_impl(context):
    context.favorites_page.verify_favorites_url()

@then('favorites: I verify that the favorites list is complete by "{product_name}"')
def step_impl(context, product_name):
    context.favorites_page.verify_element_is_displayed_as_list(product_name)

@when('favorites: I delete one product by "{product_name}"')
def step_impl(context):
    context.favorites_page.click_sterge_produs()

@then('favorites: I see one element less in the list')
def step_impl(context):
    context.favorites_page.verify_element_is_not_displayed
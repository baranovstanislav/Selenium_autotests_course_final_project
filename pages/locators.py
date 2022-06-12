from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(1) > .alertinner')
    PRICE_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(3) > .alertinner > p:nth-of-type(1)')
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, '.product_main > p:nth-of-type(1)')

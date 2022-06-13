from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    NEW_USER_EMAIL_FORM = (By.NAME, 'registration-email')
    NEW_USER_PASSWORD_FORM1 = (By.NAME, 'registration-password1')
    NEW_USER_PASSWORD_FORM2 = (By.NAME, 'registration-password2')
    REGISTER_ACCEPT_LINK = (By.NAME, 'registration_submit')

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(1) > .alertinner')
    PRODUCT_NAME_IN_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(1) > .alertinner > strong')
    PRICE_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(3) > .alertinner > p:nth-of-type(1)')
    PRICE_IN_MESSAGE_LINK = (By.CSS_SELECTOR, '#messages > .alert:nth-of-type(3) > .alertinner > p:nth-of-type(1) > strong')
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, '.product_main > p:nth-of-type(1)')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_CONTENT_LINK = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_MESSAGE_LINK = (By.CSS_SELECTOR, '#content_inner > p:nth-of-type(1)')
    

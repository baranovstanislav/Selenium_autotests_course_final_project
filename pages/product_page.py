from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_link.click()
        self.solve_quiz_and_get_code()
    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE_LINK), "Add_to_basket message is not presented"
    def should_be_product_name_in_message(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LINK).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_LINK).text 
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE_LINK).text
        print('имя:', name, 'сообщение:', message, 'имя в сообщении', name_in_message)
        assert name_in_message == name, 'product name in message is incorrect'
    def should_price_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET_MESSAGE_LINK), "Price_basket message is not presented"
    def should_be_product_price_in_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LINK).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE_LINK).text
        message = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_MESSAGE_LINK).text        
        print('цена товара:', price, 'сообщение о цене товара в корзине:', message, 'цена в сообщении', price_in_message)
        assert price_in_message == price, 'price in message is incorrect'          

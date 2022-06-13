from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
   def should_not_be_basket_content(self):
      assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_LINK), "Goods are presented, but should not be"
   def should_be_basket_empty_message(self):
      assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE_LINK), "Empty_basket message is not presented"               
    
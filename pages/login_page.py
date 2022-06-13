from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Login link isn\'t presented'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn't presented"
        
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.browser.find_element(*LoginPageLocators.NEW_USER_EMAIL_FORM).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.NEW_USER_PASSWORD_FORM1).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.NEW_USER_PASSWORD_FORM2).send_keys(self.password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_ACCEPT_LINK)
        register_button.click()